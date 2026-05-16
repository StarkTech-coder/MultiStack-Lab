import zmq
import time
import json

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5560")

print("[KAMERA] Çok parçalı (Multipart) yayın başladı...")

while True:
    # 1. PARÇA: Topic (Sadece etiket) -> Metin (bytes olmalı)
    topic = "VisionAgent".encode("utf-8")

    # 2. PARÇA: Metadata -> JSON'ı string yapıp bytes'a çeviriyoruz
    metadata_dict = {"timestamp": time.time(), "fps": 30, "detections": ["person"]}
    metadata = json.dumps(metadata_dict).encode("utf-8")

    # 3. PARÇA: Raw Image Data -> Simüle etmek için ham baytlar oluşturuyoruz
    # Gerçek projede burası: cv2.imencode('.jpg', frame)[1].tobytes() olur.
    raw_image_data = b"Burasivideokaresininhammilyonlarcabaytlikverisidir"

    # --- 🚀 KRİTİK AN: ZINCIRLEME GÖNDERİM ---
    # Bütün parçaları sırayla bir listeye koyup tek seferde fırlatıyoruz!
    socket.send_multipart([topic, metadata, raw_image_data])

    print("[KAMERA] 3 parçalı mesaj başarıyla fırlatıldı.")
    time.sleep(2)
