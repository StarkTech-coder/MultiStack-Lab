# ==========================================
# Day 5: Error Handling (Hata Yönetimi)
# ==========================================

# Jarvis'in hata yönetimi yeteneklerini geliştirelim!

def process_energy(input_value):
    try:
        # Gelen veriyi sayıya çevirmeyi dene
        # Try to convert input to integer
        energy = int(input_value)
        print(f"Energy processed: {energy} units.")

    except ValueError:
        # Eğer sayıya çevrilemezse (harf girildiyse) burası çalışır
        # Runs if a ValueError occurs (e.g., entering letters instead of numbers)
        print("ERROR: Invalid input! Please enter a numeric value, Sir.")

    except Exception as e:
        # Diğer tüm bilinmeyen hatalar için genel bir koruma
        # General protection for all other unknown errors
        print(f"ANOMALY DETECTED: {e}")


# Test Edelim:
process_energy("100")  # Çalışır
process_energy("yüz")  # Çökmez, uyarı verir!

# Example: Shield Power Distribution (Örnek: Kalkan Gücü Dağılımı)

def shield_status():
    try:
        total_power = input("Toplam Güç: ")
        shield_count = input("Kalkan Sayısı: ")

        # Girdileri sayıya çeviriyoruz
        result = int(total_power) / int(shield_count)
        print(f"Her kalkan başına düşen güç: {result}")

    except ZeroDivisionError:
        print("KRİTİK HATA: Kalkan sayısı 0 olamaz, sistem çöker!")
    except ValueError:
        print("HATA: Lütfen sadece sayısal değerler giriniz, Sir.")
    except Exception as e:
        print(f"BEKLENMEDİK ANOMALİ: {e}")
    finally:
        print("Kalkan kontrol protokolü sonlandırıldı.")


shield_status()

# Example: Setting Energy Levels (Örnek: Enerji Seviyelerini Ayarlama)

def set_energy(value):
    if value < 0:
        raise ValueError("Sir, enerji seviyesi negatif olamaz!")  # Hatayı biz uydurduk!
    print(f"Enerji ayarlandı: {value}")


# Test Edelim:

def save_energy_report(value):
    try:
        # 1. Adım: Sadece hata riski olan işlem (Dönüştürme)
        energy = int(value)

    except ValueError:
        # Hata varsa burası çalışır
        print("HATA: Kayıt başarısız! Geçersiz enerji formatı.")

    else:
        # 2. Adım: Hata YOKSA burası çalışır
        # Eğer int(value) başarılı olduysa, raporu kaydedebiliriz
        print(f"BAŞARILI: {energy} birim enerji sisteme kaydedildi.")
        # Burada başka işlemler de yapabilirsin, örneğin dosyaya yazmak gibi.

    finally:
        # Her durumda sistem logu tutulur
        print("Enerji kayıt protokolü tamamlandı.")


# Test 1: Başarılı durum
save_energy_report("450")
# Çıktı: BAŞARILI... ve Enerji kayıt protokolü...

# Test 2: Hatalı durum
save_energy_report("çok_yüksek")
# Çıktı: HATA... ve Enerji kayıt protokolü...
