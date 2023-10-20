from flask import Flask, request, render_template, send_file
from PIL import Image
import io
from detection_custom import detect
app = Flask(__name__)

# Function to process the image
def process_image(input_image):

    img = Image.open(input_image)
    #img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return img

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if a file was submitted
        if 'image' in request.files:
            image = request.files['image']
            # Ensure it's an allowed image file type (e.g., 'jpg', 'png', 'jpeg', 'gif', etc.)
            if image:
                # Process the image
                processed_image = process_image(image)
                # Save the processed image temporarily
                result_image_path = 'static/images/result_image.jpg'
                processed_image.save(result_image_path)
                threshhold=request.form.get('threshhold')
                detect(float(threshhold))
                predict_image_path='static/images/pred.jpg'
                return render_template('index.html', result_image=predict_image_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)