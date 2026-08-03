import qrcode

data = input('Enter the Text or URL: ').strip()
filename = input('Enter the File Name: ').strip()

# Ensure filename ends with .png
if not filename.lower().endswith('.png'):
    filename += '.png'

try:
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color='black', back_color='white')
    image.save(filename)
    print(f'QR Code saved as {filename}')
    
    # Optional: show QR code image
    image.show()
except Exception as e:
    print("Error generating QR code:", e)
