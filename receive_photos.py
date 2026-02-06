from flask import Flask, request, jsonify
import os

app = Flask(__name__)
# PHOTOS_FOLDER = 'photos'
PHOTOS_FOLDER = '/home/k/animation-photos/photos'
os.makedirs(PHOTOS_FOLDER, exist_ok=True)

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo'}), 400
    file = request.files['photo']

    existing = len([f for f in os.listdir(PHOTOS_FOLDER) if f.endswith('.jpg')])
    photo_num = existing + 1
    filename = f'photo_{photo_num:06d}.jpg'
    filepath = os.path.join(PHOTOS_FOLDER, filename)
    file.save(filepath)
    print(f"✓ Saved {filename} (total: {photo_num})")
    return jsonify({'photo_number': photo_num, 'total_photos': photo_num})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
