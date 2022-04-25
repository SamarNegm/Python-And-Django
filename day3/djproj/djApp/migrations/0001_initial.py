# Generated by Django 4.0.4 on 2022-04-22 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40, null=True)),
                ('lname', models.CharField(default='noName', max_length=40)),
                ('age', models.ImageField(upload_to='')),
                ('std_track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djApp.track')),
            ],
        ),
    ]