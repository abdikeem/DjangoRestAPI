# Generated by Django 3.2.8 on 2021-10-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=10)),
                ('l_name', models.CharField(max_length=10)),
                ('emp_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
