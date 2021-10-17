from django.urls import path

from . import views as guiViews

urlpatterns = [

    path('', guiViews.accueil, name='accueil'), 
    path('ville', guiViews.ville, name='ville'), 
    path('lieu/ville/<int:town_id>/', guiViews.lieu, name='lieu'), 
    path('lieu/ville/<int:town_id>/categorie/<int:cat_id>', guiViews.lieuCat, name='lieu-categorie'), 
    path('creer-compte', guiViews.escription, name='creer-compte'), 
    path('login', guiViews.userLogin, name='login'), 
    path('logout', guiViews.userLogout, name='logout'),
    path('dashboard', guiViews.dashboard, name='dashboard'), 
    path('evenement', guiViews.evenement, name='evenement'), 
    path('itineraire', guiViews.itineraire, name='itineraire'), 
]
