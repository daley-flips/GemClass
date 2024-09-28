from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from gemini_test import generate_text

app = Flask(__name__, template_folder='frontend')

CORS(app)

# Initialize conversation history
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    global conversation_history
    data = request.get_json()
    user_input = data.get('data')
    try:
        # Append user's message to the conversation history
        conversation_history.append({'author': 'user', 'content': user_input})

        # Prepare the conversation history as a single string
        conversation_text = ''
        for turn in conversation_history:
            if turn['author'] == 'user':
                conversation_text += f"User: {turn['content']}\n"
            else:
                conversation_text += f"Assistant: {turn['content']}\n"

        # Generate the assistant's response
        response_text = generate_text(conversation_text)

        # Append the assistant's response to the conversation history
        conversation_history.append({'author': 'assistant', 'content': response_text})

        return jsonify({"response": True, "message": response_text})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message": error_message, "response": False})

if __name__ == '__main__':
    app.run()
