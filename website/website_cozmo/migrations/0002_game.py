# Generated by Django 3.2.9 on 2022-01-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_cozmo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('file', models.FilePathField()),
            ],
            options={
                'db_table': 'game',
            },
        ),
    ]
