from django.forms import ModelForm

from .models import *



class PaysForm(ModelForm):
    class Meta:
        model = Pays
        fields = '__all__'



class ProvinceForm(ModelForm):
    class Meta:
        model = Province
        # fields = ['nom_province']
        fields = '__all__'



class VilleForm(ModelForm):
    class Meta:
        model = Ville
        # fields = ['nom_ville']
        fields = '__all__'


class TypeForm(ModelForm):
    class Meta:
        model = Type
        # fields = ['nom_type']
        fields = '__all__'


class LieuForm(ModelForm):
    class Meta:
        model = Lieu
        # fields = ['nom_ville']
        fields = '__all__'



class EvenementForm(ModelForm):
    class Meta:
        model = Evenement
        # fields = ['nom_ville']
        fields = '__all__'