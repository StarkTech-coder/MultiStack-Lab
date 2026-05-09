# ==========================================
# Day 3: Control Flow & Loops (PRO START)
# (Gün 3: Kontrol Akışı ve Döngüler)
# ==========================================

# 1. While Loop (Jarvis'i Sürekli Açık Tutma)
is_running = True

print("--- JARVIS SYSTEM ONLINE ---")

# Bu döngü, is_running True olduğu sürece sonsuza kadar döner
while is_running:
    command = input("Awaiting Command (Komut Bekleniyor): ").strip().lower()

    if command == "exit" or command == "kapat":
        print("System shutting down. Goodbye, Sir.")
        is_running = False  # Döngüyü kırar ve programı bitirir

    elif command == "status" or command == "durum":
        print("System: Online | Battery: 98% | All sensors active.")

    elif command == "list tasks" or command == "görevleri listele":
        # Day 2'de öğrendiğimiz listeyi burada kullanalım
        tasks = ["Security Check", "Analyze Logs"]
        print(f"Active Tasks: {tasks}")

    else:
        print(f"Unknown command: '{command}'. Please try again.")

battery = 100

while battery >= 0:  # 0 olduğunda da içeri girsin ki son durumu görelim
    print(f"Battery level: {battery}%")

    if battery <= 20 or battery == 0:
        print("Warning: Low Battery! (Düşük Pil Uyarısı!)")

    if battery == 0:
        print("System shutting down... (Sistem kapanıyor...)")
        break  # Döngüyü anında kırmak için en kesin yol!

    battery -= 20


# ==========================================
# Day 3 - Part 2: For Loops (List Iteration)
# (Gün 3 - Bölüm 2: For Döngüleri - Liste Tarama)
# ==========================================

# Jarvis'in kontrol etmesi gereken sistemler listesi
systems = ["Network", "Security", "Sensors", "AI Core", "Database"]

print("--- JARVIS SYSTEM SCAN STARTING ---")

# 'system' değişkeni, listenin içindeki her bir elemanı sırayla temsil eder
for system in systems:
    print(f"[SCANNING]: {system} is being checked...")
    # Burada her sistem için ayrı bir işlem yapıldığını hayal et
    print(f"[RESULT]: {system} is ONLINE.")

print("--- ALL SYSTEMS OPERATIONAL ---")

# ------------------------------------------
# range() Fonksiyonu ile Sayısal Döngü
# ------------------------------------------
# Jarvis 5 saniye içinde kendini başlatıyor:
import time  # Zaman işlemleri için

print("System initializing in:")
for i in range(5, 0, -1):  # 5'ten başla, 0'a kadar git, -1'er azalt
    print(f"{i}...")
    time.sleep(1)  # Gerçekçi olması için 1 saniye bekletilebilir
print("JARVIS IS NOW FULLY FUNCTIONAL!")

# EXAMPLE: Inventory Check (ÖRNEK: Envanter Kontrolü)

inventory = ["Mark I", "Mark II", "Mark III", "Mark IV"]

for item in inventory:
    if item == "Mark III":
        print(f"Special Upgrade Found: {item}!")
    else:
        print(f"Standard Item: {item}.")

# Do-While Simülasyonu

# Kullanıcı doğru şifreyi girene kadar en az bir kez sorar
while True:
    secret = input("Security Code: ")
    if secret == "1234":
        break  # Şart sağlandığı an döngüden çıkar

# Nested Loops (İç içe döngüler - Çok boyutlu tarama)
layers = ["Layer 1", "Layer 2"]
sensors = ["Temp", "Pressure"]

for l in layers:
    for s in sensors:
        print(f"Scanning {l} - {s}")  # Her katman için tüm sensörleri tek tek gezer

# List Comprehension
names = ["tony", "pepper", "bruce"]
clean_names = []
for n in names:
    clean_names.append(n.capitalize())

# Aynı işlemi tek satırda yapabiliriz:
clean_names = [n.capitalize() for n in names]
print(clean_names)  # ['Tony', 'Pepper', 'Bruce']

regions = ["North", "South", "East"]
frequencies = ["Low-Range", "High-Range"]

# İç içe döngülerle bölge ve frekans taraması

for r in regions:  # DIŞ DÖNGÜ: Önce bir bölgeyi seçer
    print(f"--- Sector {r} Scanning ---")
    for (
        f
    ) in frequencies:  # İÇ DÖNGÜ: Seçilen bölge içindeki tüm frekansları tek tek gezer
        print(f"Checking {f} in {r}...")

# List Comprehension ile aynı işlemi yapalım:
raw_sensors = ["cam_01", "mic_02", "temp_03"]

new_list_raw_sensors = [n.capitalize() for n in raw_sensors]

# İç içe döngülerle çok boyutlu tarama
sectors = [1, 2]
checks = ["HardDrive", "Memory"]

for s in sectors:
    print(f"Scanning Sector {s}...")
    for c in checks:
        print(f"Checking {c} in Sector {s}...")


# 3 Katmanlı bir bina, her katmanda 4 sensörün durumu
security_grid = [
    [1, 1, 0, 1],  # Kat 1
    [1, 0, 1, 1],  # Kat 2
    [1, 1, 1, 1],  # Kat 3
]  # Ensure this list of lists is properly defined and not empty


# İç İçe Döngü: security_grid içindeki her katı ve o kattaki her sensörü tek tek gez
for floor_index, floor in enumerate(security_grid):
    for sensor_index, sensor in enumerate(floor):
        if sensor == 0:
            print(f"HATA: Kat {floor_index + 1}, Sensör {sensor_index + 1} çalışmıyor!")

# Tek Satır (Pro): Sadece 3. katın (indeks 2) verilerini alıp, hepsini string'e çevir
third_floor_sensors = [str(sensor) for sensor in security_grid[2]]
print(third_floor_sensors)


