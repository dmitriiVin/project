from django.db import models

class CalendarSyncState(models.Model):
    key = models.CharField(max_length=255, primary_key=True)
    sync_token = models.TextField(null=True, blank=True)
    last_synced = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Calendar sync state: {self.key}" 