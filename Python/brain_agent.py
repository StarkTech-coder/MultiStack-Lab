import zmq

context = zmq.Context() # ZMQ context oluştur

socket = context.socket(zmq.PULL) # PULL tipi socket oluştur
socket.connect("tcp://127.0.0.1:5555") # Yayına bağlan

print("Beyin Ajani pusuda bekliyor...")

while True:
    message = socket.recv_string() # Veri gelene kadar burada bekler (Bloklamaz, sadece bu süreç bekler)
    print(f"Beyin Ajani received: {message} / Beyin Ajani aldı: {message}")