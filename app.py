## Flask App Routing (This imports Flask, which is needed to create the web application.)
from flask import Flask


## Create a simple Flask application
## Flask(__name__) creates an instance of the Flask application.
## The __name__ variable tells Flask that this is the main application file.

app = Flask(__name__)

## @app.route("/") → Defines a route, meaning this function will run when you visit the root URL.
## methods=["GET"] → This specifies that this route only handles GET requests.


@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to Krish Naik Hindi Channel"

if __name__ == "__main__":
    app.run(debug=True)

## app.run(debug=True) Starts the Flask development server.debug=True enables debug mode,which Auto-reloads the server when you make changes.
## and Shows detailed error messages in the browser if the code crashes.
