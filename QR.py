import qrcode

url =input("Enter URL: ").strip()
file_path = "C:\\Users\\LENOVO\\OneDrive\\Pictures\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)
print("QR Code generated successfully!")