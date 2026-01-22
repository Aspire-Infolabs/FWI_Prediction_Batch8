from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import os
import warnings

warnings.filterwarnings('ignore', category=UserWarning)

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  

# Load the Ridge model
MODEL_PATH = 'ridge.pkl'

def load_model():
    """Load the Ridge regression model from pickle file"""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file {MODEL_PATH} not found. Please place ridge.pkl in the project directory.")
    
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    return model

try:
    model = load_model()
    print(f"[OK] Model loaded successfully from {MODEL_PATH}")
except FileNotFoundError as e:
    print(f"[WARNING] {e}")
    model = None

@app.route('/')
def index():
    """Serve the main HTML file"""
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict FWI based on input parameters"""
    try:
        if model is None:
            return jsonify({
                'error': 'Model not loaded. Please ensure ridge.pkl exists in the project directory.'
            }), 500
        
        data = request.get_json()
        
       
        features = [
            float(data.get('Temperature', 0)),
            float(data.get('RH', 0)),
            float(data.get('Ws', 0)),
            float(data.get('Rain', 0)),
            float(data.get('FFMC', 0)),
            float(data.get('DMC', 0)),
            float(data.get('DC', 0)),
            float(data.get('ISI', 0)),
            float(data.get('BUI', 0))
        ]
        
        features_array = np.array([features])
        
        prediction = model.predict(features_array)
       
        fwi = float(prediction[0]) if isinstance(prediction, np.ndarray) else float(prediction)
        
        fwi = max(0, fwi)
        
        print(f"Prediction: FWI = {fwi}, Features = {features}")
        
        return jsonify({
            'fwi': round(fwi, 2),
            'success': True
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS, etc.) - must be last route"""
    if filename.endswith('.py') or filename.startswith('venv') or filename.startswith('.'):
        return jsonify({'error': 'File not found'}), 404
    try:
        return send_from_directory('.', filename)
    except:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    print("Fire Weather Index Prediction API")
    print("=" * 50)
    if model:
        print("[OK] Model ready for predictions")
    else:
        print("[WARNING] Model not loaded - please add ridge.pkl to the directory")
    print("=" * 50)
    print("Starting server on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
