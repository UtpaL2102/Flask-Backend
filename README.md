# Flask API and Frontend Demo

This repository contains a **Flask-based API** along with implementations for **calculating average marks**, **handling JSON data**, and **demonstrating REST API concepts**. Additionally, it includes **a frontend form**, API endpoints, and examples of how to test the APIs using **Postman**.

---

## **📌 Features Implemented**

### 1️⃣ **Flask Backend for Handling Form Data**
- Users enter marks in **Maths, Science, and History**.
- Flask processes the input and calculates the **average marks**.
- Displays results on an HTML page using `render_template`.

📌 **File:** `app.py`
```python
maths = float(request.form['maths'])
science = float(request.form['science'])
history = float(request.form['history'])

average_marks = (maths + science + history) / 3
return render_template('form.html', score=average_marks)
```

---

### 2️⃣ **Creating a Flask API Endpoint (`/api`)**
- Accepts **JSON input** with numbers `a` and `b`.
- Returns their **sum** as a JSON response.

📌 **File:** `app.py`
```python
@app.route('/api', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    a_val = float(data['a'])
    b_val = float(data['b'])
    return jsonify(a_val + b_val)
```

📌 **Test Using Postman:**
- **Method:** `POST`
- **URL:** `http://127.0.0.1:5000/api`
- **Body (JSON):**
```json
{
    "a": 10,
    "b": 20
}
```
- **Response:** `{ "result": 30.0 }`

---

### 3️⃣ **Testing the API in Postman vs Browser**
- **POST requests** work in **Postman**, but trying to access `127.0.0.1:5000/api` in a browser gives `Method Not Allowed`.
- This happens because browsers make **GET requests** by default, while this API **only accepts POST requests**.

📌 **Solution:** Add support for `GET` if needed:
```python
@app.route('/api', methods=['GET', 'POST'])
```

---

### 4️⃣ **Frontend Form (`form.html`)**
- HTML form to **input marks**.
- Sends data to Flask for processing.

📌 **File:** `templates/form.html`
```html
<form action="/" method="POST">
    <input type="number" name="maths" placeholder="Maths Marks" required>
    <input type="number" name="science" placeholder="Science Marks" required>
    <input type="number" name="history" placeholder="History Marks" required>
    <button type="submit">Submit</button>
</form>
```

---

### 5️⃣ **Why Flask Instead of Streamlit/Gradio?**
| Feature               | Streamlit / Gradio | Flask (or FastAPI) |
|----------------------|-------------------|-------------------|
| **Scalability**      | Limited to small projects | Handles multiple requests efficiently |
| **API Control**      | Limited customization | Full control over API structure |
| **Security**         | Basic | Advanced (JWT, OAuth, authentication) |
| **Database Handling** | Not designed for it | Supports SQL & NoSQL databases |
| **Background Processing** | Limited | Supports Celery for async jobs |

---

## **🚀 Running the Project Locally**

### **🔹 Step 1: Install Dependencies**
```bash
pip install flask
```

### **🔹 Step 2: Run the Flask App**
```bash
python app.py
```

### **🔹 Step 3: Open in Browser**
- Form UI: `http://127.0.0.1:5000/`
- API Endpoint (Test with Postman): `http://127.0.0.1:5000/api`

---

## **📌 Future Improvements**
✅ Add **JWT Authentication** to secure the API.  
✅ Implement **Flask-SQLAlchemy** for database support.  
✅ Use **Celery** for background task processing.  

---

### **👨‍💻 Author:** Utpal
🔗 **GitHub:** [Your GitHub Link]  
📧 **Email:** [Your Email]  

🚀 **Happy Coding!**

