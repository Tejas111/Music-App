# Generated by Django 2.0.5 on 2018-05-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t1', '0006_auto_20180529_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
