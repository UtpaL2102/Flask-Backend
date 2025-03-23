from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    a_val = float(data['a'])
    b_val = float(data['b'])
    return jsonify(a_val + b_val)

if __name__ == "__main__":
    app.run(debug=True)
