import speedtest
import csv
from datetime import datetime

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping_result = st.results.ping

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print result
    print(f"[{timestamp}]")
    print(f"Ping: {ping_result:.2f} ms")
    print(f"Download: {download_speed:.2f} Mbps")
    print(f"Upload: {upload_speed:.2f} Mbps")

    # Log to CSV
    with open("speed_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, ping_result, download_speed, upload_speed])

if __name__ == "__main__":
    test_internet_speed()

