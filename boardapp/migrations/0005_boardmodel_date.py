# Generated by Django 3.2.3 on 2021-07-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0004_alter_boardmodel_readtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
