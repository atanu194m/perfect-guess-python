# pip install qrcode[pil]

import qrcode
qr= qrcode.make("add url")
qr.save("My_qrcode.png")
print("qrcode generated successfully.")
