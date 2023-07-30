# Generated by Django 4.2.3 on 2023-07-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Este campo precisará estar marcado para a página ser exibida publicamente.'),
        ),
    ]
