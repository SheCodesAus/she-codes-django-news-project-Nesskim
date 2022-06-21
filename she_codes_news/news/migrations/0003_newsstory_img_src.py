from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsstory_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='img_src',
            field=models.CharField(default='string:image source', max_length=200),
        ),
    ]