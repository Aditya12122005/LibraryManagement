from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

books = [
    {"id": 1, "name": "Python Programming"},
    {"id": 2, "name": "Data Structures"},
    {"id": 3, "name": "Database Systems"},
]

def search_books(query):
    return [b for b in books if query.lower() in b["name"].lower()]

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Library Login</title></head>
<body>
  <h2>Library Login</h2>
  <form method="post">
    <input type="text" id="username" name="username" placeholder="Username">
    <input type="password" id="password" name="password" placeholder="Password">
    <button type="submit" id="login-btn">Login</button>
  </form>
  {% if error %}<p class="error">{{ error }}</p>{% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("username") == "admin" and request.form.get("password") == "admin123":
            return redirect(url_for("dashboard"))
        error = "Invalid credentials"
    return render_template_string(LOGIN_PAGE, error=error)

@app.route("/dashboard")
def dashboard():
    return "<h1 id='welcome'>Welcome to Library Dashboard</h1>"

@app.route("/search")
def search():
    q = request.args.get("q", "")
    return {"results": search_books(q)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)