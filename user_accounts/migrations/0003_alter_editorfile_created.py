# Generated by Django 4.2.7 on 2024-03-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0002_remove_editorfile_file_text_editorfile_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorfile',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
