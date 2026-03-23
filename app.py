import sqlite3
from flask import Flask, render_template, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "gym-secret-key-123"
def get_db():
    db = sqlite3.connect("database.db")
    db.row_factory = sqlite3.Row
    return db

@app.route("/")
def index():
    db = get_db()
    query = request.args.get("query", "")
    if query:
        sql = """SELECT E.*, C.name as category 
                 FROM exercises E, categories C 
                 WHERE E.category_id=C.id AND (E.name LIKE ? OR E.description LIKE ?)"""
        exercises = db.execute(sql, ["%"+query+"%", "%"+query+"%"]).fetchall()
    else:
        sql = "SELECT E.*, C.name as category FROM exercises E, categories C WHERE E.category_id=C.id"
        exercises = db.execute(sql).fetchall()  
    return render_template("index.html", exercises=exercises, query=query)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        db = get_db()
        try:
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", [username, password])
            db.commit()
            return redirect("/login")
        except:
            return "Error: Username already taken!"
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username=?", [username]).fetchone()
        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect("/")
        return "Invalid username or password!"
    return render_template("login.html")

@app.route("/new", methods=["GET", "POST"])
def new():
    if "user_id" not in session:
        return redirect("/login")
    db = get_db()
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        category_id = request.form["category_id"]
        db.execute("INSERT INTO exercises (user_id, category_id, name, description) VALUES (?, ?, ?, ?)",
                   [session["user_id"], category_id, name, description])
        db.commit()
        return redirect("/")
    categories = db.execute("SELECT * FROM categories").fetchall()
    return render_template("new.html", categories=categories)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)