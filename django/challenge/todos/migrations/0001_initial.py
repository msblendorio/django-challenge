# Generated by Django 4.1.5 on 2023-01-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('order', models.IntegerField()),
                ('description', models.TextField()),
                ('is_completed', models.BooleanField(default=True)),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)),
            ],
        ),
    ]
