from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/quizzes", methods=["GET", "POST"])
def quizzes():
    if request.method == "POST":
        return jsonify({"message": "Quiz submitted"})
    return render_template("quiz.html")


@app.route("/progress")
def progress():
    return render_template("progress.html")


@app.route("/timer")
def timer():
    return render_template("timer.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
