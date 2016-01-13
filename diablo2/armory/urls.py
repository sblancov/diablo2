from django.conf.urls import url
from django.views.generic.list import ListView

from models import Helm

urlpatterns = [
    url(r'^helms$', ListView.as_view(model=Helm)),
]
