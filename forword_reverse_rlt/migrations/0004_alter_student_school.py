# Generated by Django 4.1.2 on 2023-02-18 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forword_reverse_rlt', '0003_alter_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='forword_reverse_rlt.school'),
        ),
    ]
