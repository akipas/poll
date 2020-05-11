# Generated by Django 3.0.5 on 2020-05-04 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_moteur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('moteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Moteur')),
            ],
        ),
    ]