from tasks import reverse 

result = reverse.delay('celery example')
print(result.get(timeout=10))