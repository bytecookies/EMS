# Generated by Django 3.2.16 on 2022-12-21 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0003_howdidyougettoknowaboutintimasia_nationality_organization'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='howdidyougettoknowaboutintimasia',
            options={'verbose_name': 'How Did You Get To Know About INTIMASIA', 'verbose_name_plural': 'How Did You Get To Know About INTIMASIA'},
        ),
        migrations.AlterModelOptions(
            name='nationality',
            options={'verbose_name': 'Nationality', 'verbose_name_plural': 'Nationalities'},
        ),
        migrations.AlterModelOptions(
            name='natureofbusiness',
            options={'verbose_name': 'Nature Of Business', 'verbose_name_plural': 'Nature Of Business'},
        ),
        migrations.AlterModelOptions(
            name='productcatogory',
            options={'verbose_name': 'Product Catogory', 'verbose_name_plural': 'Product Categories'},
        ),
        migrations.AlterModelOptions(
            name='productsubcatogory',
            options={'verbose_name': 'Product Sub Catogory', 'verbose_name_plural': 'Product Sub Categories'},
        ),
    ]
