import qrcode
import os

output_folder = "qr_codes_imagenes"
os.makedirs(output_folder, exist_ok=True)

imagenes = [
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.32_28be21f7",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.32_b034cd9b",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.33_2ccef6fc",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.33_8db1cf0d",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.33_ba08e472",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.33_bbbc7a26",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.34_3ac51fa0",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.34_70f13756",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.34_948dec99",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.35_deff953e",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.36_8e0a6668",
    "Imagen_de_WhatsApp_2025-10-15_a_las_20.24.36_f9d6d711",
]

url_base = "https://gongora-g.github.io/Codigos_QR/"

for nombre in imagenes:
    url = f"{url_base}{nombre}.html"
    qr = qrcode.make(url)
    qr.save(os.path.join(output_folder, f"{nombre}.png"))

print("Códigos QR generados correctamente.")
