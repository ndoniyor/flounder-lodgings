# Generated by Django 4.1.1 on 2022-09-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.TextField(),
        ),
    ]
