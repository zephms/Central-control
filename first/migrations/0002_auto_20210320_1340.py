# Generated by Django 3.1.7 on 2021-03-20 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='desc',
            field=models.TextField(default='Null'),
        ),
        migrations.AlterField(
            model_name='auth',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='auth',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
