from django.urls import path
from DontStarve import views

app_name='DontStarve'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
    path('detail/<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
]