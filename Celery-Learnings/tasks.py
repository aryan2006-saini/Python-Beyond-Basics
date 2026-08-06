from celery import Celery
from time import sleep

app = Celery("tasks", broker="redis://localhost:6379", backend="redis://localhost:6379")

@app.task
def process(x,y):
    i = 0
    while i<5:
        sleep(1)
        i+=1
        print("processing...")

    return x**2+y**2

# celery -A tasks worker -l info

## Open 2-terminal tabs and in first terminal run -> python -i tasks.py and in second -> celery -A tasks worker -P solo -l info
## Now in first tab -> process.delay(2,3)