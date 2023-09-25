from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("html.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        print(username)
      
    return render_template("html.html", username = username)

if __name__ == "__main__":
    app.run(debug=True)
