from flask import Flask

app = Flask(__name__)

@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    return f"Welcome to {username}'s profile!"

if __name__ == "__main__":
    app.run(debug=True)
