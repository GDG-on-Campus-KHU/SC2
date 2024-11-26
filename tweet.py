import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
# bearer_token = os.environ.get("BEARER_TOKEN")
bearer_token = "AAAAAAAAAAAAAAAAAAAAABFMxAEAAAAA%2FHR93WlMHJss9QuNQjMg877q0BE%3DdDqJ3SX5rGshq4SN1lkNXrnBkwPvCKIp9i4UE2AhCApiwmo8Qh"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_search(keyword, tweet_fields="text,created_at,geo", media_fields="url,preview_image_url"):
    query_params = {
        "query": "재난 lang:ko",
        "tweet.fields": tweet_fields,
        "expansions": "attachments.media_keys",
        "media.fields": media_fields,
    }
    json_response = connect_to_endpoint(search_url, query_params)
    open("result.json", "w").write(json.dumps(json_response, indent=4, sort_keys=True))
    return json.dumps(json_response, indent=4, sort_keys=True)
