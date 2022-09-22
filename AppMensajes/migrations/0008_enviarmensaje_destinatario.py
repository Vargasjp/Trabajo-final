# Generated by Django 4.1 on 2022-09-22 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppMensajes', '0007_rename_lastname_enviarmensaje_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enviarmensaje',
            name='destinatario',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
