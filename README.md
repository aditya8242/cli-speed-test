# CLI Speed Test 🚀

A lightweight Python command-line tool to test your internet speed (Download, Upload, Ping) and log results to a CSV file. Useful for tracking your ISP performance over time.

## ⚙️ Features

- Simple CLI interface  
- Measures Ping, Download, and Upload  
- Appends results to speed_log.csv  
- Easily automatable via cron for periodic testing  

## 🧪 Usage

Run the test manually:

    python speed_test.py

Or if you're using a virtual environment:

    source .venv/bin/activate
    python speed_test.py

## 💾 Example Output

    [2025-07-07 14:12:37]
    Ping: 60.33 ms
    Download: 1.31 Mbps
    Upload: 1.49 Mbps

## 📈 Example CSV Output

    Timestamp, Ping (ms), Download (Mbps), Upload (Mbps)
    2025-07-07 14:00:00, 60.33, 1.31, 1.49
    2025-07-07 15:00:00, 45.20, 12.45, 4.83

## ⏰ Automating with Cron (Optional)

You can automate the script to run periodically using cron.

### For Linux/macOS:

1. Open your crontab:

    crontab -e

2. Add a cron job. For example, to run the script every hour:

    0 * * * * cd /full/path/to/cli-speed-test && /full/path/to/.venv/bin/python speed_test.py

    Replace paths with your actual project and Python paths.
    This will append new results to speed_log.csv every hour.

3. To confirm it’s running:

    tail speed_log.csv

## 📦 Installation

Install dependencies:

    pip install -r requirements.txt

Or install manually:

    pip install speedtest-cli

## 🛣️ Roadmap

- [x] Manual speed testing via CLI  
- [x] Logging results to CSV  
- [x] Cron-compatible automation  
- [ ] Plotting trends with matplotlib or plotext  
- [ ] Real-time CLI output with rich  
- [ ] Speed drop alerts  
- [ ] Web dashboard (Flask/Streamlit)

## 💡 Ideas?

Feel free to fork or suggest features via issues. Contributions welcome.

## 👨‍💻 Built by Aditya — because “trusting your ISP” isn't a debugging strategy.

