# Generated by Django 2.2.4 on 2020-01-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Honbab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='honbab',
            name='img',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
