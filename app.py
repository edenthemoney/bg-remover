from flask import Flask, render_template, jsonify

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()
