import requests
import math
from load import load_env_variable
from space_to_address import get_first_road_address


def __get_distance_result__(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_distance_between_to_address(addr1, addr2):
    kakao_key = load_env_variable("KAKAO_API_KEY")

    addr1_to_address = get_first_road_address(addr1)
    addr2_to_address = get_first_road_address(addr2)

    response = requests.get(
        "https://dapi.kakao.com/v2/local/search/address.json",
        params={"query": addr1_to_address},
        headers={"Authorization": "KakaoAK " + kakao_key},
    ).json()
    print(response)
    x, y = response["documents"][0]["x"], response["documents"][0]["y"]  # x, y= 위도, 경도

    response = requests.get(
        "https://dapi.kakao.com/v2/local/geo/transcoord.json",
        params={"x": x, "y": y, "output_coord": "WTM"},
        headers={"Authorization": "KakaoAK " + kakao_key},
    ).json()
    # x1, y1 = 위경도를 WTM으로 변환
    x1, y1 = response["documents"][0]["x"], response["documents"][0]["y"]

    response = requests.get(
        "https://dapi.kakao.com/v2/local/search/address.json",
        params={"query": addr2_to_address},
        headers={"Authorization": "KakaoAK " + kakao_key},
    ).json()
    x, y = response["documents"][0]["x"], response["documents"][0]["y"]

    response = requests.get(
        "https://dapi.kakao.com/v2/local/geo/transcoord.json",
        params={"x": x, "y": y, "output_coord": "WTM"},
        headers={"Authorization": "KakaoAK " + kakao_key},
    ).json()
    x2, y2 = response["documents"][0]["x"], response["documents"][0]["y"]

    return __get_distance_result__(x1, y1, x2, y2)