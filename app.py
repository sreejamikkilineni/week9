from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Show the registration form
    return render_template('myForm.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['username']
    email = request.form['email']
    # Pass data to greeting.html
    return render_template('greeting.html', name=name, mail=email)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
