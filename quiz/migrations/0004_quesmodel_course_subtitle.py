# Generated by Django 4.1.3 on 2024-01-11 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_sub_category_image_upload'),
        ('quiz', '0003_quesmodel_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='course_subtitle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.sub_category'),
        ),
    ]
