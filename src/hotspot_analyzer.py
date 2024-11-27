import json
from load import load_json
from seoul_api import fetch_hotspot_info
from distance import get_distance_between_to_address
from behaviour_tips import get_behaviour_tips

class HotspotAnalyzer:
    def __init__(self, hotspot, clientspot, safety_cate_name, output_path):
        # 데이터 로드 및 초기화
        self.hotspot = hotspot
        self.clientspot = clientspot
        self.safety_cate_name = safety_cate_name
        self.output_path = output_path

    def analyze(self):
        # 정보를 가져오고 출력하는 메서드
        info1 = fetch_hotspot_info(self.hotspot)
        info2 = get_distance_between_to_address(self.hotspot, self.clientspot)
        info3 = get_behaviour_tips(self.safety_cate_name)

        # JSON 형식 데이터 생성
        result_data = {
            "푸시 알림 내용": f"{self.hotspot}에 {self.safety_cate_name}가 발생했습니다. 안전에 유의하세요",
            "혼잡도정보": info1,
            "재난반경": info2,
            "행동요령": info3
        }

        #print(result_data)

        # JSON 파일로 저장
        with open(self.output_path, "w", encoding="utf-8") as file:
            json.dump(result_data, file, ensure_ascii=False, indent=4)

        print(f"결과가 {self.output_path}에 저장되었습니다.")

