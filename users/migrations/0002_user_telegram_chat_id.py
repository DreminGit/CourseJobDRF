from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="telegram_chat_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Telegram Chat ID"
            ),
        ),
    ]