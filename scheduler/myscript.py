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
