# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime

class ViewingActivity(models.Model):
    profile_name = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.DateTimeField(default=datetime.datetime.now)
    duration = models.TimeField(default=datetime.time(0, 0))
    title = models.CharField(max_length=255, blank=True, null=True)
    video_type = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, null=True, default=None)
    latest_bookmark = models.CharField(max_length=255, blank=True, null=True)
    session_id = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'viewing_activity'

    def __str__(self):
        return self.title
