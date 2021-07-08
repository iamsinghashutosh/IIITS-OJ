from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('savereview/',views.savereview,name='save-review'),
    path('sendmail/',views.send_email,name='sendmail')

    
]

