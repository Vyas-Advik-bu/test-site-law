from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

# Initialize the application
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
# This allows your HTML file (served from a different origin or file system)
# to communicate with this Python server.
CORS(app)

@app.route('/')
def home():
    """Health check route."""
    return "Server is running!"

@app.route('/api/page1', methods=['GET'])
def page1_data():
    """Backend logic for Page 1"""
    return jsonify({
        "status": "success",
        "page": "Page 1",
        "message": "Welcome to the Dashboard data stream.",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/page2', methods=['GET'])
def page2_data():
    """Backend logic for Page 2"""
    return jsonify({
        "status": "success",
        "page": "Page 2",
        "message": "Settings configuration loaded.",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/page3', methods=['GET'])
def page3_data():
    """Backend logic for Page 3"""
    return jsonify({
        "status": "success",
        "page": "Page 3",
        "message": "User profile data retrieved.",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/page4', methods=['GET'])
def page4_data():
    """Backend logic for Page 4"""
    return jsonify({
        "status": "success",
        "page": "Page 4",
        "message": "Analytics engine ready.",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("Starting Python Backend on port 5000...")
    # debug=True allows the server to auto-reload if you change code
    app.run(debug=True, port=5000)