

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
   
   path('sports',views.home,name='home'),
   path('contact',views.contact,name='contact'),
   path('school_reg',views.school_reg,name='school_reg'),
   path('player_reg',views.player_reg,name='player_reg'),
   path('player_data',views.player_data,name='player_data'),
   path('team_formation',views.team_formation,name='team_formation'),
   #--------------------------------------------------------------#
   path('school_register',views.school_register,name='school_register'),
   path('player_register',views.player_register,name='player_register'),
   path('team_form',views.team_form,name='team_form'),
   path('match_form',views.match_form,name='match_form'),
   path('match_toss',views.match_toss,name='match_toss'),
   path('match_view/',views.match_view,name='match_view'), 
   #url(r'^match_view/', views.match_view),
   path('volleyball_view/',views.volleyball_view,name='volleyball_view'),
   path('football_view/',views.football_view,name='football_view'),

   path('',views.dashboard_demo,name='dashboard_demo'),

]

