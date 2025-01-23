import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(help_text='Укажите место действия', max_length=250, verbose_name='Место действия')),
                ('time_action', models.TimeField(help_text='Укажите время действия', verbose_name='Время действия')),
                ('action', models.CharField(help_text='Укажите действие', max_length=250, verbose_name='Действие')),
                ('is_nice', models.BooleanField(blank=True, default=False, help_text='Укажите признак приятной привычки', null=True, verbose_name='Признак приятной привычки')),
                ('frequency', models.IntegerField(default=7, help_text='Укажите периодичность привычки', verbose_name='Периодичность')),
                ('remuneration', models.CharField(blank=True, help_text='Укажите вознаграждение', max_length=250, null=True, verbose_name='Вознаграждение')),
                ('lead_time', models.PositiveIntegerField(default=120, help_text='Укажите время на выполнение', verbose_name='Время на выполнение')),
                ('is_published', models.BooleanField(blank=True, default=False, help_text='Укажите признак публичности', null=True, verbose_name='Признак публичности')),
                ('owner', models.ForeignKey(blank=True, help_text='Укажите владельца привычки', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец привычки')),
                ('related_habit', models.ForeignKey(blank=True, help_text='Укажите связанную привычку', null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]