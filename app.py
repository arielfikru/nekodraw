from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Inisialisasi URL API awal
API_URL = "https://2174-35-225-148-232.ngrok-free.app"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data['prompt']
    negative_prompt = data['negative_prompt']
    steps = data['steps']
    cfg_scale = data['cfg_scale']
    seed = data['seed']
    width = data['width']
    height = data['height']

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "seed": seed,
        "width": width,
        "height": height,
    }

    response = requests.post(url=f'{API_URL}/sdapi/v1/txt2img', json=payload)
#    print(response.json())  # Tambahkan baris ini
    r = response.json()

    if 'images' in r:
        return jsonify({"image": r['images'][0]})
    else:
        return jsonify({"error": "No images found in the response"}), 400

@app.route('/update-url', methods=['POST'])
def update_url():
    global API_URL
    data = request.json
    API_URL = data['url']
    return jsonify({"message": "API URL updated successfully!"})

@app.route('/get-models', methods=['GET'])
def get_models():
    response = requests.get(url=f'{API_URL}/sdapi/v1/sd-models')
    return response.json()


if __name__ == '__main__':
    app.run(debug=True)
