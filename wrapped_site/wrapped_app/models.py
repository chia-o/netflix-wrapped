# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Titles(models.Model):
    title_id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titles'

    def __str__(self):
        return self.title


class ViewingActivity(models.Model):
    profile_name = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    video_type = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    latest_bookmark = models.CharField(max_length=255, blank=True, null=True)
    title_id = models.ForeignKey(Titles, on_delete=models.CASCADE, db_column='title_id', blank=True, null=True)
    session_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'viewing_activity'

    def __str__(self):
        return self.title
