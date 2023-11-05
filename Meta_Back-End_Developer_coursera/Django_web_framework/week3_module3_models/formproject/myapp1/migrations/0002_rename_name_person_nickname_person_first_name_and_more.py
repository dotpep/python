# Generated by Django 4.2.6 on 2023-11-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='nickname',
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]