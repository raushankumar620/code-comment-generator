
from flask import Flask, render_template, request, jsonify
from comment_model import generate_comment

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API route to handle code input and return commented code
@app.route('/generate_comment', methods=['POST'])
def generate_comment_api():
    # Get code from the POST request
    data = request.get_json()
    code = data.get('code', '')

    # Error handling: Check if code is empty
    if not code:
        return jsonify({"error": "No code provided!"}), 400

    # Generate comments using the NLP model
    commented_code = generate_comment(code)

    # Return the commented code as JSON response
    return jsonify({"commented_code": commented_code})

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
