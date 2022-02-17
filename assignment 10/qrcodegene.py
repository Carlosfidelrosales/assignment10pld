import qrcode
from PIL import Image

sync = qrcode.QRCode(
    
    border = 4,
     
    box_size = 15,

    error_correction= qrcode.constants.ERROR_CORRECT_M,
    
    version = 2
)

"""
QR CODE PATTERN
"""

digiInfo = """TAGUIG CITY COVID-19 CONTACT TRACING FORM

Personal Details
    Name            : Carlos Fidel A. Rosales
    Age             : 22 
    Birthdate       : March 26, 1999
    Sex             : Male
    Address         : #123 London Bridge, Bangbang, Taguig City
    Phone Number    : 0912-333-4356
    E-mail          : carlitofudelito302@gmail.com

Vaccination Status
    COVID-19 Vaccine
        Received Dose/s : 2
        First Dose      : Pfizer ; September 23, 2021
        Second Dose     : Pfizer ; November 24, 2021
    COVID-19 Booster Shot
        Received Shot/s : 0

>> TIME RECORDED: 13:55 <<<
>> DATE RECORDED: FEBRUARY 15, 2022 <<< """

sync.add_data(digiInfo)

sync.make(fit = True) ; frame = sync.make_image(back_color = 'white', fill_color = 'black').convert('RGB')

present_trademark = Image.open('rickasley.jpg')
present_trademark.thumbnail((180, 180))
TMplacement = ((frame.size[0] - present_trademark.size[0]) // 2, (frame.size[1] - present_trademark.size[1]) // 2)
frame.paste(present_trademark, TMplacement)

frame.save('ROSALES QR CODE.png')

