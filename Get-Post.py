from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Get values from the form and convert them to float
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        # Calculate average marks
        average_marks = (maths + science + history) / 3

        # Pass the calculated average to the template
        return render_template('form.html', score=average_marks)

    return render_template('form.html', score=None)

if __name__ == "__main__":
    app.run(debug=True)
