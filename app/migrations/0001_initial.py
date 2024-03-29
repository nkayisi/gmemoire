# Generated by Django 3.2.7 on 2021-09-11 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_pays', models.CharField(max_length=50)),
                ('code_pays', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_province', models.CharField(max_length=50)),
                ('pays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pays')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ville', models.CharField(max_length=50)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.province')),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_lieu', models.CharField(max_length=50)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('image_1', models.ImageField(upload_to=None)),
                ('image_2', models.ImageField(upload_to=None)),
                ('image_3', models.ImageField(upload_to=None)),
                ('image_4', models.ImageField(upload_to=None)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.type')),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ville')),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=150)),
                ('acteur', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lieu')),
            ],
        ),
    ]
