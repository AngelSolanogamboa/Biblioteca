# Generated by Django 5.2 on 2025-05-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_libro_disponible'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='leido',
            field=models.BooleanField(default=False),
        ),
    ]
