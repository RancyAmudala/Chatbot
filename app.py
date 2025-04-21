from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load your urls.json data
with open('urls.json') as f:
    url_data = json.load(f)

# Route for the home page (shows the form)
@app.route('/')
def index():
    # Make sure 'panda.html' is in the 'templates' folder
    return render_template('panda.html')

# Route for handling the /chat POST request
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message'].lower()
    response = {"url": None, "error": None}

    # Search through all URL entries
    for entry in url_data:
        if any(keyword in user_message for keyword in entry['keywords']):
            response['url'] = entry['url']
            break

    if not response['url']:
        response['error'] = "No matching URL found"

    return jsonify(response)

if __name__ == '__main__':
    print("Starting server...")
    app.run(debug=True)
