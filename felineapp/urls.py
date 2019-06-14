from django.conf.urls import url, include
from felineapp import views

app_name = 'felineapp'

urlpatterns = [
    url(r'^register/$', views.Register.as_view(), name='register')
]