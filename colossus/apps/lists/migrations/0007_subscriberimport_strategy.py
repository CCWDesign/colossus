# Generated by Django 2.1 on 2018-08-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20180805_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriberimport',
            name='strategy',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Create only. Ignore existing emails.'), (2, 'Update only. Ignore non-existing emails.'), (3, 'Update or create.')], default=3, help_text='The email address will be used as the main subscriber identifier. Select the strategy you want to use to import subscribers to the list. "Create only" means emails that are already present in the list (subscribed or any other status) will be completely ignored and remain unchanged. On the other hand, if you select "Update only", the import action will only have effect on subscribers that are already in the list, updating the fields accordingly to the CSV file. Finally, the "Update or create" will update existing subscribers, and if the email is not part of the list, a new subscriber record will be created.', verbose_name='import strategy'),
        ),
    ]
