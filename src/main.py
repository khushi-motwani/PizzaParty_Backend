from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200

# TODO import and register additional routes from other modules (blueprint) here

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
    
    
