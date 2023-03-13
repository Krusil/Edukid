# Generated by Django 4.1.4 on 2023-01-13 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_active_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type_of_user',
            field=models.CharField(choices=[('pupil', 'Ученик'), ('teacher', 'Учитель'), ('parent', 'Родитель')], max_length=8, verbose_name='Роль'),
        ),
    ]