from django.urls import path
from . import views
"""
path =('',views.index,name = 'index')-This means https://website.com we can enter into the page.


But

path =('/downloads',views.downloads,name = 'downloads')--This means https://website.com/downloads we can enter into the page.
whatever written in the brackets is or should be written in the url while typed by the user.

Using CSRF token in django protects the info as we use Post method in our index.html form.
Post method is used for high security,it will not allow user to see the eneterd text or we can say info and get method is used for normal data generally not so secure.
"CSRF"token very very very important.

"""

urlpatterns = [
    path('',views.index,name = "index"),
    path('counter',views.counter,name = 'counter')
]
