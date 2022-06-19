# Generated by Django 4.0.4 on 2022-06-19 07:32

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
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood_name', models.CharField(max_length=30)),
                ('neighbourhood_location', models.CharField(max_length=30)),
                ('occupants_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('photo', models.ImageField(blank=True, upload_to='profile/')),
                ('profile_email', models.EmailField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('neighbourhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourapp.neighbourhood')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourapp.neighbourhood')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='neighbourapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('business_email', models.EmailField(max_length=100)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourapp.neighbourhood')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourapp.profile')),
            ],
        ),
    ]
