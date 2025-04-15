import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from prometheus_client import generate_latest, REGISTRY, Counter
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Set custom database path (same as Add Note service)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qwertyuiop@mysql:3306/defaultdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

metrics = PrometheusMetrics(app)

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

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_note(id):
    # Find the note by ID
    note = Note.query.filter_by(id=id).first()
    
    if not note:
        return jsonify({"error": "Note not found"}), 404

    # Delete the note
    db.session.delete(note)
    db.session.commit()

    return jsonify({"message": f"Note with ID {id} deleted successfully"}), 200

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
    app.run(debug=True, host='0.0.0.0', port=5003)
