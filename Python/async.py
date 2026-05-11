import asyncio  # Asenkron kütüphanesi / Asynchronous library


# Define an asynchronous function / Asenkron bir fonksiyon tanımla
async def sentinel_report():
    print("Report: Sending data to cloud... / Rapor: Veri buluta gönderiliyor...")
    await asyncio.sleep(
        2
    )  # Wait for 2 seconds without freezing / Donmadan 2 saniye bekle
    print("Report: Data sent successfully! / Rapor: Veri başarıyla gönderildi!")


async def camera_stream():
    print("Camera: Streaming 30 FPS... / Kamera: 30 FPS akış devam ediyor...")


async def main():
    # Run both tasks together / İki görevi aynı anda çalıştır
    await asyncio.gather(sentinel_report(), camera_stream())


# Start the engine / Motoru çalıştır
asyncio.run(main())

# --- ARKA PLAN GÖREVLERİ (BACKGROUND TASKS) ---


# 1. Background Task: Simulation of uploading a photo / Arka Plan Görevi: Fotoğraf yükleme simülasyonu
async def upload_photo(photo_name):
    print(f"Starting upload: {photo_name} / Yükleme başlıyor: {photo_name}")
    await asyncio.sleep(3)  # Heavy internet task / Ağır internet görevi
    print(f"Upload complete: {photo_name} / Yükleme tamamlandı: {photo_name}")


# 2. Main Stream: Tracking movement / Ana Akış: Hareket takibi
async def tracking_loop():
    while True:
        print("Sentinel is tracking... (FPS: 30) / Sentinel takip ediyor...")
        await asyncio.sleep(0.5)  # Non-blocking wait / Donma yapmayan bekleme


async def main():
    print("System started. / Sistem başlatıldı.")

    # CASE: We found a target / DURUM: Bir hedef bulduk
    # We use create_task to run it in the background without waiting
    # create_task kullanarak beklemeksizin arka planda çalıştırıyoruz
    asyncio.create_task(upload_photo("intruder_001.jpg"))

    # Program continues immediately to the tracking loop
    # Program anında takip döngüsüne devam eder
    await tracking_loop()


# Start the engine / Motoru çalıştır
if __name__ == "__main__":
    asyncio.run(main())
