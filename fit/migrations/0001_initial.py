# Generated by Django 3.1.2 on 2020-10-07 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_steps', models.IntegerField(default=0)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fit.date')),
            ],
        ),
    ]
