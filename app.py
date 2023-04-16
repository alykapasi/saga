from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
responses = []

@app.route('/')
def index():
    return render_template('index.html', responses=responses)

@app.route('/api', methods=['POST'])
def api():
    text = request.form.get('textInput')
    response = fetch_openai(text)
    responses.insert(0, response)
    return redirect(url_for('index'))

def fetch_openai(text):
    api_key = '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'
    api_url = 'https://api.openai.com/v1/engines/text-davinci-002/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    data = {
        'temperature': 0.7,
        'top_p': 1,
        'prompt': text,
        'max_tokens': 50,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0,
    }

    response = requests.post(api_url, headers=headers, json=data)
    return response.json()['choices']

if __name__ == '__main__':
    app.run(debug=True)
