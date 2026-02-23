# pip install qrcode[pil]

import qrcode
url = input ("enter the url:").strip()
file_path =  "C:\\Users\\LENOVO\\OneDrive\\Pictures\\qrcode.png"

qr = qrcode. QRCode()
qr.add_data(url)

img = qr.make_image()
image.save(file_path)
