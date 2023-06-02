## Reference
[Getting Started with Celery Tutorial (10 min)](https://www.youtube.com/@prettyprinted)

## Instructions
- Install packages from **requirements.txt** in root directory
- Install DockerDesktop
1. Navigate inside **redisx2** directory
1. Execute `docker-compose up --build`
1. Open a new terminal
1. Execute `celery -A tasks worker --loglevel=info`
1. Open a new terminal
1. Execute `python3 queue-example.py`

*If everything went correctly, you should see the reversed string of "celery example" printed to your terminal after 5 seconds. If you receive a timeout error, something is wrong*

