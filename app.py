from flask import Flask, request, jsonify
import os
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('persons.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route("/api", methods=["GET", "POST"])
def persons():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM person")
        persons = [
            {"user_id": row[0], "name": row[1], "gender": row[2]}
            for row in cursor.fetchall()
        ]

        if persons is not None:
            return jsonify(persons)

    if request.method == "POST":
        new_name = request.form["name"]
        new_gender = request.form["gender"]
        sql = """INSERT INTO person (name, person) VALUES (?, ?)"""  # Corrected column name

        cursor.execute(sql, (new_name, new_gender))
        conn.commit()
        return f"user with the id: {cursor.lastrowid} created successfully", 201

@app.route('/api/<int:user_id>', methods=["GET", "PUT", "DELETE"])
def single_person(user_id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM person WHERE user_id=?", (user_id,))
        row = cursor.fetchone()

        if row is not None:
            person = {"user_id": row[0], "name": row[1], "gender": row[2]}
            return jsonify(person), 200
        else:
            return "Person not found", 404

    if request.method == "PUT":
        sql = """UPDATE person 
                    SET name=?, 
                    person=?  -- Corrected column name
                    WHERE user_id=? """

        name = request.form["name"]
        gender = request.form["gender"]

        updated_person = {
            "user_id": user_id,
            "name": name,
            "gender": gender
        }

        cursor.execute(sql, (name, gender, user_id))
        conn.commit()
        return jsonify(updated_person), 200

    if request.method == "DELETE":
        sql = """DELETE FROM person WHERE user_id=? """
        cursor.execute(sql, (user_id,))
        conn.commit()
        return f"The user with id: {user_id} has been deleted", 200

if __name__ == "__main__":
    conn = sqlite3.connect('persons.sqlite')
    cursor = conn.cursor()
    sql_query = """CREATE TABLE IF NOT EXISTS person(
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        person TEXT NOT NULL
    )"""
    cursor.execute(sql_query)
    app.run(debug=False, host = '0.0.0.0')
