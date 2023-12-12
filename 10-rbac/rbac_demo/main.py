import os
import requests
from kubernetes import client, config
from dotenv import load_dotenv
import time
from datetime import datetime, timedelta

load_dotenv()

# Slack Webhook URL
SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']

# Kubernetes Namespace and Pod Threshold
NAMESPACE = os.environ['NAMESPACE']
POD_THRESHOLD = int(os.environ['POD_THRESHOLD'])


def send_slack_message(message):
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    return response.status_code


def should_notify(last_notification_time: datetime) -> bool:
    """Returns True if the last notification was sent more than 5 minutes ago."""
    if last_notification_time is None:
        return True
    else:
        return datetime.now() > last_notification_time + timedelta(minutes=5)

def main():
    last_notification_sent = None
    while True:
        config.load_incluster_config()
        v1 = client.CoreV1Api()
        pods = v1.list_namespaced_pod(NAMESPACE)
        pod_count = len(pods.items)

        if pod_count > POD_THRESHOLD:
            message = f"Number of pods in {NAMESPACE} has exceeded {POD_THRESHOLD}. Current count: {pod_count}"
            if should_notify(last_notification_sent):
                send_slack_message(message)
                last_notification_sent = datetime.now()
        
        time.sleep(10)

if __name__ == '__main__':
    main()
