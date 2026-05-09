# Modülü içe aktarıyoruz 
import energy_system


print("--- Jarvis Başlatılıyor ---")

# Diğer dosyadaki fonksiyonu çağırıyoruz
status = energy_system.check_battery()
print(status)

power = energy_system.calculate_jump_power(100)
print(f"Jump Power needed: {power}")
