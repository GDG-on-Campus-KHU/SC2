import requests
import urllib.parse

url = "http://openapi.safekorea.go.kr/openapi/service/behaviorconduct/disaster/civildefence/total/list"
service_key = "szf/qk3jq0Jrn55bQhWFc8uvRFtq5U3sduU/CC41pB6mRbMhYrdm1gQGMS0hfJ1CYeUCfnXihAd8D2wSG37snQ=="
params = {
    "serviceKey": urllib.parse.unquote(service_key),
    "safety_cate": "04001",
}

response = requests.get(url, params=params)
print(response.content)
