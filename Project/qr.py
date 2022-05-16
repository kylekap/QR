import requests
import qrcode
import qrcode.image.styles.moduledrawers as md
import qrcode.image.styledpil as spil

from PIL import Image


class QR:
    def __init__(
        logo=(
            "https://pbs.twimg.com/profile_images/1464389628941811715/36yJVxtJ_400x400.jpg"
        ),
    ):
        if logo != (
            "https://pbs.twimg.com/profile_images/1464389628941811715/36yJVxtJ_400x400.jpg"
        ):
            if logo[:4] == "http":
                self.logo_img = Image.open(requests.get(logo_location, stream=True).raw)
            else:
                self.logo_img = Image.open(logo_location)
        wpercent = 100 / float(self.logo_img.size[0])
        hsize = int((float(self.logo_img.size[1]) * float(wpercent)))
        self.logo_img = self.logo_img.resize((100, hsize), Image.ANTIALIAS)

    def create_QR(self,
        txt="",
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        version=None,
        box_size=5,
        border=4,
        fill_color="black",
        back_color="white",
        image_factory=spil.StyledPilImage,
        module_drawer=md.CircleModuleDrawer(),
        fit=True,
    ):
        """Generate QR Code.

        Args:
            error_correction (_type_, optional): Level of error correction. Defaults to qrcode.constants.ERROR_CORRECT_H (30%).
            version (_type_, optional): _description_. Defaults to None.
            box_size (int, optional): Box size on QR codes. Defaults to 5.
            border (int, optional): Border size on QR code. Defaults to 4.
            fill_color (str, optional): Fill-in color for QR codes. Defaults to "black".
            back_color (str, optional): Background color for QR codes. Defaults to "white".
            image_factory (_type_, optional): Type of image factory. Leave alone unless experienced. Defaults to spil.StyledPilImage.
            module_drawer (_type_, optional): Type of module-drawer. Leave alone unless experienced. Defaults to md.CircleModuleDrawer().
            fit (bool, optional): Make fit to specific size. Defaults to True.
        """
        self.QR_TEXT = txt
        qr_generated = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
        )
        qr_generated.add_data(self.QR_TEXT)
        qr_generated.make(fit=fit)
        img = qr_generated.make_image(
            fill_color=fill_color,
            back_color=back_color,
            image_factory=image_factory,
            module_drawer=module_drawer,
        )
        self.img = img

        self.pos = (
            (self.img.size[0] - self.logo_img.size[0]) // 2,
            (self.img.size[1] - self.logo_img.size[1]) // 2,
        )

        self.img.paste(self.logo_img, pos)

        self.img.save("static/Logo.png")
