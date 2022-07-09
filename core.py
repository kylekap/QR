"""Main function

Returns:
    png: png image of QRCode
"""

from flask import Flask, render_template, request
from Project import qr 

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    """Post/Get response

    Returns:
        image: QR code image
    """
    code = qr.QR()
    code.create_QR(txt=request.args.get("data"))
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5001)
