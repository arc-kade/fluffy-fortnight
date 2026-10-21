"""Processing logic using functional programming (map, filter, lambda)."""

from utils.decorator import log_execution
from validator import is_valid_line


@log_execution
def process_records(lines):
    """Split raw lines into (valid_records, invalid_lines).

    * filter()  selects valid / invalid lines
    * map()     turns lines into dicts and uppercases the usernames
    * lambda    used for the small transformations
    """
    valid_lines = list(filter(is_valid_line, lines))
    invalid_lines = list(filter(lambda line: not is_valid_line(line), lines))

    records = map(
        lambda line: dict(zip(("username", "email", "login_time"), line.split())),
        valid_lines,
    )
    valid_records = list(
        map(lambda record: {**record, "username": record["username"].upper()}, records)
    )
    return valid_records, invalid_lines
