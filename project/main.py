"""Secure Log Analyzer & Backup System - entry point."""

from pathlib import Path

from file_handler import FileHandlingError, load_pickle, read_lines, save_pickle, write_lines
from processor import process_records

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "log.txt"
INVALID_FILE = BASE_DIR / "invalid_log.txt"
BACKUP_FILE = BASE_DIR / "valid_log.pkl"


def display_records(title, records):
    print(f"\n=== {title} ({len(records)}) ===")
    if not records:
        print("  (none)")
    for r in records:
        print(f"  {r['username']:<12} {r['email']:<28} {r['login_time']}")


def main():
    print("=== Secure Log Analyzer & Backup System ===")
    try:
        lines = read_lines(LOG_FILE)
        print(f"Read {len(lines)} record(s) from {LOG_FILE.name}")

        valid_records, invalid_lines = process_records(lines)
        display_records("Valid records", valid_records)

        write_lines(INVALID_FILE, invalid_lines)
        print(f"\n{len(invalid_lines)} invalid record(s) written to {INVALID_FILE.name}")

        save_pickle(BACKUP_FILE, valid_records)
        print(f"Valid records pickled to {BACKUP_FILE.name}")

        display_records("Loaded from pickle", load_pickle(BACKUP_FILE))

    except FileHandlingError as error:
        print(f"\nFile error: {error}")
    except KeyboardInterrupt:
        print("\nCancelled by user.")
    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()
