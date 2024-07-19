from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('obituary_platform.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS obituaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            date_of_death DATE NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            submission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            slug TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return "<style>body{background-color:black;color:white;} a{color:orange;text-decoration:none;} a:hover{color:darkorange;}</style><center>Welcome to the Obituary Platform <br><a href='/submit'>Submit an Obituary</a> | <a href='/view_obituaries'>View Obituaries</a> | <a href='/sitemap.xml'>Sitemap</a></center>"
@app.route('/submit_obituary', methods=['POST'])
def submit_obituary():
    try:
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        date_of_death = request.form['date_of_death']
        content = request.form['content']
        author = request.form['author']
        slug = f"{name.replace(' ', '-').lower()}-{datetime.now().strftime('%Y%m%d%H%M%S')}"

        conn = sqlite3.connect('obituary_platform.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO obituaries (name, date_of_birth, date_of_death, content, author, slug)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, date_of_birth, date_of_death, content, author, slug))
        conn.commit()
        conn.close()
        
        # Redirect to a thank you page after successful submission
        return redirect(url_for('thank_you'))
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/thank_you')
def thank_you():
    return "<style>body{background-color:black;color:white;} a{color:orange;text-decoration:none;}</style>Thank you for submitting the obituary!"

@app.route('/submit', methods=['GET'])
def submit_form():
    return render_template('obituary_form.html')

@app.route('/view_obituaries', methods=['GET'])
def view_obituaries():
    conn = sqlite3.connect('obituary_platform.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, date_of_birth, date_of_death, content, author, submission_date, slug FROM obituaries')
    obituaries = cursor.fetchall()
    conn.close()
    return render_template('view_obituaries.html', obituaries=obituaries)


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    conn = sqlite3.connect('obituary_platform.db')
    cursor = conn.cursor()
    cursor.execute('SELECT slug FROM obituaries')
    obituaries = cursor.fetchall()
    conn.close()

    sitemap_xml = render_template('sitemap_template.xml', obituaries=obituaries)
    response = app.response_class(sitemap_xml, mimetype='application/xml')
    return response

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
