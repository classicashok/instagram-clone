# Generated by Django 2.2 on 2019-12-18 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('photo', models.ImageField(upload_to='profile_pic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.UserModel')),
            ],
        ),
    ]
