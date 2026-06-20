"""
Entry point for the WhatsApp bulk messaging bot.

Before running:
1. Place your CSV file at data/students.csv
2. Place the NCCS logo at data/logo.png
3. Update src/config.py with your correct column name and message text
4. Make sure you're logged into WhatsApp Web in your default browser
5. Run: python main.py
"""

from src import config
from src.number_cleaner import get_clean_number_list
from src.sender import send_bulk_messages


def main():
    print("📋 Step 1: Reading and cleaning numbers from CSV...")
    numbers = get_clean_number_list(config.CSV_PATH, config.PHONE_COLUMN_NAME)

    if not numbers:
        print("❌ No valid numbers found. Please check your CSV file. Exiting.")
        return

    confirm = input(f"About to send to {len(numbers)} numbers. Type 'yes' to proceed: ")
    if confirm.strip().lower() != "yes":
        print("Aborted by user.")
        return

    print("\n📋 Step 2: Sending messages...\n")
    send_bulk_messages(numbers)


if __name__ == "__main__":
    main()