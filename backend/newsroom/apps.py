from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig

scheduler = BackgroundScheduler()


class NewsroomConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "newsroom"

    def ready(self):
        from .jobs import sync_sources

        if not scheduler.running:
            # run once just at startup
            scheduler.add_job(sync_sources, "date", run_date=datetime.now())
            scheduler.start()
