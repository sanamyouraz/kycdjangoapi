# Generated by Django 3.2.19 on 2023-06-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('province', models.CharField(choices=[('Pradesh No.1', 'Pradesh No.1'), ('Pradesh No.2', 'Pradesh No.2'), ('Pradesh No.3', 'Pradesh No.3'), ('Pradesh No.4', 'Pradesh No.4'), ('Pradesh No.5', 'Pradesh No.5')], max_length=50)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pimage', models.ImageField(blank=True, upload_to='pimages')),
                ('rdoc', models.FileField(blank=True, upload_to='rdocs')),
            ],
        ),
    ]
