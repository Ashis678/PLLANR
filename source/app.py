from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Models
class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tasks = db.relationship('Task', backref='template', cascade="all, delete-orphan")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    interval = db.Column(db.Integer, nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey('template.id'), nullable=False)

# Routes
@app.route('/')
def home():
    return render_template('base.html')  # Render your base or home page 
    
@app.route('/templates', methods=['GET', 'POST'])
def template_creator():
    if request.method == 'POST':
        # Get data from form
        template_name = request.form['templateName']
        task_names = request.form.getlist('taskName[]')
        time_intervals = request.form.getlist('timeInterval[]')

        # Create Template and associated Tasks
        new_template = Template(name=template_name)
        for name, interval in zip(task_names, time_intervals):
            new_template.tasks.append(Task(name=name, interval=int(interval)))

        # Save to database
        db.session.add(new_template)
        db.session.commit()

        return redirect(url_for('template_creator'))

    # Fetch templates and tasks from database
    templates = Template.query.all()
    return render_template('template_creator.html', templates=templates)

@app.route('/templates/delete/<int:template_id>', methods=['POST'])
def delete_template(template_id):
    # Find the template by ID and delete it
    template = Template.query.get_or_404(template_id)
    db.session.delete(template)
    db.session.commit()
    return redirect(url_for('template_creator'))

# Initialize database (creates tables if they don't exist)
with app.app_context():
    db.create_all()  # Explicitly create tables during startup

@app.route('/pomodoro', methods=['GET'])
def pomodoro():
    return render_template('pomodoro.html')  # Your Pomodoro Timer page

# Route for the settings page
@app.route('/letsdothis', methods=['GET','POST'])
def letsdothis():
    return render_template('letsdothis.html')  # Timer-related page (or any other)

@app.route('/base', methods=['GET'])
def home111():
    return render_template('base.html')

@app.route('/get_templates') 
def get_templates(): 
    templates = Template.query.all() 
    templates_list = [{'id': template.id, 'name': template.name} 
    for template in templates] 
    return jsonify({'templates': templates_list})

# Route to fetch tasks based on template_id
@app.route('/get_tasks/<int:template_id>')
def get_tasks(template_id):
    # Fetch tasks associated with the template_id using SQLAlchemy
    template = Template.query.get_or_404(template_id)
    tasks = template.tasks  # This retrieves the related tasks automatically

    tasks_list = [{'id': task.id, 'name': task.name, 'interval': task.interval} for task in tasks]
    return jsonify({'tasks': tasks_list})

# Add other routes as needed

if __name__ == '__main__':
    app.run(debug=True)
