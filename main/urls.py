from django.urls import path

from .views import index, other_page, BLoginView, profile, BLogoutView, ChangUserInfoView, BPasswordChangeView

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('<str:page>/', other_page, name='other'),
    path('accounts/login/', BLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', BPasswordChangeView.as_view(), name='password_change'),
]