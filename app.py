from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My First Flask Website</h1>
    <p>Deployed from GitHub!</p>
    """

if __name__ == "__main__":
    app.run(debug=True)

