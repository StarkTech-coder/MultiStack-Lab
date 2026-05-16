import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5560")

# Sadece "VisionAgent" etiketiyle başlayan trenleri kabul et diyoruz
socket.setsockopt_string(zmq.SUBSCRIBE, "VisionAgent")

print("[J.A.R.V.I.S.] Çok parçalı hat dinleniyor...")

while True:
    # --- 🚀 TREN KAPIYA GELDİ ---
    # recv_multipart() bize otomatik olarak bir LİSTE döndürür
    parcalar = socket.recv_multipart()

    # Vagonları sırasıyla açıyoruz
    vagon_1_topic = parcalar[0].decode("utf-8")
    vagon_2_metadata = json.loads(parcalar[1].decode("utf-8"))
    vagon_3_görüntü = parcalar[2]  # Dikkat: Decode etmiyoruz, çünkü o HAM BAYT!

    print("\n[J.A.R.V.I.S.] ------- YENİ PAKET ALINDI -------")
    print(f"1. Parça (Topic): {vagon_1_topic}")
    print(
        f"2. Parça (Metadata): {vagon_2_metadata} -> Zaman: {vagon_2_metadata['timestamp']}"
    )
    print(f"3. Parça (Ham Veri Boyutu): {len(vagon_3_görüntü)} bayt.")
