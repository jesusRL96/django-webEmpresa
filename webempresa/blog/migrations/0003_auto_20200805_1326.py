# Generated by Django 2.0.2 on 2020-08-05 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200803_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nombre',
            new_name='name',
        ),
    ]
