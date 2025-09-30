from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Contact Page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # Abhi simple print kar rahe, real me DB/email use kar sakte
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return "Form Submitted Successfully!"
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
