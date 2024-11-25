from load import load_json
from seoul_api import fetch_hotspot_info
from distance import get_distance_between_to_address

class HotspotAnalyzer:
    def __init__(self, spot_json_path, clientspot):
        # 데이터 로드 및 초기화
        self.loaded_places = load_json(spot_json_path)
        self.hotspot_areas = self.loaded_places.get("hotspot_areas", [])
        self.hotspot = self._get_hotspot()
        self.r2_hotspot = self._get_r2_hotspot()
        self.clientspot = clientspot

    def _get_hotspot(self):
        # hotspot_areas 리스트에서 4번째 장소 가져오기 (인덱스 4가 존재하면)
        return self.hotspot_areas[4] if len(self.hotspot_areas) > 4 else None

    def _get_r2_hotspot(self):
        # r2_hotspot을 첫 번째 단어로 분리 (공백 기준)
        return (self.hotspot_areas[4] if len(self.hotspot_areas) > 4 else None).split()[0] 

    def analyze(self):
        # 정보를 가져오고 출력하는 메서드
        info1 = fetch_hotspot_info(self.hotspot)
        info2 = get_distance_between_to_address(self.r2_hotspot, self.clientspot)

        print("result")
        print(info1)
        print(info2)

# 사용 예시
spot_json_path = "/Users/kimjihe/Desktop/sprint_challenge/data/spot.json"
clientspot = "석촌고분"
analyzer = HotspotAnalyzer(spot_json_path, clientspot)
analyzer.analyze()
