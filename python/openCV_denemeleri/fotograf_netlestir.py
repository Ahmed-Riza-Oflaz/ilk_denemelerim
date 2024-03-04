import cv2

def foto_netlestir(image_path, output_path, scale=2):
    try:
        # Resmi oku
        image = cv2.imread(image_path)
        
        # Resmin başarıyla okunup okunmadığını kontrol et
        if image is None:
            raise FileNotFoundError(f"{image_path} dosyası okunamadı.")
    
        # Boyutları yeniden ayarla
        height, width = image.shape[:2]
        new_width = int(width * scale)
        new_height = int(height * scale)
        
        # Boyutlandırma işlemi
        dim = (new_width, new_height)
        resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        
        # Gaussian bulanıklık uygula (isteğe bağlı)
        blurred_image = cv2.GaussianBlur(resized_image, (0, 0), 3)
        
        # Netleştirme için unsharp mask uygula
        unsharp_image = cv2.addWeighted(resized_image, 1.5, blurred_image, -0.5, 0)
        
        # Sonucu kaydet
        cv2.imwrite(output_path, unsharp_image)
        print(f"{output_path} dosyası başarıyla oluşturuldu.")
    
    except Exception as e:
        print(f"Hata: {e}")

# Kullanım örneği
foto_netlestir( "C://Users/Acer/OneDrive/Masaüstü/Ekran görüntüsü 2024-03-03 030317.png" , "netlestirilmis_resim.jpg", scale=2)
