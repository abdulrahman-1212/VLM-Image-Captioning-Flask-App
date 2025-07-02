from flask import Flask, request, render_template
from PIL import Image
import os
from caption_model import generate_caption

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/caption', methods=['POST'])
def caption():
    if 'image' not in request.files:
        return "No image uploaded", 400

    file = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    img = Image.open(filepath).convert('RGB')
    caption = generate_caption(img)

    return render_template('result.html', image_path=filepath, caption=caption)

if __name__ == '__main__':
    app.run(debug=True)
