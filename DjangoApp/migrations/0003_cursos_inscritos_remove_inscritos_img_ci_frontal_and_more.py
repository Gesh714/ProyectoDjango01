# Generated by Django 4.2.7 on 2023-11-29 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0002_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos_inscritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=200)),
                ('id_sence', models.IntegerField()),
                ('comuna', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('fecha_inicio', models.CharField(max_length=10)),
                ('fecha_termino', models.CharField(max_length=10)),
                ('modalidad', models.CharField(blank=True, choices=[('Presencial', 'Presencial'), ('e-learning', 'E-Learning')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='inscritos',
            name='img_ci_frontal',
        ),
        migrations.RemoveField(
            model_name='inscritos',
            name='img_ci_posterior',
        ),
        migrations.AddField(
            model_name='inscritos',
            name='img_field_frontal',
            field=models.FileField(default='', error_messages='Sobrescribiendo', upload_to='', verbose_name='Imagen frontal del CI'),
        ),
        migrations.AddField(
            model_name='inscritos',
            name='img_field_posterior',
            field=models.FileField(default='', error_messages='Sobrescribiendo', upload_to='', verbose_name='Imagen posterior del CI'),
        ),
        migrations.AlterField(
            model_name='inscritos',
            name='rsh',
            field=models.FileField(default='', error_messages='Sobrescribiendo', upload_to='', verbose_name='Registro social de hogares'),
        ),
    ]
