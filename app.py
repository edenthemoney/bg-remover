from flask import Flask, render_template, request, send_file, jsonify
from rembg import remove
from PIL import Image
import io
import os
from pathlib import Path
import uuid
import time

app = Flask(__name__)

# Create uploads directory
UPLOAD_DIR = Path('uploads')
UPLOAD_DIR.mkdir(exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml'), 200, {'Content-Type': 'application/xml'}

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    try:
        # Generate unique ID
        job_id = str(uuid.uuid4())
        
        # Read input image
        input_image = Image.open(file.stream)
        
        # Remove background
        output_image = remove(input_image)
        
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

# Cleanup old files (older than 1 hour)
def cleanup_old_files():
    current_time = time.time()
    for file_path in UPLOAD_DIR.glob('*.png'):
        if current_time - file_path.stat().st_mtime > 3600:  # 1 hour
            file_path.unlink()

if __name__ == '__main__':
    app.run(debug=True, port=5002, threaded=True)
