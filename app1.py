from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to Krish Naik Hindi Channel"

@app.route("/index", methods=["GET"])  # ✅ pehle uper wala print hoga line but jab url me /index add kroge toh 
def index():                            # neeche wala bhi aajaega
    return "<h1>Welcome to Index Page<h2>"  # isme hum h1 mtlb HTML ke tags bhi add kar sakte hai

if __name__ == "__main__":
    app.run(debug=True)
