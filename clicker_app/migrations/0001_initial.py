# Generated by Django 2.2.17 on 2021-03-14 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Upgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('cost', models.IntegerField(default=6969)),
                ('effect', models.IntegerField(default=1)),
                ('auto_click', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OwnsUpgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clicker_app.Account')),
                ('upgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clicker_app.Upgrade')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='achievements',
            field=models.ManyToManyField(to='clicker_app.Achievement'),
        ),
        migrations.AddField(
            model_name='account',
            name='upgrades',
            field=models.ManyToManyField(through='clicker_app.OwnsUpgrade', to='clicker_app.Upgrade'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]