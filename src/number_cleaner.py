"""
Reads the CSV file, validates and cleans phone numbers,
and returns a clean, deduplicated list ready for sending.
"""

import re
import pandas as pd
from src import config


def load_numbers_from_csv(csv_path: str, column_name: str) -> list:
    """Reads numbers from the given CSV column. Raises clear errors if something's wrong."""
    try:
        df = pd.read_csv(csv_path, dtype=str)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")

    # Strip whitespace from column headers to avoid mismatch issues
    df.columns = [c.strip() for c in df.columns]

    if column_name not in df.columns:
        raise ValueError(
            f"Column '{column_name}' not found in CSV. "
            f"Available columns: {list(df.columns)}"
        )

    raw_numbers = df[column_name].dropna().tolist()
    return raw_numbers


def clean_number(raw_number: str, default_country_code: str) -> str | None:
    """
    Cleans a single phone number into international format.
    Returns None if the number is invalid.
    """
    if not raw_number:
        return None

    # Keep only digits
    digits = re.sub(r"\D", "", str(raw_number))

    if not digits:
        return None

    # Case 1: starts with 0 (local format, e.g. 03001234567)
    if digits.startswith("0"):
        digits = default_country_code + digits[1:]

    # Case 2: already has country code without '+' (e.g. 923001234567)
    elif digits.startswith(default_country_code):
        pass

    # Case 3: looks like a bare local number without leading 0 (e.g. 3001234567)
    elif len(digits) == 10:
        digits = default_country_code + digits

    else:
        # Doesn't match any known pattern — treat as invalid
        return None

    # Basic sanity check: most international numbers are 11-15 digits
    if not (11 <= len(digits) <= 15):
        return None

    return "+" + digits


def get_clean_number_list(csv_path: str = None, column_name: str = None) -> list:
    """
    Full pipeline: load from CSV -> clean -> dedupe.
    Returns a list of valid, unique, properly formatted numbers.
    """
    csv_path = csv_path or config.CSV_PATH
    column_name = column_name or config.PHONE_COLUMN_NAME

    raw_numbers = load_numbers_from_csv(csv_path, column_name)

    cleaned = []
    invalid_count = 0

    for raw in raw_numbers:
        result = clean_number(raw, config.DEFAULT_COUNTRY_CODE)
        if result:
            cleaned.append(result)
        else:
            invalid_count += 1
            print(f"⚠️  Skipping invalid number: {raw}")

    unique_numbers = sorted(set(cleaned))

    print(f"\n✅ Loaded {len(raw_numbers)} rows | "
          f"Valid: {len(cleaned)} | Invalid: {invalid_count} | "
          f"Unique after dedup: {len(unique_numbers)}\n")

    return unique_numbers