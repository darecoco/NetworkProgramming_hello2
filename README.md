# helloidol2
***
1. startproject helloidol2
   1. python -m pip install django~=4.2
   2. django-admin startproject helloidol2 .
   3. File > Settings... > Language & Framework > Django > [v] Enavle Django Support
   4. Run > Edit Configurations... > + > Django Server > Name: runservr
   5. VCS > Enable Version Control Intergration... > git >` ok
2. startapp DontStarve
   1. python manage.py startapp DontStarve
   2. 'DontStarve', int INSTALLED_APPS in settings.py
3. DontStarve/
   1. models
      1. Character
         1. name, description
         2. `__str__()`: 객체를 출력할 때, 알맞은 string으로 출력하기 위해 만든다
         3. `get_absolute_url()`: 캐릭터 하나 데이터 가져오자
      2. python manage.py makemigrations DontStarve
      3. python manage.py migrate
   2. admin
      1. Character
      2. python manage.py createsuperuser
   3. views
      1. R: CharacterListView
      2. R: CharacterDetailView
      3. R: CharacterCreateView
   4. templates/DontStarve/
      1. character_list.html
      2. character_detail.html
      3. character_create.html
   5. urls
      1. DontStarve: character_list
      2. DontStarve: character_detail
      3. DontStarve: character_create
   6. templates
      1. hase.html
         1. settings.py > TEMPLATES
            1. ['BASE_DIR' / 'templates']