# Generated by Django 5.1.7 on 2025-04-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_contentblock_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentblock',
            name='task_type',
            field=models.CharField(blank=True, choices=[('test', 'Тест'), ('match', 'Сопоставление'), ('compare', 'Сравнение'), ('fill', 'Заполнение пропусков'), ('creative', 'Творческое задание')], max_length=20),
        ),
    ]
