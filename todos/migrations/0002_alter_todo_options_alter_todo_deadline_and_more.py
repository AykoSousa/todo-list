# Generated by Django 4.2.7 on 2023-11-02 23:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"ordering": ["deadline"]},
        ),
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(verbose_name="Data de Entrega"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Titulo"),
        ),
    ]
