# Generated by Django 4.2.7 on 2023-11-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0003_rename_password1_resgister_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
