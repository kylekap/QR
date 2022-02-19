"""Generates QR code

Returns:
    png: image of QR code
"""
# pylint: disable=line-too-long
import requests
import qrcode
import qrcode.image.styles.moduledrawers as md
import qrcode.image.styledpil as spil

from PIL import Image


def simple_qr(qr_text):
    """Most basic QR generator, with no logo or resizing.

    Args:
        qr_text (str): Text to make into QR code
    """
    img = qrcode.make(str(qr_text))
    # type(img)
    img.save("Results/img.png")


def adv_qr(qr_text):
    """QR Code generator function. Default settings in place to make consistent barcode

    Args:
        qr_text (str): Text to make into QR code

    Returns:
        qr.make_image: QR code PIL image
    """
    error_correction = qrcode.constants.ERROR_CORRECT_H
    version = None
    box_size = 5
    border = 4
    fill_color = "black"
    back_color = "white"
    image_factory = spil.StyledPilImage
    module_drawer = md.CircleModuleDrawer()
    fit = True

    qr_generated = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr_generated.add_data(qr_text)
    qr_generated.make(fit=fit)
    img = qr_generated.make_image(
        fill_color=fill_color,
        back_color=back_color,
        image_factory=image_factory,
        module_drawer=module_drawer,
    )
    # img.save('Results/img.png')
    return img


def qr_opt_logo(qr_text, logo_location=""):
    """Generates QR code with logo.

    Args:
        qr_text (str): Text to generate QR code
        logo_location (str, optional): location of the logo to add to the QR code Able to use file location or http:// as long as program has access to location. Defaults to "".
    """

    qr_img = adv_qr(qr_text)
    if logo_location != "":
        if logo_location[:4] == "http":
            logo = Image.open(requests.get(logo_location, stream=True).raw)
        else:
            logo = Image.open(logo_location)
        wpercent = 100 / float(logo.size[0])
        hsize = int((float(logo.size[1]) * float(wpercent)))
        logo = logo.resize((100, hsize), Image.ANTIALIAS)
        pos = (
            (qr_img.size[0] - logo.size[0]) // 2,
            (qr_img.size[1] - logo.size[1]) // 2,
        )
        qr_img.paste(logo, pos)

    qr_img.save("static/Logo.png")


if __name__ == "__main__":
    DEFAULT_LOGO = (
        "https://pbs.twimg.com/profile_images/1464389628941811715/36yJVxtJ_400x400.jpg"
    )
    qr_opt_logo("https://kylekap.pythonanywhere.com/", logo_location=DEFAULT_LOGO)

# pylint: enable=line-too-long
