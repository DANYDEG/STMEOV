# Generated by Django 5.0.2 on 2024-03-05 18:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_stage_application_date_exam_exammodule_and_more'),
        ('library', '0004_alter_question_question_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'examen', 'verbose_name_plural': 'examenes'},
        ),
        migrations.AddField(
            model_name='exam',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
        migrations.CreateModel(
            name='Breakdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(default='-', max_length=5, verbose_name=' Respuesta')),
                ('correct', models.CharField(default='-', max_length=5, verbose_name='Respuesta correcta')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam', verbose_name='Pregunta')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.question', verbose_name='Pregunta')),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(through='exam.Breakdown', to='library.question', verbose_name='Preguntas'),
        ),
    ]