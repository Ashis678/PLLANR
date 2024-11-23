from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/templates')
def templates():
    return render_template('templates.html')

@app.route('/time-config')
def time_config():
    return render_template('time_config.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

# Add other routes as needed
