from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image
from werkzeug.utils import secure_filename
import io
import os
from pathlib import Path
import uuid

app = Flask(__name__)

# v2 - Updated sitemap
# Lazy load rembg to avoid startup issues
_rembg_remove = None

def get_remove_function():
    global _rembg_remove
    if _rembg_remove is None:
        from rembg import remove
        _rembg_remove = remove
    return _rembg_remove

# Create uploads directory
UPLOAD_DIR = Path('uploads')
UPLOAD_DIR.mkdir(exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resize')
def resize_page():
    return render_template('resize.html')

@app.route('/bulk')
def bulk_page():
    return render_template('bulk.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/id-background-remover')
def id_remover():
    return render_template('id-remover.html')

@app.route('/passport-photo-remover')
def passport_remover():
    return render_template('passport-remover.html')

@app.route('/product-photo-remover')
def product_remover():
    return render_template('product-remover.html')

@app.route('/avatar-maker')
def avatar_maker():
    return render_template('avatar-maker.html')

@app.route('/image-compressor')
def image_compressor():
    return render_template('image-compressor.html')

@app.route('/image-converter')
def image_converter():
    return render_template('image-converter.html')

@app.route('/watermark-remover')
def watermark_remover():
    return render_template('watermark-remover.html')

@app.route('/image-upscaler')
def image_upscaler():
    return render_template('image-upscaler.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/best-background-remover-tools')
def blog_best_tools():
    return render_template('blog-best-tools.html')

@app.route('/blog/how-to-remove-background')
def blog_how_to():
    return render_template('blog-how-to.html')

@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml'), 200, {'Content-Type': 'application/xml'}

@app.route('/robots.txt')
def robots():
    return render_template('robots.txt'), 200, {'Content-Type': 'text/plain'}

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    try:
        # Cleanup old files
        cleanup_old_files()
        
        # Generate unique ID
        job_id = str(uuid.uuid4())
        
        # Read input image
        input_image = Image.open(file.stream)
        
        # Remove background
        remove_func = get_remove_function()
        output_image = remove_func(input_image)
        
        # Save output
        output_path = UPLOAD_DIR / f'{job_id}.png'
        output_image.save(output_path, 'PNG')
        
        return jsonify({
            'success': True,
            'job_id': job_id,
            'message': 'Background removed successfully!'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<job_id>')
def download(job_id):
    file_path = UPLOAD_DIR / f'{job_id}.png'
    if file_path.exists():
        return send_file(file_path, as_attachment=True, download_name='background-removed.png')
    return jsonify({'error': 'File not found'}), 404

@app.route('/preview/<job_id>')
def preview(job_id):
    file_path = UPLOAD_DIR / f'{job_id}.png'
    if file_path.exists():
        return send_file(file_path, mimetype='image/png')
    return jsonify({'error': 'File not found'}), 404

@app.route('/resize-image', methods=['POST'])
def resize_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    width = request.form.get('width', type=int)
    height = request.form.get('height', type=int)
    
    if not width or not height:
        return jsonify({'error': 'Width and height required'}), 400
    
    try:
        # Cleanup old files
        cleanup_old_files()
        
        job_id = str(uuid.uuid4())
        input_image = Image.open(file.stream)
        
        # Resize image
        resized_image = input_image.resize((width, height), Image.Resampling.LANCZOS)
        
        # Save output
        output_path = UPLOAD_DIR / f'{job_id}.png'
        resized_image.save(output_path, 'PNG')
        
        return jsonify({
            'success': True,
            'job_id': job_id,
            'message': f'Image resized to {width}x{height}!'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/bulk-remove', methods=['POST'])
def bulk_remove():
    if 'images' not in request.files:
        return jsonify({'error': 'No images provided'}), 400
    
    files = request.files.getlist('images')
    if not files:
        return jsonify({'error': 'No images selected'}), 400
    
    try:
        # Cleanup old files
        cleanup_old_files()
        
        job_id = str(uuid.uuid4())
        job_dir = UPLOAD_DIR / job_id
        job_dir.mkdir(exist_ok=True)
        
        processed_count = 0
        for file in files:
            if file.filename:
                # Sanitize filename to prevent path traversal (SECURITY FIX)
                safe_filename = secure_filename(file.filename)
                if not safe_filename:
                    continue
                
                # Process each image
                input_image = Image.open(file.stream)
                output_image = remove(input_image)
                
                # Save with sanitized filename
                output_path = job_dir / f'nobg_{safe_filename}'
                
                # Ensure path is within job directory (security check)
                if not output_path.resolve().is_relative_to(job_dir.resolve()):
                    continue
                
                output_image.save(output_path, 'PNG')
                processed_count += 1
        
        # Create ZIP file
        zip_path = UPLOAD_DIR / f'{job_id}.zip'
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file_path in job_dir.glob('*'):
                zipf.write(file_path, file_path.name)
        
        return jsonify({
            'success': True,
            'job_id': job_id,
            'count': processed_count,
            'message': f'Processed {processed_count} images!'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download-zip/<job_id>')
def download_zip(job_id):
    zip_path = UPLOAD_DIR / f'{job_id}.zip'
    if zip_path.exists():
        return send_file(zip_path, as_attachment=True, download_name='bulk-backgrounds-removed.zip')
    return jsonify({'error': 'ZIP file not found'}), 404

# Cleanup old files (older than 1 hour)
def cleanup_old_files():
    current_time = time.time()
    # Clean up top-level PNG files
    for file_path in UPLOAD_DIR.glob('*.png'):
        if current_time - file_path.stat().st_mtime > 3600:  # 1 hour
            file_path.unlink()
    # Clean up ZIP files
    for file_path in UPLOAD_DIR.glob('*.zip'):
        if current_time - file_path.stat().st_mtime > 3600:  # 1 hour
            file_path.unlink()
    # Clean up bulk processing job directories
    for job_dir in UPLOAD_DIR.iterdir():
        if job_dir.is_dir() and current_time - job_dir.stat().st_mtime > 3600:  # 1 hour
            import shutil
            shutil.rmtree(job_dir)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
