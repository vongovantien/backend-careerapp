# Generated by Django 4.0 on 2021-12-29 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careerapp', '0012_candidate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='bang_cap',
            new_name='degree',
        ),
    ]