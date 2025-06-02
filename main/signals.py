from django.db.models.signals import post_save
from django.dispatch import receiver
from .google_sheets import GoogleSheets_update
from .models import IT5_db, IT11_db, IT15_db, IT17_db

# Сигналы для IT5_db
@receiver(post_save, sender=IT5_db)
def update_google_sheets_it5_save(sender, instance, **kwargs):
    GoogleSheets_update(instance, "IT5")

# Сигналы для IT11_db
@receiver(post_save, sender=IT11_db)
def update_google_sheets_it11_save(sender, instance, **kwargs):
    GoogleSheets_update(instance, "IT11")

# Сигналы для IT15_db
@receiver(post_save, sender=IT15_db)
def update_google_sheets_it15_save(sender, instance, **kwargs):
    GoogleSheets_update(instance, "IT15")

# Сигналы для IT17_db
@receiver(post_save, sender=IT17_db)
def update_google_sheets_it17_save(sender, instance, **kwargs):
    GoogleSheets_update(instance, "IT17")