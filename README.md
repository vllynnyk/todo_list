# todo_list

[🔗 View on GitHub](https://github.com/vllynnyk/todo_list)


**Todo List** is a Django-based web application for managing tasks.

---

## ✨ Features

- ✅ Full CRUD functionality for Tasks and Tags
- 📂 Categorize tasks by tags
- 🎨 Clean and responsive UI using **Bootstrap 4.5**
- 📋 Enhanced forms powered by **django-crispy-forms** and `crispy-bootstrap4`

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/vllynnyk/todo_list
cd todo_list
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
# Or install manually:
pip install django crispy-forms crispy-bootstrap4
```
1. **Apply database migrations**
```bash
python manage.py migrate
```
1. **Run the development server**
```bash
python manage.py runserver
```
---

## 🧱 Tech Stack

- **Python** 3.10+
- **Django** 4.x
- **Bootstrap** 4.5
- **django-crispy-forms**
- **crispy-bootstrap4**

---

## 🧪 Testing

To run tests locally, execute:

```bash
python manage.py test
```

---

## 🤝 Contributing

Contributions are welcome!

To contribute to this project:

1. **Fork** the repository
2. **Create a new branch**
```bash
git checkout -b feature/your-feature
```
3. **Make your changes**
4. **Commit and push**
```bash
git push origin feature/your-feature
```
5. **Open a Pull Request and describe your changes**
