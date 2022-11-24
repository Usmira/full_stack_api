# Generated by Django 4.0.4 on 2022-11-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aliments',
            fields=[
                ('id_aliment', models.IntegerField(primary_key=True, serialize=False)),
                ('Category', models.CharField(max_length=100)),
                ('FoodItem', models.CharField(max_length=100)),
                ('Quantite_en_ml_or_g', models.FloatField()),
                ('calorie_en_cal_per_ml_or_g', models.FloatField()),
                ('kJ_per_ml_or_g', models.FloatField()),
            ],
        ),
    ]