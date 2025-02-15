#!/usr/bin/python3
"""
Log parser that reads from standard input and computes:
- The total file size.
- The count of status codes from allowed categories.

Outputs stats every 10 lines, at the end of input, and when interrupted.
"""
import sys
import re


def print_stats(total_size, status_counts):
    """
    Prints the accumulated file size and counts of allowed status codes.

    :param total_size: The total size of all processed requests.
    :param status_counts: Dictionary mapping HTTP status codes to their occurrence count.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def main():
    """
    Reads log entries from standard input, extracts file sizes and status codes,
    and prints aggregated statistics every 10 lines or at the end of input.
    """
    total_size = 0
    allowed_statuses = {200, 301, 400, 401, 403, 404, 405, 500}
    status_counts = {code: 0 for code in allowed_statuses}
    line_count = 0

    # Regular expression to match log format
    pattern = re.compile(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP address
        r' .* '                                 # Ignore other fields
        r'"GET /projects/260 HTTP/1\.1" '       # Request line
        r'(\d{3}) '                             # Status code
        r'(\d+)'                                # File size
    )

    try:
        for line in sys.stdin:
            line = line.strip()
            match = pattern.search(line)  # Use `search()` instead of `match()`

            if match:
                try:
                    _, status_str, size_str = match.groups()
                    status = int(status_str)
                    size = int(size_str)

                    total_size += size
                    if status in allowed_statuses:
                        status_counts[status] += 1

                    line_count += 1
                    if line_count % 10 == 0:
                        print_stats(total_size, status_counts)
                except ValueError:
                    continue  # Ignore lines that fail conversion
            else:
                continue  # Ignore completely malformed lines

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise  # Re-raise for proper exit signal handling

    # **Always print stats at least once (even for an empty file)**
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
