from flask import Flask , render_template , url_for , redirect , jsonify

app=Flask(__name__)

JOBS=[
 {
     'id':'1',
     'name':'jhony',
 },
 {
     'id':'2',
     'name':'lito'
 },


]
@app.route("/home")
def home():
    return render_template("base.html" , content="zeb",jobs=JOBS)

@app.route("/admin")
def admin():
    return redirect(url_for("user" ,name="adminoo"))


@app.route("/<name>")
def user(name):
    return f" hello {name}"

@app.route("/api/jsonn")
def jsonn():
    return jsonify(JOBS)
app.run(host="localhost",port=8000,debug=True)