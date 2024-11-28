# Detectron2 실행 함수 (예시)
def run_detectron2(image_path):
    # 이 부분에 Detectron2 모델 로드 및 추론 코드 작성
    # 예시 결과를 반환
    return {
        "image_path": image_path,
        "detections": [
            {"label": "car", "confidence": 0.98, "bbox": [100, 50, 200, 150]},
            {"label": "person", "confidence": 0.95, "bbox": [300, 80, 400, 200]}
        ]
    }