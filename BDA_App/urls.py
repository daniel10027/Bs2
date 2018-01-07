from django.conf.urls import url

from BDA_App.views import *

urlpatterns = [

    # http://localhost:8000/BDA/ES/pushData/
    url(r'^ES/pushData/?$', PushData.as_view()),

    # http://localhost:8000/BDA/ES/BDA.html
    url(r'^ES/BDA.html/?$', BDA),
]
