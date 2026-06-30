# HouseHold service app 

This is my MAD2 BOOTCAMP project



# For Mailhog use commands from GSPACE 

# go to Backend (make sure the virtual env is activated)
1. run python app 
    ```bash
    python3 app.py
    ```
2. Install celery and Redis
    ```bash
    pip install celery[Redis]
    ```
3. Run radis server

    ```bash
    redis-server
    ```
* if this says . already listining on port 6379.
* run 
    ```bash
    sudo lsof -i :6379
    ```
* check the process id and run 
    ```bash
    sudo kill <pid>
    ```
* then retry 
    ```bash
    redis-server
    ```
* if still give same error 
    ```bash
    sudo systemctl stop redis
    ```
* then again try - this will definatly run the redis
    ```bash
    redis-server
    ```

4. Open new terminal to run celery worker

    ```bash
    celery -A app.celery worker --loglevel INFO
    ```
5. Open new terminal to run celery beat

    ```bash
    celery -A app.celery beat --loglevel INFO
    ```
6. Open new terminal to run mailhost

    ```bash
    MailHog
    ```

