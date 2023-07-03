# Generated by Django 4.2.2 on 2023-07-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=20)),
                ('age', models.IntegerField()),
                ('cellphone', models.CharField(max_length=11, unique=True)),
                ('position', models.CharField(max_length=10, null=True)),
                ('salary', models.FloatField(null=True)),
            ],
        ),
    ]
