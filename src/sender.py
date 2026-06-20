"""
Core sending logic using pywhatkit.
Sends the NCCS logo with caption text to each number,
with retries, delays, and per-number error handling.
"""

import time
import random
import datetime
import pywhatkit as kit

from src import config
from src import logger


def _get_send_time(offset_seconds: int = 90):
    """
    pywhatkit needs a future time (hour, minute) to schedule the send.
    We schedule each message a bit further into the future to avoid collisions.
    """
    send_time = datetime.datetime.now() + datetime.timedelta(seconds=offset_seconds)
    return send_time.hour, send_time.minute


def send_single_message(number: str, attempt: int = 1) -> bool:
    """
    Attempts to send the logo + caption to one number.
    Returns True on success, False on failure (after retries).
    """
    try:
        hour, minute = _get_send_time(offset_seconds=90)

        kit.sendwhats_image(
            receiver=number,
            img_path=config.LOGO_PATH,
            caption=config.MESSAGE_CAPTION,
            wait_time=config.WAIT_TIME_SECONDS,
            tab_close=True,
            # tab_close=False,
            close_time=config.TAB_CLOSE_DELAY,
        )

        logger.log_result(number, "SUCCESS")
        print(f"✅ Sent to {number}")
        return True

    except Exception as e:
        error_msg = str(e)
        print(f"❌ Attempt {attempt} failed for {number}: {error_msg}")

        if attempt < config.MAX_RETRIES:
            print(f"🔁 Retrying {number}...")
            time.sleep(10)
            return send_single_message(number, attempt + 1)

        logger.log_result(number, "FAILED", error_msg)
        return False


def send_bulk_messages(numbers: list):
    """
    Loops through all numbers, sends messages one by one
    with randomized delays between each to reduce spam-flag risk.
    """
    logger.init_log_file()
    total = len(numbers)

    print(f"🚀 Starting bulk send to {total} numbers...\n")

    for index, number in enumerate(numbers, start=1):
        print(f"[{index}/{total}] Sending to {number} ...")
        send_single_message(number)

        if index < total:
            delay = random.randint(config.MIN_DELAY_SECONDS, config.MAX_DELAY_SECONDS)
            print(f"⏳ Waiting {delay}s before next message...\n")
            time.sleep(delay)

    logger.print_summary()