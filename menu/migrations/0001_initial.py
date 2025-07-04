# Generated by Django 4.2.23 on 2025-06-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.IntegerField(choices=[(0, 'Starter'), (1, 'Main'), (2, 'Dessert'), (3, 'Drink')], default=0)),
                ('price', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['type', 'name'],
            },
        ),
    ]
