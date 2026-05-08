# ==========================================
# Day 2: Lists & Data Management
# (Gün 2: Listeler ve Veri Yönetimi)
# Target: Memory structures for JARVIS
# ==========================================

# 1. Creating a List (Liste Oluşturma)
# Jarvis's active tasks (Jarvis'in aktif görevleri)
tasks = ["Security Check", "Battery Analysis", "Update OS"]

# 2. Accessing Items (Elemanlara Erişme)
# IMPORTANT: Python starts counting from 0!
# ÖNEMLİ: Python saymaya 0'dan başlar!
# [0]: First, [1]: Second, [2]: Third
print(f"[EN] First task: {tasks[0]} | [TR] İlk görev: {tasks[0]}")
print(
    f"[EN] Last task: {tasks[-1]} | [TR] Son görev: {tasks[-1]}"
)  # -1 gives the last item


# 3. Adding Items (Veri Ekleme)
# .append() -> Adds to the end (Sona ekler)
tasks.append("Voice Recognition")

# .insert() -> Adds to a specific position (Belirli bir sıraya ekler)
tasks.insert(1, "Scan Network")  # Adds to 2nd place (2. sıraya ekler)

# 4. Removing Items (Veri Silme)
# .remove() -> Removes by name (İsme göre siler)
tasks.remove("Battery Analysis")

# .pop() -> Removes by index (Sıraya göre siler)
deleted_task = tasks.pop(0)  # Removes the 1st task

print(f"Current Tasks (Güncel Görevler): {tasks}")
print(f"Deleted Task (Silinen): {deleted_task}")


# 5. List Analytics (Liste Analizi)
task_count = len(tasks)
is_update_in_list = "Update OS" in tasks  # Returns True or False

print(f"[EN] Task count: {task_count} | [TR] Görev sayısı: {task_count}")
print(f"Is 'Update OS' active?: {is_update_in_list}")

# EXAMPLE: User Access Check (ÖRNEK: Kullanıcı Erişim Kontrolü)

authorized_users = ["Tony", "Pepper", "Bruce", "Natasha"]

input_name = input("Enter your name (Adınızı girin): ")

input_name_clean = input_name.strip()

if input_name_clean in authorized_users:
    print(f"[EN] Access Granted, {input_name_clean}! | [TR] Erişim izni verildi, {input_name_clean}!")
else:
    print(f"[EN] Access Denied, {input_name_clean}! | [TR] Erişim reddedildi, {input_name_clean}!")


visitor_log = []  # Empty list to store visitor names

visitor_log.append(input_name_clean)  # Adding the visitor's name to the log

visitor_log.sort()  # Sort the log alphabetically (Alfabetik sıraya göre düzenle)

print(f"Visitor Log (Ziyaretçi Kaydı): {visitor_log}")


# ==========================================
# Day 2 - Part 2: List Slicing (PRO)
# (Gün 2 - Bölüm 2: Liste Dilimleme)
# ==========================================

# Örnek Bir Veri Seti (Jarvis'in Log Arşivi)
log_archive = ["User1", "User2", "User3", "User4", "User5", "User6"]

# 1. Belirli Bir Aralığı Almak (Range)
# [1:4] -> 1. indeksten başla, 4. indekse kadar git (4 dahil değil!)
# Sonuç: User2, User3, User4
subset = log_archive[1:4]
print(f"[EN] Middle subset: {subset} | [TR] Orta grup: {subset}")

# 2. Baştan Belirli Bir Yere Kadar (From Start)
# [:3] -> En baştan başla, 3. indekse kadar
first_three = log_archive[:3]
print(f"[EN] First 3: {first_three}")

# 3. Belirli Bir Yerden Sona Kadar (To End)
# [2:] -> 2. indeksten başla, sona kadar git
from_third = log_archive[2:]
print(f"[EN] From 3rd to end: {from_third}")

# 4. Negatif Indeksleme (Sondan Sayma - EN KRİTİK YER!)
# [-3:] -> Sondan 3 elemanı getir (Jarvis'in son aktivitelerini görmek için)
last_three = log_archive[-3:]
print(f"[EN] Last 3 activities: {last_three}")

# 5. Adım Atlayarak Gitme (Stepping)
# [::2] -> Baştan sona 2'şer atlayarak git
every_other = log_archive[::2]
print(f"[EN] Every second user: {every_other}")

#Example: Sensor List Management (Örnek: Sensör Listesi Yönetimi)

all_sensors = ["Cam1", "Cam2", "Mic1", "Mic2", "Temp1", "Temp2"] # Jarvis'in tüm sensörleri

special_cams = all_sensors[:2] 

print(f"Special Cameras (Özel Kamera): {special_cams}")

special_sensors = all_sensors[-2:]

print(f"Special Sensors (Özel Sensörler): {special_sensors}")

reversed_list = all_sensors[::-1]

print(f"Reversed Sensor List (Ters Sensör Listesi): {reversed_list}")


