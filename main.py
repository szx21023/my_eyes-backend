from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # 載入預訓練模型（coco80類別）
results = model("./20201206003287.jpg")  # 輸入圖片即可
results[0].show()  # 顯示偵測結果
