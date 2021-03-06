from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

# 나중에 라우팅을 편하게 해주는 것을 하는 것
app_name = 'accountapp'

urlpatterns = [
    #   회원가입으로 가는 페이지로 가는 경로
    path('create/', AccountCreateView.as_view(), name='create'),

    # 로그인, 로그아웃  / 로그인은 템플릿 이름을 설정해줘야 해
    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # 회원정보 확인하기
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

    #  디테일 뷰와 다를 것이 없다.
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

#     회원탈퇴
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete')


]
