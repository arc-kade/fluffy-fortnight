"""All file input/output lives here: text files and pickle files."""

import pickle


class FileHandlingError(Exception):
    """Raised with a friendly message when a file operation fails."""


def read_lines(path):
    """Return the non-empty, stripped lines of a text file."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        raise FileHandlingError(f"File not found: {path}")
    except PermissionError:
        raise FileHandlingError(f"Permission denied while reading: {path}")
    except UnicodeDecodeError:
        raise FileHandlingError(f"File is not valid UTF-8 text: {path}")
    except OSError as error:
        raise FileHandlingError(f"Could not read {path}: {error}")


def write_lines(path, lines):
    """Write each item of `lines` on its own line."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.writelines(line + "\n" for line in lines)
    except OSError as error:
        raise FileHandlingError(f"Could not write {path}: {error}")


def save_pickle(path, data):
    """Serialize `data` to a binary pickle file."""
    try:
        with open(path, "wb") as file:
            pickle.dump(data, file)
    except (OSError, pickle.PicklingError) as error:
        raise FileHandlingError(f"Could not pickle data to {path}: {error}")


def load_pickle(path):
    """Load and return data from a binary pickle file."""
    try:
        with open(path, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        raise FileHandlingError(f"Pickle file not found: {path}")
    except (pickle.UnpicklingError, EOFError):
        raise FileHandlingError(f"Pickle file is corrupted or empty: {path}")
    except OSError as error:
        raise FileHandlingError(f"Could not read {path}: {error}")