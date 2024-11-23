from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/templates')
def templates():
    return render_template('template_creator.html')

@app.route('/settings')
def tasks():
    return render_template('settings.html')

@app.route('/logout')
def tasks():
    return render_template('logout.html')

# Add other routes as needed
