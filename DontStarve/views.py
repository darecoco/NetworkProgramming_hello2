from django.shortcuts import render
from django.views.generic import ListView
from DontStarve.models import Character


class CharacterListView(ListView):
    model = Character

    #character_list = Character.objects.all()
    # DB에 모델 데이터 다 가져옴
    #return render(request, 'DontStarve/dharacter_list.html', context={'character_list':character_list}
    # 모델_list.html에 모델_list라는 키로 DB에서 가져온 데이터 넣어서 render 한다.