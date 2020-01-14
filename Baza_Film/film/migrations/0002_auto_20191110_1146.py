# Generated by Django 2.2.7 on 2019-11-10 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='film.Genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='starring',
            field=models.ManyToManyField(related_name='PersonMovie', to='film.Person'),
        ),
    ]
