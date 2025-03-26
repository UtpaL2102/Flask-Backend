# Flask API 

Welcome to the **Flask API Repository**, This contains My Flask Journey from **beginner stage** in Flask development. This repository covers everything from **basic Flask routing** to **handling API requests (GET & POST)**, using **templates**, and **creating dynamic web applications**.

This repository is a **work in progress**, and I will keep adding more concepts and implementations as I progress in my Flask learning journey. Stay tuned for updates as I explore deeper into Flask development!


---

## 📌 **Table of Contents**
1. [Introduction to Flask](#introduction-to-flask)
2. [Basic Routing](#basic-routing)
3. [Handling GET and POST Requests](#handling-get-and-post-requests)
4. [Creating a Simple API](#creating-a-simple-api)
5. [Using Variable Rules in Routes](#using-variable-rules-in-routes)
6. [Form Handling & Templates](#form-handling--templates)
7. [Testing APIs with Postman](#testing-apis-with-postman)
8. [Comparison: Flask vs Streamlit/Gradio](#comparison-flask-vs-streamlitgradio)
9. [Running the Project Locally](#running-the-project-locally)
10. [Future Improvements](#future-improvements)

---

## **📌 Introduction to Flask**
Flask is a **lightweight and powerful web framework** for Python that allows developers to build **web applications and APIs** quickly. 

- **Why Flask?**
  - Easy to set up ✅
  - Lightweight and minimalistic ✅
  - Supports RESTful APIs ✅
  - Scalable and production-ready ✅

---

## **📌 Basic Routing**
Routing defines how Flask should respond to **different URLs**.

📌 **File:** `app.py`
```python
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to Krish Naik Hindi Channel"

if __name__ == "__main__":
    app.run(debug=True)
```
✅ **Explanation:**
- `@app.route("/")` → This defines a **root URL**.
- `app.run(debug=True)` → Enables **debug mode**, which reloads the server when changes are made.

---

## **📌 Handling GET and POST Requests**
Flask supports **GET & POST methods** for handling different types of requests.

📌 **File:** `Get-Post.py`
```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        average_marks = (maths + science + history) / 3
        return render_template('form.html', score=average_marks)
    return render_template('form.html', score=None)

if __name__ == "__main__":
    app.run(debug=True)
```
✅ **Explanation:**
- `request.form["maths"]` → Fetching **user input from HTML form**.
- `return render_template("form.html", score=average_marks)` → **Passing data** to an HTML template.

📌 **Corresponding Template:** `templates/form.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Calculate Average Marks</title>
</head>
<body>
    <div class="calculate">
        <h1>Calculate average marks</h1>

        <!-- Main Input Form -->
        <form action="{{ url_for('form') }}" method="post">
            <input type="text" name="maths" placeholder="Maths" required="required" />
            <input type="text" name="science" placeholder="Science" required="required" />
            <input type="text" name="history" placeholder="History" required="required" />
            <button type="submit" class="btn btn-primary btn-block btn-large">Calculate Button</button>
        </form>

        <br>
        <!-- Display the calculated average marks -->
        <p>The average marks is {{ score }}</p>
        <br>
    </div>
</body>
</html>
```
✅ **Explanation:**
- `{{ url_for('form') }}` → Dynamically generates the URL for form submission.
- `{{ score }}` → Displays the calculated average marks after submission.

---

## **📌 Creating a Simple API**
Flask can be used to build APIs that return **JSON responses**.

📌 **File:** `API.py`
```python
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    a_val = float(data['a'])
    b_val = float(data['b'])
    return jsonify(result=a_val + b_val)

if __name__ == "__main__":
    app.run(debug=True)
```
✅ **Explanation:**
- `request.get_json()` → Parses **JSON input**.
- `jsonify(result=a_val + b_val)` → Returns **JSON output**.

📌 **Test API with Postman:**
- **POST request to:** `http://127.0.0.1:5000/api`
- **Body (JSON):**
```json
{
    "a": 10,
    "b": 20
}
```
- **Response:** `{ "result": 30.0 }`

---

## **📌 Running the Project Locally**
1️⃣ **Install Dependencies:**
```bash
pip install flask
```
2️⃣ **Run the Flask App:**
```bash
python app.py
```
3️⃣ **Access URLs:**
- API: `http://127.0.0.1:5000/api`
- Web UI: `http://127.0.0.1:5000/form`

---

## **📌 Future Improvements**
✅ Implement **JWT Authentication** for security.  
✅ Integrate **Flask-SQLAlchemy** for database storage.  
✅ Use **Celery** for background tasks.  

---

### **👨‍💻 Author:** Priyadarshi Utpal  
🔗 **GitHub:** [Your GitHub Link]  
📧 **Email:** [Your Email]  

🚀 **Happy Coding!**

