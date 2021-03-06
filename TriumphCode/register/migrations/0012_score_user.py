# Generated by Django 2.0.2 on 2018-03-23 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0011_auto_20180316_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='score_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('competitionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.competitions')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
