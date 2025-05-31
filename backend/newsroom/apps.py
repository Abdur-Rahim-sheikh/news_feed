from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig

scheduler = BackgroundScheduler()


class NewsroomConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "newsroom"

    def ready(self):
        from .jobs import sync_news, sync_sources

        if not scheduler.running:
            # run once just at startup
            app_start = datetime.now()
            scheduler.add_job(sync_sources, "date", run_date=app_start)
            scheduler.add_job(
                sync_news,
                "interval",
                minutes=10,
                next_run_time=app_start + timedelta(seconds=2),
            )

            scheduler.start()
