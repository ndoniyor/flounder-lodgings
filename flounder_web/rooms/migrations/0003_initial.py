# Generated by Django 4.1.1 on 2022-09-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0002_delete_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('bed_count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.TextField()),
                ('checkout_time', models.DateField()),
            ],
        ),
    ]
