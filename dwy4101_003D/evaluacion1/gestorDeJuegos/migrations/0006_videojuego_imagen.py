# Generated by Django 3.1.2 on 2020-11-09 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeJuegos', '0005_delete_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='videojuego',
            name='imagen',
            field=models.ImageField(null=True, upload_to='juegos'),
        ),
    ]
