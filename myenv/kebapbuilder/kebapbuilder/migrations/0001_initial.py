# Generated by Django 4.1.7 on 2023-03-06 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='MainType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_type_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additionals', models.ManyToManyField(to='kebapbuilder.additional')),
                ('main_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kebapbuilder.maintype')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kebapbuilder.person')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kebapbuilder.type')),
            ],
        ),
    ]
