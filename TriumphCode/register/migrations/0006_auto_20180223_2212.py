# Generated by Django 2.0.2 on 2018-02-23 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_problems_ptag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problems',
            old_name='pcode',
            new_name='psolution',
        ),
    ]