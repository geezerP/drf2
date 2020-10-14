# from django.urls import path
from django.conf.urls import url
from .views import PollDetail, PollList
urlpatterns = [
    url('polls/', PollList.as_view(), name='polls_list'),
    url('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail')
]