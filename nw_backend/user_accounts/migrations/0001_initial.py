# Generated by Django 4.2.4 on 2023-08-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EditorFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of file', max_length=50)),
                ('file_text', models.TextField(help_text='Text stored in file')),
                ('date_created', models.DateTimeField()),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]