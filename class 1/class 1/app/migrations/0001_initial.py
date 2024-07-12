# Generated by Django 4.0.6 on 2022-12-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('discription', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('electronics', 'electronics'), ('kichenware', 'kichenware'), ('clothes', 'clothes')], max_length=30)),
            ],
        ),
    ]