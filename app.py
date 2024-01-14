from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/adduser', methods=['POST'])
def add_user():
    data = request.get_json()
    conn = sqlite3.connect('tp_cicd.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    login = data.get('login')
    pwd = data.get('pwd')
    nom = data.get('nom')
    prenom = data.get('prenom')
    
    if login and pwd and nom and prenom:
        cursor.execute("INSERT INTO user (login, pwd, nom, prenom) VALUES (?, ?, ?, ?)",
                       (login, pwd, nom, prenom))
        conn.commit()
        conn.close()
        return jsonify({"message": "Utilisateur ajouté"}), 201
    else:
        return jsonify({"message": "Missing required fields"}), 400

@app.route('/checkuser', methods=['POST'])
def check_user():
    data = request.get_json()
    conn = sqlite3.connect('tp_cicd.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    login = data.get('login')
    pwd = data.get('pwd')

    if login and pwd:
        user = cursor.execute('SELECT * FROM user WHERE login = ? AND pwd = ?', (login, pwd)).fetchone()

        if user:
            return jsonify({"nom": user['nom'], "prenom": user['prenom']}), 200
        else:
            return jsonify({"message": "Utilisateur introuvable"}), 404
    else:
        return jsonify({"message": "Missing required fields"}), 400

if __name__ == '__main__':
    app.run(debug=True)