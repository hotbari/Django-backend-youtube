### 강사님 GIT
https://github.com/Seopftware/django-backend-youtube2

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

FileField는 장고에 파일을 저장한다.
컴퓨터를 쓰다보면 느려지는 것처럼 장고에 파일이 저장되면 로드가 느려지기 때문에 urlField


비디오 관련 RESTAPI
1. 비디오 리스트
get 전체 목록 조회
post 새로운 비디오 생성
put X
delete X - 전체 데이터 삭제 금지

기본틀 
class VideoList():
    def get():
        pass

    def post():
        pass


2. 비디오 디테일
get 특정 비디오 조회
put 특정 비디오 업데이트
delete 특정 비디오 삭제

TDD 방식으로 테스트코드 먼저 작성 -> 이게 통과하게끔 코드 작성

클래스 모델을 정의 -> makemirations (장고에게 알려주기) -> migrate(장고가 DB를 찾아감)
app을 실행해줘 --rm remove 컨테이너 지워줘 sh 쉘스트리트 실행해줘


>> 오류
장고 어드민 오류에서 auth_user 테이블에서 오류 발생
docker-compose run --rm app sh -c 'python manage.py dbshell'
youtube=# 이렇게 뜨면 DROP TABLE django_admin_log;
문젲가 됐던 0001 파일은 sqlmigrate 하겠다
docker-compose run --rm app sh -c 'python manage.py sqlmigrate admin 0001 | ./manage.py dbshell'
서버실행 docker-compose up


비디오 테스트 코드 만들고 뷰 함수 만들러 ㄱㄱ

비디오 비주얼라이즈에서 read_only=True 안했더니
..F.F
======================================================================
FAIL: test_video_detail_put (videos.tests.VideoAPITestCase.test_video_detail_put)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/app/videos/tests.py", line 92, in test_video_detail_put
    self.assertEqual(res.status_code, status.HTTP_200_OK)
AssertionError: 400 != 200

======================================================================
FAIL: test_video_list_post (videos.tests.VideoAPITestCase.test_video_list_post)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/app/videos/tests.py", line 66, in test_video_list_post
    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
AssertionError: 400 != 201

----------------------------------------------------------------------
Ran 5 tests in 7.633s

FAILED (failures=2)
오류 떴었음...!


모델을 만들면 ... 세팅에 앱추가해주고 메잉크마이그레이션.. 마이그레이트 ... 꼭 하세요... 왜 안하시는지 귀찮은가요? 
하셔야합니다.. 그래야 장고가 알 수 있거든요


video api에서 comments를 보여주고싶은데 왜 안돼!
일단 comments 폴더에 시리얼라이즈 추가
순환 참조... 문제라는데 뭘까? 이거는 내가 걍 잘못한거고 시리얼라이즈로 해결하면 됨
comment_set이랑 many=True !!

도커 파일이나 도커 컴포즈에 명령어 추가했을 때만 빌드

### 기본 과정
모델 -> 세팅 -> 마이그레이션-> 테스트 -> 뷰 -> 시리얼라이즈
어드민 페이지에서 관리하려면 어드민 등록

# 구독 버튼 테스트
    # api/v1/sub
    def test_sub_list_post(self):
        url = reverse()
        data = {
            
        }
        
        self.client.post(url,data)

구조는 유사

save()는 업데이트 때만

## *args **kwargs
args(1,2)
kwargs(a=1, b=2)

대댓글
parent =models.ForeignKey('self, dondelte_models>cASCADE, null=True, blank=True)

API 따기
개발자도구에서 네트워크 켜놓고 실행해서 로그 확인


### 3월 25일
http - websocket 차이 많음
헤더의 크기 차이
socket : 양방향 통신 가능, low overhead, frame(웹소켓에서 데이터를 나누는 단위)
3 ways 핸드쉐이크



