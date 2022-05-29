# Generated by Django 4.0 on 2021-12-29 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('careerapp', '0015_alter_user_user_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='id',
        ),
        migrations.AddField(
            model_name='candidate',
            name='user',
            field=models.OneToOneField(default=-1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='careerapp.user'),
            preserve_default=False,
        ),
    ]