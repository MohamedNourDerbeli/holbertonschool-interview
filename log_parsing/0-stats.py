#!/usr/bin/python3
import re
import sys

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def main():
    total_size = 0
    allowed_statuses = {200, 301, 400, 401, 403, 404, 405, 500}
    status_counts = {code: 0 for code in allowed_statuses}
    line_count = 0

    # Regular expression pattern to match the input format
    pattern = re.compile(
        r'^'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'  # IP address
        r' - \[.*?\] '                           # date
        r'"GET /projects/260 HTTP/1\.1" '         # request line
        r'(\d{3}) (\d+)$'                        # status and size
    )

    try:
        for line in sys.stdin:
            line = line.strip()
            match = pattern.match(line)
            if not match:
                continue

            status_str, size_str = match.groups()

            try:
                status = int(status_str)
                size = int(size_str)
            except ValueError:
                # Skip line if conversion fails (unlikely due to regex)
                continue

            total_size += size
            if status in allowed_statuses:
                status_counts[status] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

if __name__ == "__main__":
    main()
