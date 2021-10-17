from django.shortcuts import render, redirect
from django.contrib import messages
from app import models as appModels
from django.shortcuts import get_object_or_404

from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from app import forms

from .forms import UserForm
from app.forms import *


def accueil(request):
    villes = appModels.Ville.objects.all()
    context = {
        'villes': villes
    }
    return render(request, 'gui/pages/accueil.html', context)



def ville(request):
    villes = appModels.Ville.objects.all()
    context = {
        'villes': villes
    }
    return render(request, 'gui/pages/ville.html', context)



def lieu(request, town_id):

    town  = get_object_or_404(appModels.Ville, id=town_id)

    places = town.lieu_set.all()

    categories = appModels.Type.objects.all()

    context = {
        'categories': categories,
        'places': places,
        'town': town
    }
    return render(request, 'gui/pages/lieu.html', context)


def lieuCat(request, town_id, cat_id):

    town  = get_object_or_404(appModels.Ville, id=town_id)

    categorie = get_object_or_404(appModels.Type, id=cat_id)

    places = town.lieu_set.filter(type=categorie)

    categories = appModels.Type.objects.all()

    context = {
        'categories': categories,
        'places': places,
        'town': town
    }
    return render(request, 'gui/pages/lieu.html', context)



def userLogin(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('evenement')

        else:
            messages.info(request, 'Le nom d\'utilisateur ou le mot de passe est incorrect !')

    return render(request, 'gui/pages/login.html')


def userLogout(request):
    logout(request)
    return redirect('accueil')



def escription(request):

    form = UserForm()

    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        if username and email and password:
            user = User.objects.create(
                username = username,
                email = email,
                password = make_password(password)
            )


            messages.success(request, 'Salut ' + user.username + ', votre compte a été crée avec succès...')

    context = {'form': form}

    return render(request, "gui/pages/escription.html", context)



def dashboard(request):

    pays = Pays.objects.all()
    provinces = Province.objects.all()
    villes = Ville.objects.all()
    lieux = Lieu.objects.all()
    types = Type.objects.all()

    paysForm = PaysForm()
    provinceForm = ProvinceForm()
    villeForm = VilleForm()
    typeForm = TypeForm()
    lieuForm = LieuForm()

    if request.method == 'POST':

        nom_pays = request.POST.get('nom_pays')
        code_pays = request.POST.get('code_pays')

        nom_province = request.POST.get('nom_province')
        if request.POST.get('pays'):
            paysField = Pays.objects.get(id=request.POST.get('pays'))

        nom_ville = request.POST.get('nom_ville')
        description_ville = request.POST.get('description_ville')
        if request.POST.get('province'):
            provinceField = Province.objects.get(id=request.POST.get('province'))

        nom_type = request.POST.get('nom_type')

        # Lieu
        nom_lieu = request.POST.get('nom_lieu')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        description_Lieu = request.POST.get('description_Lieu')
        if request.POST.get('type'):
            type_lieu = Type.objects.get(id=request.POST.get('type'))
        if request.POST.get('ville'):
            ville_lieu = Ville.objects.get(id=request.POST.get('ville'))
        image_1 = request.POST.get('image_1')
        

        if nom_pays and code_pays:
            Pays.objects.create(
                nom_pays = nom_pays,
                code_pays = code_pays
            )
        elif nom_province and paysField:
            Province.objects.create(
                nom_province = nom_province,
                pays = paysField
            )
        elif nom_ville and provinceField and description_ville:
            Ville.objects.create(
                nom_ville = nom_ville,
                description_ville = description_ville,
                province = provinceField
            )
        elif nom_type:
            Type.objects.create(
                nom_type = nom_type
            )
        elif nom_lieu and longitude and latitude and type_lieu and ville_lieu:
            Lieu.objects.create(
                nom_lieu = nom_lieu,
                longitude = longitude,
                latitude = latitude,
                description_Lieu = description_Lieu,
                type = type_lieu,
                ville = ville_lieu,
                image_1 = image_1
            )

    context = {
        'pays': pays,
        'provinces': provinces,
        'villes': villes,
        'lieux': lieux,
        'types': types,
        'paysForm': paysForm,
        'provinceForm': provinceForm,
        'villeForm': villeForm,
        'typeForm': typeForm,
        'lieuForm': lieuForm
    }

    return render(request, "gui/pages/dashboard.html", context)



def evenement(request):

    evenements = appModels.Evenement.objects.all()

    form = EvenementForm()

    if request.method == 'POST':

        form = EvenementForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'evenements': evenements
    }

    return render(request, "gui/pages/evenement.html", context)


def itineraire(request):
    return render(request, "gui/pages/itineraire.html")
