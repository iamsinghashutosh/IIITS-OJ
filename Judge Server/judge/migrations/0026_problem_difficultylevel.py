# Generated by Django 3.0.4 on 2020-04-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0025_auto_20200401_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='difficultylevel',
            field=models.IntegerField(default=1, verbose_name='default=1'),
            preserve_default=False,
        ),
    ]
