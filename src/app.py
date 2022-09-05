import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    super_secret = os.getenv('INPUT_SECRET_VALUE')
    return f"<p>Hello, World! {super_secret}</p>"
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
