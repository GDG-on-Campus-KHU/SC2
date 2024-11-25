import requests
import xml.etree.ElementTree as ET
from load import load_env_variable

def fetch_hotspot_info(hotspot_name):
    """
    서울 교통 데이터 API에서 핫스팟 정보를 조회하고 필요한 데이터를 추출합니다.
    
    Args:
        api_key (str): 서울 교통 데이터 API 키.
        hotspot_name (str): 조회할 핫스팟 이름.
    
    Returns:
        dict: 핫스팟 관련 정보가 담긴 딕셔너리. API 요청 실패 시 None 반환.
    """
    if not hotspot_name:
        print("핫스팟 정보가 부족하여 API 요청을 진행할 수 없습니다.")
        return None
    
    seoul_transportation_api_key=load_env_variable("SEOUL_TRANSPORTATION_API_KEY")

    url = f'http://openapi.seoul.go.kr:8088/{seoul_transportation_api_key}/xml/citydata/1/10/{hotspot_name}'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            # 응답 내용 파싱
            xml_data = response.content.decode('utf-8')  # UTF-8로 디코딩
            root = ET.fromstring(xml_data)  # XML 파싱

            # 정보 추출
            info = {
                "area_nm": root.find(".//AREA_NM").text if root.find(".//AREA_NM") is not None else "정보 없음",
                "live_ppltn_stts": root.find(".//LIVE_PPLTN_STTS").text if root.find(".//LIVE_PPLTN_STTS") is not None else "정보 없음",
                "area_congest_lvl": root.find(".//AREA_CONGEST_LVL").text if root.find(".//AREA_CONGEST_LVL") is not None else "정보 없음",
                "area_congest_msg": root.find(".//AREA_CONGEST_MSG").text if root.find(".//AREA_CONGEST_MSG") is not None else "정보 없음",
                "area_ppltn_min": root.find(".//AREA_PPLTN_MIN").text if root.find(".//AREA_PPLTN_MIN") is not None else "정보 없음",
                "area_ppltn_max": root.find(".//AREA_PPLTN_MAX").text if root.find(".//AREA_PPLTN_MAX") is not None else "정보 없음",
                "warn_val": root.find(".//WARN_VAL").text if root.find(".//WARN_VAL") is not None else "정보 없음",
                "warn_stress": root.find(".//WARN_STRESS").text if root.find(".//WARN_STRESS") is not None else "정보 없음",
                "announce_time": root.find(".//ANNOUNCE_TIME").text if root.find(".//ANNOUNCE_TIME") is not None else "정보 없음",
                "command": root.find(".//COMMAND").text if root.find(".//COMMAND") is not None else "정보 없음",
                "cancel_yn": root.find(".//CANCEL_YN").text if root.find(".//CANCEL_YN") is not None else "정보 없음",
                "warn_msg": root.find(".//WARN_MSG").text if root.find(".//WARN_MSG") is not None else "정보 없음"
            }
            return info
        except ET.ParseError:
            print("XML 데이터 파싱 실패")
            return None
    else:
        print(f"API 요청 실패: {response.status_code}")
        return None