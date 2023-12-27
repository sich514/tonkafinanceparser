import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime


def parse_percentage(html):
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find('p', {'data-v-e93e1a22': '', 'class': 'fs14 fw500 lh24'})
    if element:
        return float(element.text.replace('%', '').strip())
    return None


def main():
    url = 'https://www.tonka.finance/fairlaunch'
    target_percentage = 100.0
    update_interval = 5  # seconds
    start_time = datetime.now()

    while True:
        current_time = datetime.now()
        elapsed_time = current_time - start_time
        print(f"Time elapsed: {elapsed_time}")

        response = requests.get(url)
        if response.status_code == 200:
            percentage = parse_percentage(response.text)
            if percentage is not None:
                print(f"Current percentage: {percentage}%")

                if percentage >= target_percentage:
                    print(f"Target percentage reached! Time elapsed: {elapsed_time}")
                    break
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")

        time.sleep(update_interval)


if __name__ == "__main__":
    # Set the desired start time (replace with your specific time)
    scheduled_start_time = datetime(2023, 12, 28, 4, 0, 0)

    # Calculate the delay until the scheduled start time
    current_time = datetime.now()
    delay = (scheduled_start_time - current_time).total_seconds()

    if delay > 0:
        print(f"Waiting for {delay} seconds until the scheduled start time...")
        time.sleep(delay)

    main()
