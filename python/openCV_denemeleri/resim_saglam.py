from PIL import Image

try:
    img = Image.open("cv_denemesi.png")
    img.show()
except Exception as e:
    print(f"Dosya kontrol edilemedi: {e}")
