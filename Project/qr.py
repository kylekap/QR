import qrcode
import requests
import qrcode.image.styles.moduledrawers as md
import qrcode.image.styledpil as spil

from  PIL import Image


def simple_qr(qr_text):
    """Most basic QR generator, with no logo or resizing.

    Args:
        qr_text (str): Text to make into QR code
    """    
    img = qrcode.make(str(qr_text))
    #type(img)
    img.save('Results/img.png')

def adv_qr(qr_text,error_correction=qrcode.constants.ERROR_CORRECT_H,version=None,box_size=5,border=4,fill_color='black',back_color='white', image_factory=spil.StyledPilImage,module_drawer=md.CircleModuleDrawer(),fit=True):
    """QR Code generator function. Default settings in place to make consistent barcode

    Args:
        qr_text (str): Text to make into QR code
        error_correction (qrcode.constants, optional): Type of error correction to include with barcode. Defaults to qrcode.constants.ERROR_CORRECT_H, which is 30%.
        version (int, optional): Integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix). Defaults to None.
        box_size (int, optional): How many pixels each “box” of the QR code is. Defaults to 25.
        border (int, optional): How many boxes thick the border should be (the default is 4, which is the minimum according to the specs). Defaults to 4.
        fill_color (str, optional): Color of the dots in the code. Defaults to 'black'.
        back_color (str, optional): Color of the backsplash in the code. Defaults to 'white'.
        image_factory (optional): Image factory to utilize. Defaults to spil.StyledPilImage. Recommended do not change
        module_drawer (optional): shape of the dots in the code. Defaults to md.CircleModuleDrawer(). Recommended do not change
        fit (bool, optional): Fits to the size or not. Defaults to True.

    Returns:
        qr.make_image: [description]
    """    
    qr = qrcode.QRCode(
        version=version,
        error_correction = error_correction,
        box_size=box_size,
        border=border
    )
    qr.add_data(qr_text)
    qr.make(fit=fit)
    img = qr.make_image(fill_color=fill_color, back_color=back_color,image_factory=image_factory, module_drawer=module_drawer)
    #img.save('Results/img.png')
    return img

def qr_opt_logo(qr_text,logo_location='',version=None):
    """Generates QR code with logo.

    Args:
        qr_text (str): Text to generate QR code
        logo_location (str, optional): location of the logo to add to the QR code Able to use file location or http:// as long as program has access to location. Defaults to ''.
    """    
    QRimg = adv_qr(qr_text)
    if logo_location != '':
        if logo_location[:4] == 'http':
            logo = Image.open(requests.get(logo_location,stream=True).raw)
        else:
            logo=Image.open(logo_location)
        wpercent = (100/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((100, hsize), Image.ANTIALIAS)
        pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
    
    QRimg.save('static/Logo.png')


if __name__ == '__main__':
    import config
    qr_opt_logo('https://kylekap.pythonanywhere.com/')
else:
    import Project.config
