from app import app
from flask import redirect, render_template, request, session
import users
import sheets

@app.route("/")
def index():
    user_id = users.user_id()
    if user_id == 0:
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        
@app.route("/new_sheet_collection", methods=["GET", "POST"])
def new_sheet_collection():
    if request.method == "GET":
        return render_template("new_sheet_collection.html")
    if request.method == "POST":
        collection_name = request.form["collection_name"]
        collection_type = request.form["collection_type"]
        if sheets.new_collection(collection_name, collection_type):
            return redirect("/")
        else:
            return render_template("error.html", message="Uuden kokoelman luonti ei onnistunut")
        
@app.route("/sheet_collections", methods=["GET"])
def get_sheet_collections():
    collections = sheets.get_collections()
    return render_template("sheet_collections.html", collections=collections)

@app.route("/sheet_collections/<int:id>", methods=["GET"])
def get_sheet_collection(id):
    collection = sheets.get_collection(id)
    return render_template("sheet_collection.html", collection=collection)