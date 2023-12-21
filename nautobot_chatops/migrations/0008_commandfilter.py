# Generated by Django 3.2.21 on 2023-10-25 16:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0098_rename_data_jobresult_result"),
        ("dcim", "0049_remove_slugs_and_change_device_primary_ip_fields"),
        ("nautobot_chatops", "0007_account_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommandFilter",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("command", models.CharField(max_length=200)),
                ("device_role", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="extras.role")),
                ("platform", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="dcim.platform")),
            ],
            options={
                "ordering": ["command", "device_role", "platform"],
            },
        ),
    ]
