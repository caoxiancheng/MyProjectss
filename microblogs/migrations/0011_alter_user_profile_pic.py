# Generated by Django 3.2 on 2022-03-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogs', '0010_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]