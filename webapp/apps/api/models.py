from django.db import models
from mew.core.models import BaseModel
from simple_history.models import HistoricalRecords


# class MyModel(BaseModel):
#     """
#     """
#     guid = models.CharField(max_length=255, unique=True)
#     status = models.CharField(max_length=255)
#
#     class Meta:
#         db_table = 'my_model'

#     history = HistoricalRecords(excluded_fields=['guid'])
