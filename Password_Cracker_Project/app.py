from flask import Flask, request, render_template_string # type: ignore

app = Flask(__name__)

# Insecure hardcoded credentials for demonstration
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<body>
<h2>Login Page</h2>
<form method="post">
  Username:<br>
  <input type="text" name="username"><br>
  Password:<br>
  <input type="password" name="password"><br><br>
  <input type="submit" name="submit" value="Login">
</form>
</body>
</html>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return "<h1>Login Successful!</h1>"
        else:
            return "<h1>Invalid Credentials</h1>"
    return render_template_string(LOGIN_HTML)

if __name__ == '__main__':
    app.run(debug=True)