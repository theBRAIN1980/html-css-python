# Generated by Django 3.2 on 2021-04-28 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('created',)},
        ),
    ]