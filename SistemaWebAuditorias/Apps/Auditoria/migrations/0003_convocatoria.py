# Generated by Django 2.0 on 2019-11-21 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Auditoria', '0002_auto_20191120_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='convocatoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('auditoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auditoria.auditoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
