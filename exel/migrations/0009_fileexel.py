# Generated by Django 3.2.3 on 2021-05-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exel', '0008_alter_brief_terms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fileexel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.FileField(upload_to='')),
            ],
        ),
    ]
