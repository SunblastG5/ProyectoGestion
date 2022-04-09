# Generated by Django 4.0.3 on 2022-04-02 01:31

import course.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='course.post')),
                ('due_datetime', models.DateTimeField()),
            ],
            bases=('course.post',),
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn_in_timestamp', models.DateTimeField(auto_now=True)),
                ('grade', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('file', models.FileField(blank=True, null=True, upload_to=course.models.homework_storage_path)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='course.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]