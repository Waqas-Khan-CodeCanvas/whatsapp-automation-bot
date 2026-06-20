# NCCS WhatsApp Bulk Messaging Bot

## Folder structure
whatsapp-bulk-bot/
├── data/
│   ├── students.xlsx   <- your Excel file with a phone number column
│   └── logo.png         <- NCCS logo image
├── logs/
│   └── send_log.csv     <- auto-generated after running
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── number_cleaner.py
│   ├── sender.py
│   └── logger.py
├── main.py
└── requirements.txt

## Setup
1. Install dependencies:
   pip install -r requirements.txt

2. Place your files:
   - data/students.xlsx
   - data/logo.png

3. Open src/config.py and update:
   - PHONE_COLUMN_NAME -> exact header name of the numbers column in your Excel
   - MESSAGE_CAPTION -> the message text you want sent
   - DEFAULT_COUNTRY_CODE -> change if not Pakistan (92)

4. Log into WhatsApp Web (web.whatsapp.com) in your default browser and keep it logged in.

5. Run:
   python main.py

## Notes
- This uses pywhatkit, which automates your browser to send via WhatsApp Web.
- Each message has a randomized delay (15-30s) to reduce the risk of WhatsApp flagging the account for spam.
- Do not minimize or close the browser window while sending.
- Check logs/send_log.csv after each run to see which numbers succeeded or failed.
- For large-scale or recurring use, consider Meta's official WhatsApp Business API instead.