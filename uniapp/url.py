__author__ = 'Shaurya'
from django.conf.urls import url, include
from .import views

urlpatterns = [
url(r'^display',views.display, name='display'),
url(r'^about',views.about, name='about'),
url(r'^blog',views.blog, name='blog'),
url(r'^business',views.business, name='business'),
url(r'^fourzerofour',views.fourzerofour, name='fourzerofour'),
url(r'^coming_soon',views.coming_soon, name='coming_soon'),
url(r'^communication',views.communication, name='communication'),
url(r'^contact',views.contact, name='contact'),
url(r'^course_details',views.course_details, name='course_details'),
url(r'^faq',views.faq, name='faq'),
url(r'^form',views.form, name='form'),
url(r'^gallery',views.gallery, name='gallery'),
url(r'^language',views.language, name='language'),
url(r'^login',views.login, name='login'),
url(r'^photography',views.photography, name='photography'),
url(r'^register',views.register,name='register'),
url(r'^single',views.single, name='single'),
url(r'^social_media',views.social_media, name='social_media'),
url(r'^software',views.software, name='software'),
url(r'^regdetails',views.regdetails, name='regdetails'),
url(r'^execute',views.execute, name='execute'),
url(r'^forgotpassword',views.forgotpassword, name='forgotpassword'),
url(r'^recoverpwd',views.recoverpwd, name='recoverpwd'),
url(r'^index',views.index, name='index'),
url(r'^getcity',views.getcity, name='getcity'),
url(r'^getstate',views.getstate, name='getstate'),
#url(r'^prediction',views.prediction, name='prediction'),
url(r'^getprediction',views.getprediction, name='getprediction'),
url(r'^prediction2',views.prediction2, name='prediction2')
]