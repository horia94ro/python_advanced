# Generated by Django 3.2.3 on 2021-05-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('continut', models.TextField()),
                ('data_publicare', models.DateField()),
            ],
        ),
    ]
