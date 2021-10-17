from django.db import models




class Pays(models.Model):
    nom_pays = models.CharField(max_length=50)
    code_pays = models.CharField(max_length=10)


    def __str__(self):
        return self.code_pays



class Province(models.Model):
    nom_province = models.CharField(max_length=50)

    pays = models.ForeignKey(Pays, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom_province


class Ville(models.Model):
    nom_ville = models.CharField(max_length=50)
    image_ville = models.ImageField(upload_to=None, height_field=None, width_field=None, 
                max_length=None, blank=True, null=True)
    description_ville = models.TextField(blank=True, null=True)

    province = models.ForeignKey(Province, on_delete=models.CASCADE)


    def __str__(self):
        return self.nom_ville


class Type(models.Model):
    nom_type = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_type


class Lieu(models.Model):
    nom_lieu = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    latitude =  models.CharField(max_length=50)
    image_1 = models.ImageField(upload_to='media/', height_field=None, 
                width_field=None, max_length=None, blank=True, null=True)
    image_2 = models.ImageField(upload_to='media/', height_field=None, width_field=None, 
                max_length=None, blank=True, null=True)
    image_3 = models.ImageField(upload_to='media/', height_field=None, width_field=None, 
                max_length=None, blank=True, null=True)
    image_4 = models.ImageField(upload_to='media/', height_field=None, width_field=None, 
                max_length=None, blank=True, null=True)
    description_Lieu = models.TextField(blank=True, null=True)

    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)



    def __str__(self):
        return self.nom_lieu



class Evenement(models.Model):
    designation = models.CharField(max_length=150)
    acteur = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    prix = models.DecimalField(max_digits=5, decimal_places=2)

    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)


    def __str__(self):
        return self.designation



