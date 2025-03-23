from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    return f"Logged in as {username}!"

if __name__ == "__main__":
    app.run(debug=True)
# In this code, we are using the request object to access the form data sent in the POST request.
# The request.form dictionary contains the form data sent in the POST request.