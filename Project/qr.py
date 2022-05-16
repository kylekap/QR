import requests
import qrcode
import qrcode.image.styles.moduledrawers as md
import qrcode.image.styledpil as spil

from PIL import Image


class QR:
    def __init__(self):
        try:
            self.brand_img = Image.open("static/Logo.jpg")
        except Exception as E:
            self.brand_img = ""
            print(type(E).__name__,__file__, E.__traceback__.tb_lineno)

    def create_QR(self,
        txt="",
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        version=None,
        box_size=5,
        border=2,
        fill_color="black",
        back_color="white",
        image_factory=spil.StyledPilImage,
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
            fit (bool, optional): Make fit to specific size. Defaults to True.
        """
        
        try:
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
                module_drawer=md.CircleModuleDrawer(),
                image_factory=image_factory)
            self.img = img

            wsize = int(0.25 * self.img.size[0])
            hsize = int(0.25 * self.img.size[1])
            if (type(self.brand_img) != type("")):
                self.brand_img = self.brand_img.resize((wsize,hsize), Image.ANTIALIAS)

                pos = (
                    (self.img.size[0] - self.brand_img.size[0]) // 2,
                    (self.img.size[1] - self.brand_img.size[1]) // 2,
                )
                self.img.paste(self.brand_img, pos)

            self.img.save("static/Display.png")

        except Exception as E:
            print(type(E).__name__,__file__, E.__traceback__.tb_lineno)