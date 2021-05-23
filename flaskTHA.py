from flask import Flask, request
import functools

app = Flask(__name__)
strings = []


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/tha", methods=["GET", "POST"])
def tha():
    try:
        if request.method == "POST":
            string = request.args.get('string', '')
            if not string:
                return "enter some string"

            strings.append(string)
            return "string added"
        else:
            return " ".join(strings)
    except:
        return "an error occured"


if __name__ == "__main__":
    app.run(debug=True)
