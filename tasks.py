from app import celery

@celery.task()
def someFunction():
    print ("This is a function called from celery beat")
    return 9

