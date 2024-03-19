

### 3. 장고프로젝트 세팅

requirement.txt 배포용
requirements.dev.txt 개발/테스트용


마운드 : 로컬에 저장하면 마운트(docker-compose up or dowm)하면 
    컨테이너가 제거되어도 데이터가 보존된다. 로컬 호스트 환경(./data/db)에 저장해서.


## Youtube API 개발

### 1. 모델(테이블) 구조

테이블 모델 생성 : users(디폴트) videos reactions comments subscriptions commom(디폴트)
docker-compose run --rm app sh -c 'python manage.py startapp users'


### Custion User Model Create
- TDD => 개발 및 디버깅 시간을 엄청 줄일 수 있다 (PDB도 써볼게요! Python Debugger)
    User 관련 테스트 코드

>>app.app.settings.py 로 이동

max_length=255인 이유 : charfield로 하면 varchar로 db에 들어간다, 바차의 가변성 때문에 적게 잡아 터지는 것보다 나아서


PermissionsMixin 추가 import함 왜? 유저권한관리를 위해 필요한 모듈!


users말고 UsersConfig를 가져오는 이유 : 라벨데이터가 변경할 일이 많아 용이한 커스텀을 위함

> docker-compose run --rm app sh -c ""


>>>   File "/py/lib/python3.11/site-packages/django/db/migrations/loader.py", line 327, in check_consistent_history
    raise InconsistentMigrationHistory(
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
어드민이랑 충돌나서 settings.py 에서 어드민 주석처리함 app.url에서도 주석처리함
docker-compose run --rm app sh -c 'python manage.py migrate'
주석 풀고 다시 migrate함



### 3월 19일
## DRF 세팅 (Django RestFrame work)
설치할 것 : drf-spectacular (swaggerUI, redoc만들어서 소통 등을 사용하여 RESTAPI 테스트), DjangoRestframework

의존성 관리를 위해 requirements.txt에 설치하고 빌드해주기
docker-compose build
도커파일 가보면 requirments install 로직을 작성해놓았으니 빌드만 해주면 됨
(설치 버전 확인은 공식문서 들어가서)
빌드 했으면 settings.py ㄱㄱ app/urls.py ㄱㄱ api, swagger, redoc 공식문서에 있는 대로 등록해주기

실행해봅시다, docker-compose up

도커에서 빌드 : 라이브러리 추가, 커맨드 변경



## 비디오 모델 만든대 그 전에 커먼부터 만들쟤

커먼 만들었어요~ common/models.py