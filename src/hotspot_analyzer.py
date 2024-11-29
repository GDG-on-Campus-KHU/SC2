import json
from load import load_json
from seoul_api import fetch_hotspot_info
from distance import get_distance_between_to_address
from behaviour_tips import get_behaviour_tips

class HotspotAnalyzer:
    def __init__(self, hotspot, clientspot, safety_cate_name):
        # 데이터 로드 및 초기화
        self.hotspot = hotspot
        self.clientspot = clientspot
        self.safety_cate_name = safety_cate_name

    def analyze(self):
        # 정보를 가져오고 출력하는 메서드
        info1 = fetch_hotspot_info(self.hotspot)
        info2 = get_distance_between_to_address(self.hotspot, self.clientspot)
        info3 = get_behaviour_tips(self.safety_cate_name)

        # JSON 형식 데이터 생성
        result_data = {
            "push_alarming": f"{self.hotspot}에 {self.safety_cate_name}가 발생했습니다. 안전에 유의하세요", #알람 정보
            "congestion": info1, #혼잡도 정보
            "disaster_radius": info2,  #재난발생지역과 사용자 간의 거리
            "action_plan": info3 #행동요령
        }

        return result_data

