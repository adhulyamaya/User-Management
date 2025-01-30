from django.db import models

# Create your models here.
import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    creator = models.ForeignKey(
        "main_admin.CustomUser", blank=True, related_name="creator_%(class)s_objects", on_delete=models.CASCADE)
    updater = models.ForeignKey("main_admin.CustomUser", blank=True, null=True,
                                related_name="updater_%(class)s_objects", on_delete=models.CASCADE) #creator and updater fields in your BaseModel are tied to CustomUser
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True