from django.db import models
from backend.settings import LOCAL_FILE_DIR


class FetchFile(models.Model):
    id = models.BigAutoField(primary_key=True)

    file = models.FilePathField(path=LOCAL_FILE_DIR)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()
