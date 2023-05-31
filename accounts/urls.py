from django.urls import path
from.import views

app_name='accounts'

urlpatterns=[
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('changePassword/',views.changePassword,name='changePassword'),
    path('resetPassword/',views.resetPassword,name='resetPassword'),
]