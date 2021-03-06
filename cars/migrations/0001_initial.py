# Generated by Django 3.2.9 on 2021-11-19 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(blank=True, max_length=150)),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=150, verbose_name='brand nomi: ')),
                ('model', models.CharField(max_length=150)),
                ('color', models.CharField(choices=[('1', 'oq'), ('2', 'qora'), ('3', 'kok'), ('4', 'Boshqa')], max_length=150, verbose_name='Rangi: ')),
                ('bodyType', models.CharField(blank=True, max_length=150, verbose_name='Kuzov turi')),
                ('transmission', models.CharField(blank=True, max_length=150, verbose_name='Uzatmalar qutisi')),
                ('condition', models.CharField(choices=[('1', 'Yangi'), ('2', 'Eski'), ('3', 'Ortacha'), ('4', 'Ishlatip olsa boladi'), ('5', 'Vashee Zor')], max_length=150, verbose_name='Avtomobil holati')),
                ('year', models.IntegerField(default=1800, verbose_name='Ishlap shiqarilgan yili: ')),
                ('mileage', models.CharField(max_length=150, verbose_name='Yurgan masofasi')),
                ('price', models.IntegerField(verbose_name='Narxi: ')),
                ('description', models.TextField(blank=True, help_text='Metan bor bir bola..', max_length=500, verbose_name='Qoshimcha malumot')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('image', models.ImageField(upload_to='media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.categorytransport', verbose_name='Transport Turi')),
            ],
        ),
    ]
