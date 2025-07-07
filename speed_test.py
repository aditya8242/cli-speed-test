import speedtest
import csv
import os
from datetime import datetime

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    ping_result = st.results.ping

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # CLI Output
    print(f"[{timestamp}]")
    print(f"Ping: {ping_result:.2f} ms")
    print(f"Download: {download_speed:.2f} Mbps")
    print(f"Upload: {upload_speed:.2f} Mbps")

    # Logging to CSV
    log_file = "speed_log.csv"
    file_exists = os.path.isfile(log_file)

    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Ping (ms)", "Download (Mbps)", "Upload (Mbps)"])
        writer.writerow([timestamp, ping_result, download_speed, upload_speed])

if __name__ == "__main__":
    test_internet_speed()

