from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.apply, name='apply'),
    # url(r'^apply/success/$', views.application_success, name='application_success'),
]
