from django.core.management.base import BaseCommand
from calendar_sync.service import get_service

class Command(BaseCommand):
    help = 'Start watching Google Calendar for changes'

    def handle(self, *args, **options):
        service = get_service()
        # Your implementation for watching calendars
        self.stdout.write(self.style.SUCCESS('Successfully started watch')) 