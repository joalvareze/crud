# Generated by Django 5.0.6 on 2024-07-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_games_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='games/'),
        ),
    ]