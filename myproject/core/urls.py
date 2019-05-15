from django.urls import path
from myproject.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('blank/', v.blank, name='blank'),
    path('email/', v.email, name='email'),
    path('compose/', v.compose, name='compose'),
    path('calendar/', v.calendar, name='calendar'),
    path('chat/', v.chat, name='chat'),
    path('charts/', v.charts, name='charts'),
    path('forms/', v.forms, name='forms'),
    path('ui/', v.ui, name='ui'),
    path('basic_table/', v.basic_table, name='basic_table'),
    path('datatable/', v.datatable, name='datatable'),
    path('google_maps/', v.google_maps, name='google_maps'),
    path('vector_maps/', v.vector_maps, name='vector_maps'),
    path('p404/', v.p404, name='p404'),
    path('p500/', v.p500, name='p500'),
    path('signin/', v.signin, name='signin'),
    path('signup/', v.signup, name='signup'),
    path('buttons/', v.buttons, name='buttons'),
]
