from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/bin")
def bin():
    return "just bin lol"


# if __name__ == "__main__":
#     app.run(debug=True, port=3000)
