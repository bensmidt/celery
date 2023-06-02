from tasks import reverse 

result = reverse.delay('hello world')
print(result.get(timeout=10))