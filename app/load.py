import os
import json
from dotenv import load_dotenv

def load_env_variable(key, default_value=None):
    """
    .env 파일에서 환경 변수를 로드하고 해당 키의 값을 반환합니다.
    """
    load_dotenv('/app/.env')
    value = os.getenv(key, default_value)
    if not value:
        raise EnvironmentError(f"환경 변수 '{key}'가 설정되지 않았습니다.")
    return value

def load_json(file_path):
    """
    JSON 파일을 로드하고 데이터를 반환합니다.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"'{file_path}' 경로에 JSON 파일이 존재하지 않습니다.")
    except json.JSONDecodeError:
        raise ValueError(f"'{file_path}' 파일이 올바른 JSON 형식이 아닙니다.")
