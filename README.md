# Docker Multi-Container Setup (PHP, Python, MySQL, Adminer, Nginx, Scheduler, Telegram Bot)

This project sets up a **multi-container environment** using **Docker Compose** for running PHP, Python, MySQL, Adminer, Nginx, a Python Scheduler, and a Telegram Bot for notifications. The containers are configured to share a **single MySQL database** and use Nginx as a reverse proxy.

## **Project Structure**

```
.
├── docker-compose.yml
├── conf.d/
│   ├── default.conf
├── web/
├── app/
│   ├── app.py
├── mysql/
│   ├── data/
│   ├── init.sql
├── scheduler/
│   ├── myscript.py
├── telegram/
│   ├── telegram_bot.py
├── adminer/
├── cronjob
├── requirements.txt
├── Dockerfile.php
├── Dockerfile.python
├── Dockerfile.scheduler
├── .env
└── README.md
```

---

## **1. Prerequisites**

Ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## **2. Setup & Configuration**

### **Step 1: Clone the Repository**

```sh
git clone https://github.com/your-repo/multi-container-docker.git
cd multi-container-docker
```

### **Step 2: Set Environment Variables**

Create a `.env` file and configure credentials:

```sh
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=mydatabase
MYSQL_USER=user
MYSQL_PASSWORD=password

TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## **3. Running the Containers**

Run the following command to build and start the services:

```sh
docker-compose up --build -d
```

To check running containers:

```sh
docker ps
```

To stop the containers:

```sh
docker-compose down
```

---

## **4. Accessing Services**

- **PHP Application**: [http://local.one](http://php.one)
- **Python Application**: [http://python.one](http://python.one)
- **Adminer (MySQL GUI)**: [http://adminer.one](http://adminer.one)

To test MySQL connection:

```sh
docker exec -it mysql_container mysql -uuser -ppassword mydatabase
```

---

## **5. Scheduler Container (Cron Jobs for Python Scripts)**

A `scheduler` service is included to run scheduled Python jobs using **cron**.

### **Adding Scheduled Jobs**

The schedule is defined in the `cronjob` file inside the `scheduler/` directory. Example:

```cron
# Run myscript.py every day at 2 AM
0 2 * * * root python3 /app/myscript.py >> /app/cron.log 2>&1
```

### **Checking Scheduler Logs**

To check if the scheduled job ran successfully:

```sh
docker exec -it scheduler_container cat /app/cron.log
```

To manually trigger the script for testing:

```sh
docker exec -it scheduler_container python3 /app/myscript.py
```

---

## **6. Telegram Bot for Notifications**

A `telegram` service is included to send messages to a Telegram channel when a scheduled job completes.

### **Creating a Telegram Bot**

1. Open Telegram and search for **BotFather**.
2. Start a chat and send `/newbot`.
3. Follow the instructions and copy the **Bot Token**.
4. Add your bot to a **Telegram Channel** and make it an **admin**.
5. Add the bot token and chat ID to the `.env` file.

### **Modifying the Scheduled Job to Notify Telegram**

The `scheduler/myscript.py` script sends a Telegram message when the job completes:

```python
import datetime
import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)

def main():
    log_message = f"Scheduled Job ran at {datetime.datetime.now()}"

    # Log locally
    with open("/app/cron.log", "a") as log:
        log.write(log_message + "\n")

    # Send Telegram notification
    send_telegram_message(log_message)

if __name__ == "__main__":
    main()
```

---

## **7. Troubleshooting**

### **1. Nginx Shows "502 Bad Gateway"?**

Run the following:

```sh
docker logs nginx_container
```

If you see **"Connection refused"**, check if the service is running:

```sh
docker ps
```

Then, restart the containers:

```sh
docker-compose restart
```

### **2. Checking Telegram Bot Logs**

To check if the Telegram bot is running and sending messages:

```sh
docker logs telegram_bot_container
```

To manually trigger a Telegram message:

```sh
docker exec -it telegram_bot_container python /telegram/telegram_bot.py
```

---

## **8. Stopping & Cleaning Up**

To stop all containers:

```sh
docker-compose down
```

To remove all containers and networks:

```sh
docker-compose down --volumes --remove-orphans
```

---

## **9. Extending the Setup**

- Add **additional services** (Redis, Node.js, etc.).
- Configure **SSL/TLS** using Let's Encrypt.
- Implement **Docker Swarm** or **Kubernetes** for scalability.

---

## **10. License**

This project is licensed under the **MIT License**.

