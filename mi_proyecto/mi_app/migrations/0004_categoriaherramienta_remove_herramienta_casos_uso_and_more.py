# Generated by Django 5.1.3 on 2024-12-01 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0003_noticia_autor_noticia_imagen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaHerramienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='herramienta',
            name='casos_uso',
        ),
        migrations.RemoveField(
            model_name='herramienta',
            name='enlace_descarga',
        ),
        migrations.AddField(
            model_name='herramienta',
            name='enlace',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='herramientas/'),
        ),
        migrations.AlterField(
            model_name='herramienta',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='herramienta',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.categoriaherramienta'),
        ),
    ]
