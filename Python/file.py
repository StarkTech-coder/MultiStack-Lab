import json  # Import JSON library for structured data / Yapılandırılmış veriler için JSON kütüphanesini içe aktar

# 1. JSON STORAGE (MEMORY) / JSON DEPOLAMA (BELLEK)
# -----------------------------------------------

# Create a dictionary for Sentinel's memory / Sentinel'in belleği için bir sözlük oluştur
data = {"total_humans": 42, "status": "SENTINEL ACTIVE", "last_scan": "2026-05-11"}

# SAVE DATA: Writing dictionary to memory.json / VERİYİ KAYDET: Sözlüğü memory.json dosyasına yazma
# 'w' mode means Write (overwrites everything) / 'w' modu Yazma demektir (her şeyin üzerine yazar)
with open("memory.json", "w") as f:
    json.dump(
        data, f, indent=4
    )  # indent=4 makes the JSON file readable / indent=4 JSON dosyasını okunabilir yapar

# READ DATA: Reading memory.json back into a dictionary / VERİYİ OKU: memory.json'ı tekrar sözlüğe çevirme
# 'r' mode means Read / 'r' modu Okuma demektir
with open("memory.json", "r") as f:
    memory = json.load(f)
    print(f"Total humans found: {memory['total_humans']}")  # Çıktı: 42

# 2. TXT LOGGING (HISTORY) / TXT KAYIT SİSTEMİ (GEÇMİŞ)
# -----------------------------------------------

# APPEND LOG: Adding a new line without deleting old data / LOG EKLE: Eski veriyi silmeden yeni satır ekleme
# 'a' mode means Append (adds to the end) / 'a' modu Ekleme demektir (sona ekler)
with open("sentinel_logs.txt", "a") as log_file:
    log_file.write("Detection: 1 Human - Time: 12:45 - Status: SECURE\n")
