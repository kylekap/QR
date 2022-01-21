
import qrcode
import requests
import qrcode.image.styles.moduledrawers as md
import qrcode.image.styledpil as spil

from  PIL import Image

import config

def simple_qr(qr_text):
    """[summary]

    Args:
        qr_text ([type]): [description]
    """    
    img = qrcode.make(qr_text)
    type(img)
    img.save('Results/img.png')

def adv_qr(qr_text,error_correction=qrcode.constants.ERROR_CORRECT_H,version=None,box_size=25,border=2,fill_color='black',back_color='white', image_factory=spil.StyledPilImage,module_drawer=md.CircleModuleDrawer(),fit=True):
    """[summary]

    Args:
        qr_text ([type]): [description]
        error_correction ([type], optional): [description]. Defaults to qrcode.constants.ERROR_CORRECT_H.
        version ([type], optional): [description]. Defaults to None.
        box_size (int, optional): [description]. Defaults to 25.
        border (int, optional): [description]. Defaults to 2.
        fill_color (str, optional): [description]. Defaults to 'black'.
        back_color (str, optional): [description]. Defaults to 'white'.
        image_factory ([type], optional): [description]. Defaults to spil.StyledPilImage.
        module_drawer ([type], optional): [description]. Defaults to md.CircleModuleDrawer().
        fit (bool, optional): [description]. Defaults to True.

    Returns:
        [type]: [description]
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

def qr_opt_logo(qr_text,logo_location=''):
    """[summary]

    Args:
        qr_text ([type]): [description]
        logo_location (str, optional): [description]. Defaults to ''.

    Returns:
        [type]: [description]
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
    
    QRimg.save('Results/Logo.png')    
    return None

def main():
    """main function used to run the program
    """
    str_input = input('Enter text to generate QR code:')
    qr_opt_logo(str_input,logo_location=config.default_logo)


if __name__ == '__main__':
    """[summary]
    """    
    main()
