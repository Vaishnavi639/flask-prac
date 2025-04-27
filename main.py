from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "<h1>This is the About Page!</h1>"

@app.route('/contact')
def contact():
    return "<h1>Contact us at contact@example.com</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
