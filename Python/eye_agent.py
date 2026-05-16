import zmq
import time

context = zmq.Context() # ZMQ context oluştur

socket = context.socket(zmq.PUSH) # PUSH tipi socket oluştur
socket.bind("tcp://127.0.0.1:5555") # Localhost üzerinde 5555 portundan yayına başla

print("Göz Ajani started... / Göz Ajani başladı...")

while True:
    socket.send_string("Göz Ajani is watching... / Göz Ajani izliyor...") # Veriyi fırlat ve unut
    print("Göz Ajani sent a message... / Göz Ajani bir mesaj gönderdi...")
    time.sleep(2) # Simülasyon için 2 saniye bekle