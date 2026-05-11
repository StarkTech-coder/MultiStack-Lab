import multiprocessing
import zmq
import time


# 1. VISION PROCESS (SENDER / PRODUCER)
def vision_sender():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)  # PUSH: Sadece veri gönderen soket tipi
    socket.bind(
        "tcp://127.0.0.1:5555"
    )  # Localhost üzerinde 5555 portundan yayına başla

    print("Vision Sender started... / Görüntü Gönderici başladı...")
    count = 0
    while True:
        count += 1
        msg = f"Frame_{count}"
        socket.send_string(msg)  # Veriyi fırlat ve unut
        time.sleep(1)  # Simülasyon için 1 saniye bekle


# 2. BRAIN PROCESS (RECEIVER / CONSUMER)
def brain_receiver():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)  # PULL: Gelen veriyi çeken soket tipi
    socket.connect("tcp://127.0.0.1:5555")  # Yayına bağlan

    print("Brain Receiver started... / Beyin Alıcısı başladı...")
    while True:
        message = (
            socket.recv_string()
        )  # Veri gelene kadar burada bekler (Bloklamaz, sadece bu süreç bekler)
        print(f"Brain processed: {message} / Beyin işledi: {message}")


if __name__ == "__main__":
    # Create two separate processes / İki ayrı süreç oluştur
    p1 = multiprocessing.Process(target=vision_sender)
    p2 = multiprocessing.Process(target=brain_receiver)

    # Start them on different CPU cores / Onları farklı CPU çekirdeklerinde başlat
    p1.start()
    p2.start()

    p1.join()
    p2.join()
