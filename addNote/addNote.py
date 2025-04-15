import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from prometheus_client import generate_latest, REGISTRY, Counter
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qwertyuiop@mysql:3306/defaultdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Initialize metrics
metrics = PrometheusMetrics(app)

# Create a counter manually
notes_counter = Counter('notes_added_total', 'Total number of notes added')

# Define the Note model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
with app.app_context():
    db.create_all()

# Explicitly create metrics endpoint
@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain; version=0.0.4'}

@app.route('/add', methods=['POST'])
def add_note():
    data = request.json
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_note = Note(
        title=data['title'],
        content=data['content'],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.session.add(new_note)
    db.session.commit()
    
    # Increment counter
    notes_counter.inc()

    return jsonify({"message": "Note added successfully", "note_id": new_note.id}), 201

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
    app.run(debug=True, host='0.0.0.0', port=5001)