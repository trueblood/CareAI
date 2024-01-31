from flask import Flask, jsonify, request
from flask_cors import CORS
from api.controllers.defaultController import DefaultController

app = Flask(__name__)

CORS(app, resources={
    r"/generate_story": {
        "origins": [
            "http://localhost:5001",
            "https://storybuddy.angrybuddy.com",
            "http://192.168.1.53:5070",
            "http://192.168.1.53:5080",
            "http://75.187.70.207:5070",
            "*"
        ]
    }
})

@app.route('/')
def index():
    return jsonify({'message': 'server up and running'})

@app.route('/generate_incident_description', methods=['POST'])
def generate_incident_description():
    try:
        input_text = request.json.get('input_text')
        response_length = request.json.get('response_length')
        defaultController = DefaultController()
        result = defaultController.generate_incident_description(input_text, int(response_length))
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})
    

if __name__ == '__main__':
    app.run(port=5100, debug=True)  # Set the desired port numbers