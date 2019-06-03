# Generated by Django 2.2.1 on 2019-06-01 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190601_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('status', models.CharField(choices=[('visible', 'Visible'), ('hidden', 'Hidden'), ('moderated', 'Moderated')], default='visible', max_length=20)),
                ('moderation_text', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post')),
            ],
        ),
    ]
