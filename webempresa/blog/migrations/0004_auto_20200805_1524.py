# Generated by Django 2.0.2 on 2020-08-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200805_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_posts', to='blog.Category', verbose_name='Categorias'),
        ),
    ]
