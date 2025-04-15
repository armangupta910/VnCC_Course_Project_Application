import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from prometheus_client import generate_latest, REGISTRY, Counter
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qwertyuiop@mysql:3306/defaultdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Initialize metrics
metrics = PrometheusMetrics(app)

# Create a counter manually
notes_counter = Counter('notes_added_total', 'Total number of notes added')

# Define the Note model (same schema as Add Note service)
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

# Check if the database file exists

with app.app_context():
    db.create_all()  # Create tables only if the database file doesn't exist

@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain; version=0.0.4'}


@app.route('/get/<int:id>', methods=['GET'])
def get_note(id):
    note = Note.query.filter_by(id=id).first()
    
    if not note:
        return jsonify({"error": "Note not found"}), 404

    return jsonify({
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "created_at": note.created_at,
        "updated_at": note.updated_at
    }), 200

@app.route('/debug')
def debug():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
