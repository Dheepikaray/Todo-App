# Generated by Django 4.2.6 on 2023-10-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(default=13),
            preserve_default=False,
        ),
    ]
