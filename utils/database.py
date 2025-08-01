import sqlite3
import json

def init_db():
    """Initialize the database"""
    conn = sqlite3.connect('applications.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            discord_username TEXT NOT NULL,
            answers TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def submit_application(user_id, username, discord_username, answers):
    """Submit a new application"""
    try:
        conn = sqlite3.connect('applications.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO applications (user_id, username, discord_username, answers)
            VALUES (?, ?, ?, ?)
        ''', (user_id, username, discord_username, json.dumps(answers)))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def get_pending_applications():
    """Get all pending applications"""
    conn = sqlite3.connect('applications.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM applications WHERE status = "pending"')
    applications = cursor.fetchall()
    conn.close()
    return applications 