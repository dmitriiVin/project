import subprocess
import time

processes = []

def start_process():
    processes.append(subprocess.Popen("redis-server", shell=True))
    processes.append(subprocess.Popen("python3 manage.py runserver", shell=True))
    processes.append(subprocess.Popen("celery -A python_project beat --loglevel=info", shell=True))
    processes.append(subprocess.Popen("celery -A python_project worker --loglevel=DEBUG", shell=True))

def kill_process():
    for process in processes:
        process.terminate()
        process.wait(timeout=2)

if __name__ == "__main__":
    try:
        start_process()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        kill_process()