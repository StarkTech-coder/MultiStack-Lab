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
