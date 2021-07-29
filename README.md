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