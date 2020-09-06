# Generated by Django 3.0.8 on 2020-09-05 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='username',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]