## Dockerfile

# 도커 이미지 구축
# 알파인은 경량화된 리눅스
FROM python:3.11-alpine3.19

# 도커 이미지 관리자 설정
LABEL maintainer='hotbari'

# 파이썬 관련 로그 확인 옵션(기본값은 0=Fale, 로그 남기지 않음)
ENV PYTHONUNBUFFERED=1

# 로컬에서 작업한 파일들을 가상 환경으로 복사하는 코드
# 복사하고 로컬 파일은 삭제할거임
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# ARG를 사용하여 DEV 변수를 받아옴
ARG DEV=false

# 전체 환경에서 파이썬 모듈(가상환경)을 생성
# EC2 하나를 띄워놨다고 생각해도 됨
# 전체 환경에 파이썬이 있어서 바로 생성 가능
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt ; fi && \
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"

USER django-user
