##django로 만드는 이상민 웹 이력서

####20210705 오전
- 시크릿 키 env파일로 설정 완료
- .gitignore 추가
- python manage.py startapp accountapp 로 accountapp 추가 settin.py에도 추가
- urls.py 추가 (main urls에 path 추가)
- view httpRespose로 반응 확인

####20210705 오후
- delete __pycache__ 
- extends & include로 UI 구조 설계

####20210720 
- bootstrap
- account 관련 모두 커밋
1. Authentication 진행
- account를 update, delete 같은 경우 파라메터로 접근 타인 것을 지우는 것이 가능해서 로그인했을때만 할 수 있게끔 진행
- 타 유저의 정보를 업데이트 삭제 방지

####20210722
1. decorator 적용
- @method_decorator로 login_required 를 불러와서 get, post 다 적용해야함
- login_required가 해당 경로가 장고가 원하는 대로 되어있음 이걸 수정해야함 => login_url=reverse_lazy('accountapp:login'))
- decorator.py 생성하고 이걸 다시 정리해줬음
- has_ownership

2. 관리자 생성
- python manage.py createsuperuser

3. profileapp 생성
- 회원의 media를 적용 - setting.py에 추가
- profileapp 생성, urls, settings 파일에 경로 추가, profileapp 내 urls 생성

##20210726
1. profileapp 설정
- model 설정 -> migration만들자 -> pillow가 없어서 설치 안됨(pip install pillow) -> python manage.py makemigrations, python manage.py migrate

2. forms.py 설정

3. views, urls 설정
 - create.html에서 form으로 파일을 담아서 전송할때는 enctype을 사용해야 한다.

##20210727
1. Profile views.py에 form_valid를 추가

2. profile info 업데이트
- detail.html에 profile info가 나오게끔 수정
- urls.py에  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)를 추가
- account detail.html, css 추가

3. profile updateview 추가
- views.py에 updateview 추가
- urls.py에 path 추가
- accountapp detail에 a tag 추가

##0729
1. profile 로그인해야 볼 수 있게끔
- decorator 추가

2. profile update redirect 페이지 수정
- success_url = reverse_lazy('accountapp:hello world') 수정
- profile views.py에 get_success_url 추가
- accountapp views.py에 get_success_url 추가

3. accountapp update 단어를 구글 아이콘으로 수정하기

4. account detail.html 수정
- update, delete icons 추가

##0802
1. articleapp 추가
- python manage.py startapp articleapp
- main의 setting, urls 조정

2. Magic Grid 추가
- https://jsfiddle.net/eolaojo/4pov0rdf/
- https://github.com/e-oj/Magic-Grid/tree/master/dist
- magic-grid.cjs.js 를 사용하자
- list.html 수정

3. lorem picsum 추가
- https://picsum.photos/
- magicgrid.js 사진 순서대로 불러오는 거 해줌

4. article Model구축
- model.py 수정, python manage.py makemigrations, python manage.py migrate

##0803
1. Article create 만들기
- articleapp view에 createview 추가
- urls에 path 추가
- create.html 추가
- view에 form_valid 추

2. Article detail 
- articleapp view에 detailview 추가
- urls에 path 추가
- detail.html 추가

3. Article update 
- articleapp view에 updateview 추가
- urls에 path 추가
- update.html 추가 create.html과 같아

4. Article detail.html 버튼 추가

5.  Article delete 
- articleapp view에 deleteview 추가
- urls에 path 추가
- delete.html 추가

##0805
1. articlesapp decorator.py 추가
- 로그인 확인
- 해당 유저인지 아닌지 확인하는 거
- createview 에서는 successurl 추가 

2. Article detail.html 수정
- detail.html 수정
- base.css  추가

3. Article list 수정
- view.py에 ArticleListView 추가
- urls.py path 수정
- list.html 수정
- create button 추가
- pagination 추가
- include로 pagination.html 불러오기

##0809
1. CommentApp(댓글)
- python manage.py startapp commentapp
- setting.py, urls.py 설정하고 urls.py 추가
- Model 구축, models.py, forms.py

2. comment create 구축
- views.py에 CommentCreateView 추가
- urls.py에 urlspattern 추가
- templates/commentapp create.html 추가
- articleapp view.py에 ArticleDetailView에 FormMixin 추가
- detail.html에 {% include 'commentapp/create.html' %} 추가
- create.html에 url 이름 수정, extends 및 blocks 해제, target_article.pk 값 전송을 위해 input hidden 타입 추가
- commentapp view.py에 form_valid 추가, article_pk를 input name 전송

3. comment Delete 추가
- delete.html 추가, urls.py path 추가, view.py view 추가


##0810
1. 댓글 시각화
-  detail.html 수정
    - comment 삭제 버튼 추가
    - 로그인 확인
- CommentCreateView 로그인 확인
- CommentDeleteView 작성자 확인
- decorated.py 추가

2. 반응형으로 만들고 싶다.
- NGROK Tunneling Program => host가 allow가 안되서 에러가 날거임
    - setting.py에서 ALLOWED_HOSTS에 "*"로 모든 ip에서 접근할 수 있게끔
- meta 태그 추가 => 기기에 따라 달라지게
- <meta name="viewport" content="width=device-width, intial-scale=1.0, shrink-to-fit=no">
- shrink-to-fit=no는 파이어 폭스 전용

##0812
1. 모바일로 봤을때 비율 수정 article list
- 가운데 정렬을 위한 Magic grid 수정 gutter 값 수정
- detail.html css 수정
- @media screen and (max-width: 500px) 를 추가적으로 수정함으로 반응형으로

2. projectapp 생성
- python manage.py startapp projectapp
- setting.py, urls.py 추가
- Model 구축
 - forms.py 생성
 - python manage.py makemigrations
 - python manage.py migrate
- View 생성
 - views.py createview 생성
 - urls.py path 추가
 - templates/projectsapp create.html 생성
- Detail  추가
 - detail.html, urls.py, views.py 수정
- createview success_url 수정

##0817
1. Project List 생성
- ariticles의 list.html을 참고해서 list.html 생성
- 게시판의 사진 크기에 맞게 다시 , 게시판에 그림자 지우기
- 게시판의 이름이 길면 레이아웃이 깨짐 절삭해서 보여주자  truncatechars:7
- ariticles, projects로 가는 버튼 생성

##0819
1. view에서 Mixin을 사용해서 project 게시판과 article을 연결
- articleapp Model에 project 필드를 추가
- 바뀐 거 적용해주자 python manage.py makemigrations python manage.py migrate
- forms.py에도 필드에 추가해주자

2. 내 프로필에서 확인하기
- list_fragement.html을 추가

3. 구독을 할 수 있는 subscribeapp
- python manage.py startapp subscribeapp, urls, setting 수정
- Model 구축, Meta 클래스를 이용해서 구독은 한번만 하게끔 
- python manage.py makemigrations python manage.py migrate

##0823
0. subscribeapp model 잘못 해서 다시 수정함
1. subscribeapp view 설정
- 구독하게 될 경우 
- 로그인 확인이랑 리다이렉 해주자
- 버튼을 만들어주자 프로젝트 앱에 리스트에
2. 구독정보가 있는지 없는지 확인
- 구독 버튼을 눌렀는지 안눌렀는지를 확인해주자
=> 프로젝트 앱의 디테일 뷰에서 확인이 되니까 해당 뷰에서 해당 객체가 있는지 여부를 확인하자.
=> 프로젝트 앱의 디테일 페이지를 수정해주자
  
3. 구독한 페이지만 보여지게
- Field Lookups 사용
  - where 구문을 사용하는 것
    - Model__in= 이렇게 사용하면 된다.
    - 원하는 것들을 받아서 리스트에 담고 해주자 
    

##0824
0. 이름 길어서 추가되는 수정해야함
- 확인만 함

1. 좋아요 기능 likeapp
1-1 app 생성
- python manage.py startapp likeapp, setting, urls 수정, urls추가

1-2 Model 구축
- 좋아요 숫자를 세는 모델을 만들건데
-> article Model에도 수정해줘야 해
-> likeapp Model 생성
  -> 두가지 다 반영
  -> python manage.py makemigrations
  -> python manage.py migrate
  
1-3 
- view, urls 작성
  -> view에서 좋아요가 눌렸는지 확인하고 안눌렸다면 추가하고 눌렸다면 리다이렉해주게끔
  -> 리다이렉할때 어디로 갈지도 추가
- articleapp detail.html 좋아요 추가

1-4
- css 수정 
  ->base.css, article detail.html
  
1-5
- 장고 메세지 기능(https://docs.djangoproject.com/en/3.2/ref/contrib/messages/)
- 좋아요를 눌렀을때 유저에게 메세지를 보내주자
-> def add_message(request: {_messages}, level: Any, message: Any, extra_tags: str = '', fail_silently: bool = False) -> Any
-> 위를 사용해서 view.py 수정
-> 해당 메세지를 base.html에서 메세지를 출력할 수 있게끔 해주자
    -> message framework에서 message tag를 수정해서 색색별로 달라지게끔 해주자