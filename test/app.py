from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy credentials
USER_CREDENTIALS = {"username": "codeverse", "password": "123456"}

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            session['user'] = username
            return redirect(url_for("assessment"))
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html", error=None)

@app.route("/assessment")
def assessment():
    if 'user' not in session:
        return redirect(url_for("login"))
    return render_template("assessment.html")  # your existing HTML file

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

