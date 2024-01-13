from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuration de la base de données
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="tp_cicd"
)

# Endpoint pour ajouter un utilisateur
@app.route('/adduser', methods=['POST'])
def add_user():
    login = request.json['login']
    pwd = request.json['pwd']
    nom = request.json['nom']
    prenom = request.json['prenom']

    cursor = db.cursor()
    query = "INSERT INTO user (login, pwd, nom, prenom) VALUES (%s, %s, %s, %s)"
    values = (login, pwd, nom, prenom)
    cursor.execute(query, values)
    db.commit()

    return jsonify(message="Utilisateur ajouté avec succès")

# Endpoint pour vérifier login/pwd et renvoyer (nom, prenom) si l'utilisateur existe
@app.route('/checkuser', methods=['POST'])
def check_user():
    login = request.json['login']
    pwd = request.json['pwd']

    cursor = db.cursor()
    query = "SELECT nom, prenom FROM user WHERE login = %s AND pwd = %s"
    values = (login, pwd)
    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        return jsonify(nom=result[0], prenom=result[1])
    else:
        return jsonify(message="Utilisateur non trouvé")

if __name__ == '__main__':
    app.run()