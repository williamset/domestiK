# Generated by Django 5.0.4 on 2024-05-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0003_remove_foyer_member_foyer_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='foyer',
            name='admin',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
