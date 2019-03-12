# Generated by Django 2.1.1 on 2018-11-02 18:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=120)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('amount', models.IntegerField()),
                ('deadline', models.DateTimeField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]