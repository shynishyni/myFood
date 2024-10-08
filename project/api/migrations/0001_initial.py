# Generated by Django 5.0.7 on 2024-09-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('quotes', models.JSONField()),
                ('step1', models.CharField(max_length=500, null=True)),
                ('step2', models.CharField(max_length=500, null=True)),
                ('step3', models.CharField(max_length=500, null=True)),
                ('step4', models.CharField(max_length=500, null=True)),
                ('step5', models.CharField(max_length=500, null=True)),
                ('step6', models.CharField(max_length=500, null=True)),
                ('step7', models.CharField(max_length=500, null=True)),
                ('step8', models.CharField(max_length=500, null=True)),
                ('step9', models.CharField(max_length=500, null=True)),
                ('step10', models.CharField(max_length=500, null=True)),
                ('ing1', models.CharField(max_length=500, null=True)),
                ('ing2', models.CharField(max_length=500, null=True)),
                ('ing3', models.CharField(max_length=500, null=True)),
                ('ing4', models.CharField(max_length=500, null=True)),
                ('ing5', models.CharField(max_length=500, null=True)),
                ('ing6', models.CharField(max_length=500, null=True)),
                ('ing7', models.CharField(max_length=500, null=True)),
                ('ing8', models.CharField(max_length=500, null=True)),
                ('ing9', models.CharField(max_length=500, null=True)),
                ('ing10', models.CharField(max_length=500, null=True)),
                ('ing11', models.CharField(max_length=500, null=True)),
                ('ing12', models.CharField(max_length=500, null=True)),
                ('ing13', models.CharField(max_length=500, null=True)),
                ('ing14', models.CharField(max_length=500, null=True)),
                ('ing15', models.CharField(max_length=500, null=True)),
                ('pic1', models.ImageField(upload_to='food_images/')),
                ('pic2', models.ImageField(upload_to='food_images/')),
            ],
        ),
    ]
