from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/wifi_cafes')
def wifi_cafes():
    conn = sqlite3.connect('cafes.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM cafes WHERE wifi = ? AND power = ?', (True, True))
    cafes = cursor.fetchall()

    conn.close()
    return render_template('wifi_cafe.html', cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)
