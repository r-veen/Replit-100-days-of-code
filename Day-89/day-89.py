from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

messages = []


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    username = request.headers.get('X-Replit-User-Name', 'Guest')
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            messages.insert(0, (username, message))
    return render_template('texting.html',
                           userid=username,
                           messages=messages,
                           enumerate=enumerate)


@app.route('/delete_message/<int:index>', methods=['POST'])
def delete_message(index):
    username = request.headers.get('X-Replit-User-Name', 'Guest')
    if username == '16807368' and 0 <= index < len(messages):
        messages.pop(index)
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
