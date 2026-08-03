import qrcode

data = input('Enter the Text or URL: ').strip()
filename = input('Enter the File Name: ').strip()

# Ensure the file has a .png extension
if not filename.lower().endswith('.png'):
    filename += '.png'

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)

print(f'QR Code saved as {filename}')
# Optional: open the QR code image
image.show()
