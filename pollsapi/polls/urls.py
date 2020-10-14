# from django.urls import path
from django.conf.urls import url
from .views import ChoiceList, CreateVote, PollDetail, PollList
urlpatterns = [
    url('polls/', PollList.as_view(), name='polls_list'),
    url('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    url('choices/', ChoiceList.as_view(), name="choice_list"),
    url('vote/', CreateVote.as_view(), name="create_vote"),
]