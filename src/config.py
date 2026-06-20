"""
Central configuration file.
Edit values here — never touch logic in other files.
"""

import os

# ── Paths ──────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSV_PATH = os.path.join(BASE_DIR, "data", "students.csv")
LOGO_PATH = os.path.join(BASE_DIR, "data", "logo.png")
LOG_PATH = os.path.join(BASE_DIR, "logs", "send_log.csv")

# ── CSV settings ────────────────────────────────────────
# Exact column header in your CSV file that contains phone numbers
PHONE_COLUMN_NAME = "Number"   # change this to match your actual column header

# ── Country code settings ──────────────────────────────
DEFAULT_COUNTRY_CODE = "92"    # Pakistan. Change if needed.

# ── Message settings ───────────────────────────────────
MESSAGE_CAPTION = """\
🌟 Assalam-o-Alaikum!

Good news! If you applied for our previous E-Commerce course but were not selected, this is your chance to be part of something even bigger and more advanced.

We are now offering a *NAVTTC AI-Powered E-Commerce Course*, where you'll learn how to combine Artificial Intelligence with modern E-Commerce skills to stay ahead in today's digital marketplace.

✅ *100% FREE Training*
✅ Industry-Relevant AI & E-Commerce Skills
✅ NAVTTC Supported Program
✅ Limited Seats Available

If you are interested in joining, please contact us for details and registration:

contact No 📞 :  *+92 347 5266247*

⚡ Limited seats available. Priority will be given to interested candidates who respond early.

We look forward to helping you take the next step in your professional journey.
"""

# ── Sending behavior ────────────────────────────────────
MIN_DELAY_SECONDS = 30     # minimum wait between messages
MAX_DELAY_SECONDS = 45     # maximum wait between messages
# WAIT_TIME_SECONDS = 20     # time pywhatkit waits for WhatsApp Web tab to load before sending
WAIT_TIME_SECONDS = 30     # time pywhatkit waits for WhatsApp Web tab to load before sending
# TAB_CLOSE_DELAY = 5        # seconds before pywhatkit closes the browser tab after sending
TAB_CLOSE_DELAY = 15        # seconds before pywhatkit closes the browser tab after sending

# ── Retry settings ─────────────────────────────────────
MAX_RETRIES = 2