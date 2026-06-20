"""
Handles writing send results to a CSV log file,
so you have a clear record of what succeeded or failed.
"""

import csv
import os
from datetime import datetime
from src import config

EXPECTED_HEADERS = ["number", "status", "timestamp", "error_message"]


def init_log_file():
    """Creates the log file with headers if it doesn't exist or is invalid/empty."""
    os.makedirs(os.path.dirname(config.LOG_PATH), exist_ok=True)

    needs_fresh_header = True

    if os.path.exists(config.LOG_PATH):
        try:
            with open(config.LOG_PATH, mode="r", encoding="utf-8") as f:
                reader = csv.reader(f)
                first_row = next(reader, None)
                if first_row == EXPECTED_HEADERS:
                    needs_fresh_header = False
        except Exception:
            needs_fresh_header = True

    if needs_fresh_header:
        with open(config.LOG_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(EXPECTED_HEADERS)


def log_result(number: str, status: str, error_message: str = ""):
    """Appends a single result row to the log file."""
    with open(config.LOG_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            number,
            status,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            error_message
        ])


def print_summary():
    """Reads the log file and prints a quick summary at the end of the run."""
    if not os.path.exists(config.LOG_PATH):
        print("No log file found.")
        return

    sent, failed = 0, 0
    try:
        with open(config.LOG_PATH, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("status") == "SUCCESS":
                    sent += 1
                elif row.get("status") == "FAILED":
                    failed += 1
    except Exception as e:
        print(f"⚠️ Could not read log file properly: {e}")
        return

    print("\n──────── SUMMARY ────────")
    print(f"✅ Sent:   {sent}")
    print(f"❌ Failed: {failed}")
    print(f"📄 Full log: {config.LOG_PATH}")
    print("──────────────────────────\n")