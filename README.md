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
      2. python manage.py makemigrations DontStarve
      3. python manage.py migrate
   2. admin
      1. Character
      2. python manage.py createsuperuser