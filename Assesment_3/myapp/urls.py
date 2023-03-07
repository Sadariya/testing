from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns =[
    
    path('',views.index),
    path('forget/',views.forget),
    path('home/',views.home,name='home'),
    path('profile/',views.profile),
    path('userlogout',views.userlogout),

    path('societymember/',views.societymember),
    path('editsocietymember/',views.editsocietymember,name='editsocietymember'),
    path('deletemember/<int:id>',views.deletemember),

    path('watchmen/',views.watchmen),
    path('editwatchmen/',views.editwatchmen,name='editwatchmen'),
    path('deletewatchman/<int:id>',views.deletewatchman),

    path('visitors/',views.visitors),
    path('visitors_list/',views.visitors_list),

    path('events/',views.events),
    path('editevent/',views.editevent),
    path('deleteevent/<int:id>',views.deleteevent),

    path('notices/',views.notices),
    path('notice_view/',views.notice_view),

]