# Generated by Django 2.0.6 on 2018-08-08 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('status', models.IntegerField(choices=[(1, 'Em avaliação'), (2, 'Aprovado'), (3, 'Necessita de correções'), (4, 'Não aprovado')], default=1, verbose_name='Status')),
                ('local', models.CharField(max_length=100, verbose_name='Local')),
                ('bio_author', models.TextField(verbose_name='Descrição do Autor')),
                ('start_date', models.DateField(verbose_name='Data de Início')),
                ('end_date', models.DateField(verbose_name='Data Final')),
                ('registration_date', models.DateField(verbose_name='Data de Registro')),
                ('workload', models.TimeField(default=0, verbose_name='Carga Horária')),
                ('education', models.CharField(max_length=100, verbose_name='Formação')),
                ('degree', models.CharField(max_length=100, verbose_name='Titulação')),
                ('vacancies', models.PositiveIntegerField(verbose_name='Vagas')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Inscrito'), (2, 'Presente'), (3, 'Ausente')], default=1)),
                ('role', models.IntegerField(choices=[(1, 'Ouvinte'), (2, 'Ministrante')], default=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('event', 'user')},
        ),
    ]
