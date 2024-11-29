from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets import register_coco_instances
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import cv2
import json

# # COCO JSON 파일에서 카테고리 개수 읽기
# def get_num_classes(coco_json_path):
#     with open(coco_json_path, 'r') as f:
#         coco_data = json.load(f)
#     return len(coco_data["categories"])

# 심각도 측정 기준 (확신도에 따라)
def measure_severity(scores):
    severity = []
    for score in scores:
        if score > 0.9:
            severity.append("High Severity")
        elif score > 0.7:
            severity.append("Medium Severity")
        else:
            severity.append("Low Severity")
    return severity

# Detectron2 실행 함수 (예시)
def run_detectron2(image_path, output_path):
    # 기존 데이터셋 제거
    for dataset_name in ["train_dataset", "val_dataset", "test_dataset"]:
        if dataset_name in MetadataCatalog.list():
            MetadataCatalog.remove(dataset_name)
        if dataset_name in DatasetCatalog.list():
            DatasetCatalog.remove(dataset_name)

    # 데이터셋 다시 등록
    register_coco_instances("train_dataset", {}, "/path/to/dataset/train/train_coco.json", "/path/to/dataset/train/images")
    register_coco_instances("val_dataset", {}, "/path/to/dataset/val/val_coco.json", "/path/to/dataset/val/images")
    register_coco_instances("test_dataset", {}, "/path/to/dataset/test/test_coco.json", "/path/to/dataset/test/images")

    num_classes = 3

    # Config 설정
    cfg = get_cfg()
    cfg.merge_from_file("path/to/mask_rcnn_R_50_FPN_3x.yaml")
    cfg.MODEL.WEIGHTS = "path/to/model_final.pth"
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = num_classes  # num_classes 설정
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # 추론 시 threshold 설정
    cfg.DATASETS.TEST = ("test_dataset",)

    # Predictor 생성
    predictor = DefaultPredictor(cfg)

    im = cv2.imread(image_path)
    outputs = predictor(im)

    # 예측 결과의 확신도 (scores) 가져오기
    scores = outputs["instances"].scores

    # 심각도 측정
    severity = measure_severity(scores)

    # 결과 출력
    # for idx, score in enumerate(scores):
    #     print(f"Object {idx + 1}: {severity[idx]} (Confidence Score: {score:.2f})")

    # 결과 시각화
    v = Visualizer(im[:, :, ::-1], MetadataCatalog.get("test_dataset"), scale=1.2)
    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    result_image = v.get_image()[:, :, ::-1]

    # 결과 이미지 저장
    result_image_path = f"{output_path}/result.jpg"
    cv2.imwrite(result_image_path, result_image)


    return {"severity": severity, "result_image_path": result_image_path}