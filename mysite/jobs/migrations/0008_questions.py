# Generated by Django 2.2 on 2019-09-06 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20190906_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=1000)),
            ],
        ),
    ]
