"""Regular-expression validation of log records."""

import re

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$")
TIME_PATTERN = re.compile(r"^([01]\d|2[0-3]):[0-5]\d$")   # HH:MM, 24-hour


def is_valid_email(email):
    return EMAIL_PATTERN.match(email) is not None


def is_valid_time(login_time):
    return TIME_PATTERN.match(login_time) is not None


def is_valid_line(line):
    """A line is valid if it has exactly 3 fields: username email login_time,
    with a well-formed email and a valid HH:MM time."""
    parts = line.split()
    if len(parts) != 3:
        return False
    _, email, login_time = parts
    return is_valid_email(email) and is_valid_time(login_time)
