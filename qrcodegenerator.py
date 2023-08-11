import qrcode

input_data = input("· Enter the URL of the page to generate a QR Code: ")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("code.png")

print("· Your QR Code has been created successfully.")
input()
