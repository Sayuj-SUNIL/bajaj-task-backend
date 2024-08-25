from flask import Flask, request, jsonify,send_file,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "http://localhost:3000"}})

@app.route('/')
def home():
    return "Its up"

@app.route('/process', methods=['POST'])
def process_data():
    # Get the data from the request
    data = request.json.get('data', [])
    
    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    # Find the highest lowercase alphabet
    lowercase_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None
    
    # Prepare the response
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    print("Response being sent:", response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)