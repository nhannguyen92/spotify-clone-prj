# Generated by Django 4.2.20 on 2025-05-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_usercreatedalbum_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('listener', 'Listener'), ('artist', 'Artist')], default='listener', max_length=20),
        ),
    ]
