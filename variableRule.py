from flask import Flask

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to the Index Page</h2>"

## Variable Rule Example for Pass
@app.route('/success/<int:score>')  
def success(score):
    return "The person has passed and the score is: " + str(score)

## Variable Rule Example for Fail
@app.route('/fail/<int:score>')  # Fixed: Added '/' and renamed function
def fail(score):
    return "The person has failed and the score is: " + str(score)

if __name__ == "__main__":
    app.run(debug=True)
