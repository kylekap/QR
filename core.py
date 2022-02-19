from flask import Flask, render_template, request
import os
import Project.qr as qr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    data = request.args.get("data")
    qr.qr_opt_logo(data)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5001)
