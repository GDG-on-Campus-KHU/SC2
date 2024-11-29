from flask import Flask, request, jsonify
from hotspot_analyzer import HotspotAnalyzer
from detectron import run_detectron2
import os
import json
import cv2

app = Flask(__name__)

def analyze_and_merge(hotspot, clientspot, safety_cate_name, image_path):
    #1. HotspotAnalyzer 결과 분석
    analyzer = HotspotAnalyzer(hotspot, clientspot, safety_cate_name)
    hotspot_results = analyzer.analyze()

    # 2. Detectron2 결과 얻기 
    detectron2_results = run_detectron2(image_path)

    combined_results = {
        "hotspot_results": hotspot_results,
        "detectron2_results": detectron2_results
    }

    return combined_results


@app.route('/analyze', methods=['POST'])
def analyze():
    data=request.json
    image_path="/Users/kimjihe/Desktop/SC2/src/images/flood_begium.jpg"
    im = cv2.imread(image_path)
    hotspot=data.get("hotspot", "경복궁")
    clientspot=data.get("clientspot", "서울역")
    safety_cate_name=data.get("safety_cate_name", "대설")

    try:
        combined_results = analyze_and_merge(hotspot, clientspot, safety_cate_name, image_path)
        
        response = jsonify({"status": "success", "results": combined_results})
        response.charset = "utf-8" 
        return response
    except Exception as e:
        response = jsonify({"status": "error", "message": str(e)})
        response.charset = "utf-8" 
        return response, 500
    

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)