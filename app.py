from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('searching.html')  # Loads index.html from templates/

if __name__ == '__main__':
    app.run(port=8000, debug=True)
