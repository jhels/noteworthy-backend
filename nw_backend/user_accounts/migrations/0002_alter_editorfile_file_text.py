# Generated by Django 4.2.4 on 2023-08-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorfile',
            name='file_text',
            field=models.TextField(help_text='Text stored in file', max_length=25000),
        ),
    ]
