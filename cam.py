from flask import Flask, render_template, request
import os
import base64

app = Flask(__name__)

# Ensure the Vexorpro directory exists
SAVE_DIR = "Vexorpro"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('cam5.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json['image']
    
    # Decode base64 image
    image_data = base64.b64decode(data.split(',')[1])
    
    # Find the next available filename
    image_number = 1
    while True:
        file_path = os.path.join(SAVE_DIR, f'captured_image{image_number}.png')
        if not os.path.exists(file_path):
            break
        image_number += 1
    
    # Save file
    with open(file_path, 'wb') as f:
        f.write(image_data)
    
    return {'message': 'Image saved successfully!', 'path': file_path}

if __name__ == '__main__':
    app.run(debug=True)