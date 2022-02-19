"""Main function

Returns:
    png: png image of QRCode
"""

from flask import Flask, render_template, request
from Project import qr  # pylint: disable=import-error

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    """_summary_

    Returns:
        _type_: _description_
    """
    data = request.args.get("data")
    qr.qr_opt_logo(data)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5001)
