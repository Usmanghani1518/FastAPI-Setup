from __future__  import annotations
from tortoise import fields
from tortoise.models import Model


class Code(Model):
    id = fields.IntField(primary_key=True)
    type = fields.CharField(max_length=64)
    value = fields.CharField(max_length=32)
    expires_at = fields.DatetimeField()

    user: fields.ForeignKeyRelation["Users"] = fields.ForeignKeyField(
        "models.Users",
        related_name="codes",
        on_delete=fields.CASCADE,
    )

    created_at = fields.DatetimeField(auto_now_add=True)

