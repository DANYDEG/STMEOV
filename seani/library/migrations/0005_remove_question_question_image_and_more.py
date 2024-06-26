# Generated by Django 5.0.2 on 2024-06-04 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_question_question_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_image',
        ),
        migrations.AlterField(
            model_name='question',
            name='answer1',
            field=models.CharField(default='Me interesa', max_length=200, verbose_name='Respuesta A'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer2',
            field=models.CharField(default='No me interesa', max_length=200, verbose_name='Respuesta B'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct',
            field=models.CharField(default='A', max_length=5, verbose_name='Respuesta Correcta'),
        ),
    ]
