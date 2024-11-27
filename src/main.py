from hotspot_analyzer import HotspotAnalyzer
import sys

def main():
    hotspot="여의도" #spot.json 참고 
    clientspot = "하나증권"
    safety_cate_name = "홍수" #behaviour_tips의 safety_cate 참고
    output_path = f"/Users/kimjihe/Desktop/SC2/src/result/{safety_cate_name}.json"

    analyzer = HotspotAnalyzer(hotspot, clientspot, safety_cate_name, output_path)

    analyzer.analyze()

if __name__ == "__main__":
    main()