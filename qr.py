import qrcode

# Get input from user
data = input("Enter URL or text: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Generate image
img = qr.make_image(
    fill_color="black",
    back_color="white"
)

# Save image
img.save("my_qr.png")

print("QR Code generated successfully!")
