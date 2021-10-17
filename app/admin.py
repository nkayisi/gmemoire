from django.contrib import admin


from .models import *



admin.site.register(Pays);
admin.site.register(Province);
admin.site.register(Ville);
admin.site.register(Lieu);
admin.site.register(Type);
admin.site.register(Evenement);
