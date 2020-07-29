# Generated by Django 2.2 on 2020-07-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200723_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, 'Python'), (1, 'Java'), (2, 'Javascript'), (3, 'Linux'), (4, 'Css'), (5, 'Html'), (6, 'React'), (7, 'Devops')], null=True)),
            ],
            options={
                'verbose_name': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='blog', to='blog.Category', verbose_name='Category'),
        ),
    ]
