# Generated by Django 3.2.7 on 2021-09-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=50, verbose_name='Type'),
        ),
    ]
