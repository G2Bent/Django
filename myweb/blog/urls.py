from django.conf.urls import url
from . import views
from blog.views import page,upload,upload_save
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^login/$',views.login),
    url(r'^login_ok/$',views.login_ok),
    url(r'^logout/$',views.logout),
    url(r'^accounts/login/$',views.index),
    url(r'^student/$',views.student),
    url(r'^book/$',views.SBook),
    url(r'^book_page/$',page),
    url(r'^upfile/$',upload),
    url(r'^upload_s/$',upload_save),
]