# ==========================================
# MULTISTACK-LAB: PYTHON JOURNEY
# Day 1: Variables and Basics (Değişkenler ve Temeller)
# Target: Foundations for Project JARVIS (JARVIS Projesi İçin Temeller)
# ==========================================

# 1. Variable Definition (Değişken Tanımlama)
# JARVIS's Identity Credentials (JARVIS'in Kimlik Bilgileri)
bot_name = "Jarvis"  # String: Text data (Metin verisi)
version = 1.0  # Float: Decimal numbers (Ondalıklı sayı)
is_active = True  # Boolean: True/False logic (Mantıksal değer)

# 2. Printing to Console (Ekrana Yazdırma)
# Initial Communication (İlk İletişim)
print(f"System: {bot_name} is starting...")  # Sistem başlatılıyor
print(f"Version: {version}")  # Versiyon bilgisi
print(f"Status: {is_active}")  # Aktiflik durumu

# 3. Getting User Input (Kullanıcıdan Bilgi Alma)
# Interaction with the owner (Sahibi ile etkileşim)
user_name = input("Sir, what is your name? (Efendim, isminiz nedir?): ")
print(f"Glad to meet you {user_name}! How can I assist you today?")
# Tanıştığıma memnun oldum! Bugün size nasıl yardımcı olabilirim?

# [NOTE]: Variables are the foundation of memory.
# [NOTU]: Değişkenler hafızanın temelidir.
# We will manage all commands through these variables in the future.
# İleride tüm komutları bu değişkenler üzerinden yöneteceğiz.


# ==========================================
# Day 1 - Part 2: Advanced Variable Operations
# (Gün 1 - Bölüm 2: İleri Seviye Değişken İşlemleri)
# ==========================================

# 1. Basic Math Operations (Temel Matematiksel İşlemler)
# Let's calculate Jarvis's uptime or battery (Jarvis'in çalışma süresini veya pilini hesaplayalım)
battery_level = 100
battery_usage_per_hour = 1.5
total_uptime_hours = 24

remaining_battery = battery_level - (battery_usage_per_hour * total_uptime_hours)

print(
    f"Bilingual - [EN] Remaining Battery: {remaining_battery}% | [TR] Kalan Pil: {remaining_battery}%"
)

# 2. String Manipulation (Metin Manipülasyonu)
# Jarvis needs to clean up user voice commands (Jarvis'in sesli komutları temizlemesi gerekir)
raw_command = "   OPEN THE CAMERA   "
clean_command = raw_command.strip().lower()  # Strips spaces and makes it lowercase

print(f"Original: '{raw_command}'")
print(f"Cleaned (Temizlenmiş): '{clean_command}'")

# 3. Type Casting (Veri Tipi Dönüşümü)
# Converting input (string) to integer for calculations
# Kullanıcıdan alınan metni hesaplama için sayıya çevirme
user_age_str = "25"  # This comes as text (Bu metin olarak gelir)
user_age_int = int(user_age_str)  # Converting to number (Sayıya çeviriyoruz)
years_to_reach_hundred = 100 - user_age_int

print(f"Sir, you will be 100 in {years_to_reach_hundred} years.")

# 4. Multi-Assignment (Çoklu Atama)
# Assigning values to multiple variables at once
# Aynı anda birden fazla değişkene değer atama
cpu_usage, ram_usage, temperature = 45, 60, 52

print(f"System Monitor -> CPU: {cpu_usage}%, RAM: {ram_usage}%, TEMP: {temperature}°C")


# Example: Temperature Conversion (Örnek: Sıcaklık Dönüşümü)

celsius_temp = input("Enter temperature in Celsius (Sıcaklığı Celsius olarak girin): ")

celsius_temp_float = float(celsius_temp)  # Convert string to float

fahrenheit_temp = (celsius_temp_float * 1.8) + 32

print(f"EN] Temperature: {fahrenheit_temp:.1f} F | [TR] Sıcaklık: {fahrenheit_temp:.1f} F")
