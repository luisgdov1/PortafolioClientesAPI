# Generated by Django 4.0.3 on 2022-03-19 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Cliente', models.CharField(max_length=255)),
                ('direccion_Cliente', models.CharField(max_length=255)),
                ('email_Cliente', models.CharField(max_length=255)),
                ('telefono_Cliente', models.IntegerField()),
            ],
        ),
    ]