from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.contact, name='contact'),
    #url(r'^success/$', views.contact_success, name='contact_success'),
]