import os

TEMPORAL_TASK_QUEUE = os.getenv("TEMPORAL_TASK_QUEUE", "no-sendbox-python-django")
TEMPORAL_SCHEDULER_HOST = os.getenv("TEMPORAL_SCHEDULER_HOST", "127.0.0.1")
TEMPORAL_SCHEDULER_PORT = os.getenv("TEMPORAL_SCHEDULER_PORT", "7233")
