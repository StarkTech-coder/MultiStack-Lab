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
    time.sleep(1) # Gerçekçi olması için 1 saniye bekletilebilir
print("JARVIS IS NOW FULLY FUNCTIONAL!")

# EXAMPLE: Inventory Check (ÖRNEK: Envanter Kontrolü)

inventory = ["Mark I", "Mark II", "Mark III", "Mark IV"]

for item in inventory:
    if item == "Mark III":
        print(f"Special Upgrade Found: {item}!")
    else:
        print(f"Standard Item: {item}.")
