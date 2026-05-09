# 1. Fonksiyon (Function) Nedir?
# Fonksiyon, bir işi yapmak için paketlenmiş kod bloğudur. Bir kez yazarsın, bin kez kullanırsın.

# Temel Kural:

# def: "Define" (Tanımla) kelimesinden gelir. Fonksiyonun başladığını söyler.

# Parametre: Fonksiyonun çalışması için dışarıdan gelen veridir (parantez içindekiler).

# return: Fonksiyonun işini bitirip sana verdiği sonuçtur.

# ==========================================
# Day 4: Functions - Jarvis's Skills
# (Gün 4: Fonksiyonlar - Jarvis'in Yetenekleri)
# ==========================================


# Define a function to calculate remaining energy
# Geriye kalan enerjiyi hesaplamak için bir fonksiyon tanımla
def calculate_energy(battery, consumption):
    """
    Calculates the final battery level after usage.
    Kullanımdan sonraki son pil seviyesini hesaplar.
    """
    remaining = battery - consumption
    return remaining  # Sends the result back (Sonucu geri gönderir)


# --- USING THE FUNCTION (FONKSİYONU KULLANMA) ---

current_battery = 100
shield_usage = 25

# Call the function and store the result
# Fonksiyonu çağır ve sonucu kaydet
final_status = calculate_energy(current_battery, shield_usage)

print(f"Jarvis Report: After shield usage, battery is at %{final_status}")
# (Jarvis Raporu: Kalkan kullanımından sonra pil: %75)

# Example: Energy Consumption Simulation (Örnek: Enerji Tüketimi Simülasyonu)
usage_list = [5, 15, 20, 10]

for usage in usage_list:
    current_power = calculate_energy(current_power, usage)

    # Check if battery is critical
    # Pil kritik seviyedeyse uyarı ver
    if current_power < 0:
        print("CRITICAL: Energy depleted! (KRİTİK: Enerji tükendi!)")
        current_power = 0  # Pil negatif görünmesin diye sabitledik
        break  # Enerji bittiyse daha fazla harcama yapma, döngüden çık

    print(f"After using {usage} units, remaining power: %{current_power}")

# (Kullanılan {usage} biriminden sonra kalan güç: %{current_power})

def scan_area(sector, energy_cost=5):  # energy_cost yazılmazsa hep 5 olur
    print(f"{sector} taranıyor. Harcanan: {energy_cost}")


scan_area("Mutfak")  # 5 harcar
scan_area("Garaj", 20)  # 20 harcar

# Example: Repairing Parts (Örnek: Parçaları Tamir Etme)

def repair_parts(*parts):  # Yıldız işareti 'ne gelirse paketle' demek
    for part in parts:
        print(f"{part} tamir edildi.")


repair_parts("Helmet", "Glove", "Boots")  # İstediğin kadar yazabilirsin!

# Example: Nested Functions (Örnek: İç İçe Fonksiyonlar)

def prepare_suit():
    # İç fonksiyon (Yardımcı)
    def calibrate_sensors():
        return "Sensors OK"

    status = calibrate_sensors()
    print(f"Zırh Hazırlanıyor... Durum: {status}")


prepare_suit()
# calibrate_sensors() -> Bunu dışarıda çağıramazsın, hata verir! (Güvenli)

# Lambda Functions (Anonim Fonksiyonlar - Kısa ve Tek Seferlik İşler İçin)

# Klasik yöntem:
def square(x):
    return x * x


# Lambda yöntemi:
power_up = lambda x: x * x

print(power_up(5))  # Çıktı: 25

# Example: System Report with Keyword Arguments (Örnek: Anahtar Kelime Argümanları ile Sistem Raporu)

def system_report(status, **details):
    print(f"Main Status: {status}")

    # details bir sözlük (dictionary) gibi davranır
    for key, value in details.items():
        print(f"--- {key.capitalize()}: {value}")


# Kullanımı:
system_report("Active", battery=85, oxygen="Optimal", speed="Mach 2")

# (Ana Durum: Aktif | --- Battery: 85 | --- Oxygen: Optimal | --- Speed: Mach 2)


# Scope (Kapsam) - Global vs Local Variables (Global vs Lokal Değişkenler)

hero = "Tony"  # GLOBAL (Herkes tanır)


def change_hero():
    hero = "Steve"  # LOKAL (Sadece bu fonksiyonun içinde geçerli)
    print("Inside:", hero)


change_hero()  # Çıktı: Inside: Steve
print("Outside:", hero)  # Çıktı: Outside: Tony (Dışarıdaki değişmedi!)
