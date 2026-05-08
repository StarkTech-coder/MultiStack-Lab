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