import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

safety_cate = {
    "태풍 ": "01001",
    "홍수": "01002",
    "호우": "01003",
    "강풍": "01004",
    "대설": "01005",
    "한파": "01006",
    "풍랑": "01007",
    "황사": "01008",
    "폭염": "01009",
    "가뭄 ": "01010",
    "지진": "01011",
    "지진해일": "01012",
    "해일": "01013",
    "산사태": "01014",
    "화산폭발": "01015",
    "해양오염사고": "02001",
    "대규모 수질오염": "02002",
    "식용수": "02003",
    "공동구 재난": "02004",
    "가축질병": "02005",
    "감염병 예방": "02006",
    "철도·지하철사고": "02007",
    "금융전산": "02008",
    "원전사고": "02009",
    "화학물질사고": "02010",
    "화재": "02011",
    "산불": "02012",
    "건축물 붕괴": "02013",
    "댐 붕괴": "02014",
    "폭발": "02015",
    "항공기사고 ": "02016",
    "화생방사고 ": "02017",
    "정전": "02018",
    "전기·가스사고": "02019",
    "유도선 사고": "02020",
    "수난사고 ": "02021",
    "테러발생시 ": "02022",
    "전력수급단계별": "02023",
}

url = "https://www.safetydata.go.kr"
dataName = "/V2/api/DSSP-IF-20588"
serviceKey = "854WZLWK1RKW0WGM"


def get_behaviour_tips(safety_cate_name):
    if safety_cate_name not in safety_cate:
        return "해당하는 안전정보가 없습니다."
    payloads = {"serviceKey": serviceKey, "returnType": "json", "pageNo": "1", "numOfRows": "100", "safety_cate": safety_cate[safety_cate_name]}

    response = requests.get(url + dataName, params=payloads)

    response_json = response.json()

    return response_json["body"]
