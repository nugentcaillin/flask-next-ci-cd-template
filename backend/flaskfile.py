from flask import Flask, request, jsonify

app = Flask(__name__)

default_message = "Hello, this is a Flask app running on Gunicorn inside Docker!"

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": default_message})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)