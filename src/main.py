from hotspot_analyzer import HotspotAnalyzer
import sys

def main():
    hotspot="경복궁" #spot.json 참고 
    clientspot = "서울역"
    safety_cate_name = "대설" #behaviour_tips의 safety_cate 참고
    output_path = f"/Users/kimjihe/Desktop/SC2/src/result/{safety_cate_name}.json"   #json 결과파일 저장경로

    analyzer = HotspotAnalyzer(hotspot, clientspot, safety_cate_name, output_path)

    analyzer.analyze()

if __name__ == "__main__":
    main()