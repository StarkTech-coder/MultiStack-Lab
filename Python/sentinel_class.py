# OOP Nedir?
# Şu ana kadar yazdığımız kodlar "yapılacaklar listesi" gibiydi (Önce bunu yap, sonra şunu böl...).
# OOP ise bir "Fabrika Kalıbı" çıkarmaktır.
# Class (Sınıf): Bir şeyin projesidir, blueprint'idir. (Örn: "Mark 42 Zırhı Projesi").
# Object (Nesne): O projeden üretilmiş gerçek kanlı canlı zırhtır. (Örn: Tony'nin giydiği o spesifik zırh).


class Sentinel:
    # 1. Özellikler (Attributes): Zırhın nesi var?
    def __init__(self, name, power_source):
        self.name = name
        self.power_source = power_source
        self.is_online = False
        print(f"--- {self.name} Projesi Oluşturuldu ---")

    # 2. Yetenekler (Methods): Zırh ne yapabilir?
    def boot_up(self):
        self.is_online = True
        print(f"{self.name} sistemleri {self.power_source} ile başlatıldı. Sir.")

    def attack(self):
        if self.is_online:
            print(f"{self.name} lazerleri ateşliyor! 🔥")
        else:
            print("HATA: Sistem çevrimdışı. Önce boot_up yapın.")


# --- NESNE ÜRETME (Object Creation) ---
# Projeden gerçek bir zırh üretiyoruz
my_jarvis = Sentinel("Jarvis-V1", "Arc Reactor")

# Yetenekleri kullanıyoruz
my_jarvis.boot_up()
my_jarvis.attack()


# TEST: Başka bir zırh daha üretelim


class Weapon:
    def __init__(self, type, ammo):
        # BURADA: Dışarıdan gelen 'type' ve 'ammo' değerlerini
        # robotun hafıza kartına (self) kaydetmen lazım.
        self.type = type
        self.ammo = ammo

    def fire(self):
        # BURADA: Eğer mermi (self.ammo) 0'dan büyükse 1 azalt.
        # Değilse "Mermi bitti" yazdır.
        if self.ammo > 0:
            self.ammo -= 1
            print(f"{self.type} ateşlendi! Kalan mermi: {self.ammo}")
        else:
            print(f"HATA: {self.type} mermisi bitti! Şarjör yenileyin.")


# TEST ET
lazer = Weapon("Lazer", 3)
lazer.fire()
lazer.fire()
lazer.fire()
lazer.fire()  # Burada "Mermi bitti" demeli!


# OPSİYONEL PARAMETRELER (Optional Parameters)
class SentinelArmor:
    # 'name' ve 'power' ZORUNLU (Required)
    # 'color' ve 'is_stealth' OPSİYONEL (Default/Optional)
    def __init__(self, name, power, color="Steel Gray", is_stealth=False):
        self.name = name
        self.power = power
        self.color = color
        self.is_stealth = is_stealth

        print(f"--- {self.name} Zırhı Hazır ---")

    def show_specs(self):
        status = "Gizli Mod Aktif" if self.is_stealth else "Normal Mod"
        print(
            f"Zırh: {self.name} | Güç: {self.power} | Renk: {self.color} | Durum: {status}"
        )


# --- KULLANIM SENARYOLARI ---

# 1. Sadece zorunlu olanları veriyoruz:
mark1 = SentinelArmor("Mark-1", 100)
mark1.show_specs()
# Çıktı: Renk 'Steel Gray' olur, Stealth 'False' olur. (Sen vermediğin için varsayılanı kullandı)

# 2. Hepsini kendi istediğimiz gibi veriyoruz:
stealth_suit = SentinelArmor("Ghost", 85, "Midnight Blue", True)
stealth_suit.show_specs()
# Çıktı: Senin verdiğin değerler (Midnight Blue ve True) geçerli olur.
