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