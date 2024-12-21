FROM python:3.9-slim

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    git wget build-essential clang libomp-dev \
    libgl1-mesa-glx libglib2.0-0 \
    && apt-get clean

# Python 환경 설정
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Detectron2 설치 (Git clone 및 빌드)
RUN git clone https://github.com/facebookresearch/detectron2.git \
    && cd detectron2 \
    && pip install -e .

# 애플리케이션 복사
COPY .env /app/.env
COPY app/ /app/app/
COPY model/ /app/model/

# Flask 실행
CMD ["python3", "/app/app/main.py"]


