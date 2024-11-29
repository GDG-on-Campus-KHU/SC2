from flask import Flask, request, jsonify
from hotspot_analyzer import HotspotAnalyzer
from detectron import run_detectron2
import os
import json

app = Flask(__name__)

def analyze_and_merge(hotspot, clientspot, safety_cate_name, image_path, output_path):
    #1. HotspotAnalyzer 결과 분석
    analyzer = HotspotAnalyzer(hotspot, clientspot, safety_cate_name, output_path)
    hotspot_results = analyzer.analyze()

    # 2. Detectron2 결과 얻기 
    #detectron2_results = run_detectron2(image_path, output_path)

    combined_results = {
        "hotspot_results": hotspot_results,
        #"detectron2_results": detectron2_results
    }

    #결과 저잧
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(combined_results, json_file, ensure_ascii=False, indent=0)

    return combined_results


@app.route('/analyze', methods=['POST'])
def analyze():
    data=request.json
    image_path=data.get("./images/화재_회기.jpg")
    hotspot=data.get("hotspot", "경복궁")
    clientspot=data.get("clientspot", "서울역")
    safety_cate_name=data.get("safety_cate_name", "대설")

    output_path = f"./result/{safety_cate_name}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        combined_results = analyze_and_merge(hotspot, clientspot, safety_cate_name, image_path, output_path)
        return jsonify({"status": "success", "results":combined_results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)