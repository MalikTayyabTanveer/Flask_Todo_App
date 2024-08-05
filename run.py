from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pyngrok import ngrok
import os

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
    return redirect(url_for('index'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    # Start Flask app in a separate thread
    from threading import Thread
    flask_thread = Thread(target=lambda: app.run(port=5000))
    flask_thread.start()

    # Connect to ngrok
    public_url = ngrok.connect(5000)
    print(f"Public URL: {public_url}")
