from django.shortcuts import render
from rest_framework.response import Response


from rest_framework.viewsets import ModelViewSet


from .serializers import *
from .models import *



class PaysApiView(ModelViewSet):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer



class ProvinceApiView(ModelViewSet):
    serializer_class = ProvinceSerializer

    def get_queryset(self):
        return Province.objects.all()
    

    def create(self, request, *args, **kwargs):
        provinceData = request.data
        newProvince = Province.objects.create(
            nom_province = provinceData['nom_province'],
            pays = Pays.objects.get(id=provinceData['pays'])
        )
        newProvince.save()
        serializer = ProvinceSerializer(newProvince)
        return Response(serializer.data)



class VilleApiView(ModelViewSet):
    serializer_class = VilleSerializer

    def get_queryset(self):
        return Ville.objects.all()


    def create(self, request, *args, **kwargs):
        villeData = request.data
        newVille = Ville.objects.create(
            nom_ville = villeData['nom_ville'],
            province = Province.objects.get(id=villeData['province'])
        )
        newVille.save()
        serializer = VilleSerializer(newVille)
        return Response(serializer.data)

    

class TypeApiView(ModelViewSet):
    serializer_class = TypeSerializer

    def get_queryset(self):
        return Type.objects.all()
    

    
class LieuApiView(ModelViewSet):
    serializer_class = LieuSerializer

    def get_queryset(self):
        return Lieu.objects.all()

    def create(self, request, *args, **kwargs):
        lieuData = request.data
        newLieu = Lieu.objects.create(
            nom_lieu = lieuData['nom_lieu'],
            longitude = lieuData['longitude'],
            latitude = lieuData['latitude'],
            # image_1 = lieuData['image_1'],
            type = Type.objects.get(id=lieuData['type']),
            ville = Ville.objects.get(id=lieuData['ville'])
        )
        newLieu.save()
        serializer = LieuSerializer(newLieu)
        return Response(serializer.data)



class EvenementApiView(ModelViewSet):
    serializer_class = EvenementSerializer

    def get_queryset(self):
        return Evenement.objects.all()


    def create(self, request, *args, **kwargs):
        evenementData = request.data
        newEvenement = Evenement.objects.create(
            denomination = evenementData['denomination'],
            acteur = evenementData['acteur'],
            date = evenementData['date'],
            prix = evenementData['prix'],
            lieu = Lieu.objects.get(id=evenementData['lieu'])
        )
        newEvenement.save()
        serializer = VilleSerializer(newEvenement)
        return Response(serializer.data)

    

