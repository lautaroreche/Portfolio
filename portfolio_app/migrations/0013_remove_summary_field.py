from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0010_project_image2_project_image3_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='summary',
        ),
    ]
