import requests
import re
import json
import xml.etree.ElementTree as ET
from load import load_env_variable

def get_first_road_address(keyword):
    """
    주어진 검색어로 주소 API를 호출하고 첫 번째 도로명 주소를 반환합니다.
    
    Args:
        keyword (str): 검색어.
        current_page (int): 검색 페이지 번호 (기본값: 1).
        count_per_page (int): 페이지당 검색 결과 수 (기본값: 10).
    
    Returns:
        str: 첫 번째 도로명 주소. 결과가 없으면 빈 문자열 반환.
    """
    url = "https://business.juso.go.kr/addrlink/addrLinkApiJsonp.do"
    confm_key = load_env_variable("ADDRESS_API_KEY")

    params = {
        "confmKey": confm_key,
        "currentPage": 1,
        "countPerPage": 10,
        "keyword": keyword,
    }

    response = requests.get(url=url, params=params)
    jsonp_data = response.text
    print(jsonp_data)

    try:
        # JSONP 형식에서 callback 함수 제거
        json_data = (re.search(r"\((.*?)\)$", response.text)).group(1) 
        data = json.loads(json_data)

    except json.JSONDecodeError as e:
        data = parse_xml(jsonp_data)
    
    road_addr = data.get('roadAddr', None)
    if not road_addr:
        raise Exception("도로 주소를 찾을 수 없습니다.")
    
    return road_addr


def parse_xml(xml_data):
    """XML 데이터를 파싱하여 dictionary로 변환"""
    try:
        data = re.search(r"'returnXml':\s*'(.*?)'", xml_data)
        matched_data = data.group(1)
        root = ET.fromstring(matched_data)
        result = {}
        
        # XML에서 원하는 데이터를 추출 (예시로 'roadAddr'을 추출)
        for elem in root.iter():
            if elem.tag == 'roadAddr':
                result['roadAddr'] = elem.text
        
        return result
    except ET.ParseError as e:
        raise Exception(f"XML 파싱에 실패했습니다. 오류: {e}")