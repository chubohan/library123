# Generated by Django 4.2.6 on 2023-10-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_remove_post_publishing'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publishing',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
