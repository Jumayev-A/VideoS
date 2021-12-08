# Generated by Django 4.0 on 2021-12-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
    ]
