# Generated by Django 3.2.5 on 2021-07-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('weather', models.CharField(max_length=50)),
            ],
        ),
    ]
