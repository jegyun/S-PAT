# 
FROM python:3.11-slim

# curl 설치
RUN apt update && apt install -y curl

# 컨테이너 내 작업 디렉토리를 /code로 설정
WORKDIR /code

# 호스트의 requirements.txt를 컨테이너에 복사
COPY ./requirements.txt /code/requirements.txt

# 필요한 파이썬 패키지를 설치
RUN pip install --no-cache-dir -r /code/requirements.txt

# 컨테이너에서 사용할 포트 8000을 명시적으로 열어줌
EXPOSE 8000

# 전체 app 디렉토리를 컨테이너에 복사
COPY ./app /code/app

# alembic 관련 파일들 복사
COPY ./alembic /code/alembic
COPY ./alembic.ini /code/alembic.ini

HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/api/health || exit 1

# FastAPI 앱을 uvicorn으로 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]