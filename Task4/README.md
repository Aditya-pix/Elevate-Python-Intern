# Flask User Management REST API

## 📌 Project Overview
This is a simple REST API built with **Flask** that manages user data.  
It supports basic CRUD operations:  
- **GET** → Fetch all users  
- **POST** → Add a new user  
- **PUT** → Update an existing user  
- **DELETE** → Remove a user  

This project demonstrates fundamental API development skills using Python and Flask.

---

## ⚙️ Requirements
- Python 3.9+  
- Flask  
- Requests (optional, for testing)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run
1. Clone this repository or copy the files.  
2. Run the Flask app:

```bash
python app.py
```

3. By default, the API runs at:  
   **http://127.0.0.1:5000/**

---

## 📡 API Endpoints

### 1. Get all users
```http
GET /users
```

### 2. Add a new user
```http
POST /users
Content-Type: application/json
{
  "name": "Alice",
  "age": 25
}
```

### 3. Update a user
```http
PUT /users/1
Content-Type: application/json
{
  "name": "Alice Updated",
  "age": 26
}
```

### 4. Delete a user
```http
DELETE /users/1
```

---

## 🧪 Testing the API
You can test the endpoints using:  
- **Postman** (recommended for beginners)  
- **curl** (command line)  
- Python’s **requests** library  

Example with Python `requests`:
```python
import requests

res = requests.get("http://127.0.0.1:5000/users")
print(res.json())
```

---

## 🎯 Outcome
✅ Learn how REST APIs work  
✅ Practice Flask routing  
✅ Understand CRUD operations  
