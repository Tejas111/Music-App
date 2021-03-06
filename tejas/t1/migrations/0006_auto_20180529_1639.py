# Generated by Django 2.0.5 on 2018-05-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t1', '0005_song_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.CharField(default='Some', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.CharField(default='Some', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='song_title',
            field=models.CharField(default='Some', max_length=250),
            preserve_default=False,
        ),
    ]
