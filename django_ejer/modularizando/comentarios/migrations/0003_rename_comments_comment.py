# Generated by Django 4.1 on 2022-08-16 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_rename_data_comment_comments_date_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
