import qrcode
from PIL import Image

# Define the URL
url = "https://batin-warsaw-website.lovable.app/"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file path
image_path = "/mnt/data/batin_warsaw_qr.png"
img.save(image_path)

image_path
