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
            scheduler.add_job(
                sync_sources, "interval", minutes=1, next_run_time=datetime.now()
            )
            scheduler.start()
