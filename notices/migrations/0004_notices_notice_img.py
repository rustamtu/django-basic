# Generated by Django 4.2.4 on 2023-09-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0003_alter_notices_notice_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='notices',
            name='notice_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='notices/'),
        ),
    ]
