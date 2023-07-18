#!/usr/bin/python3

import sys

total_file_size = 0
status_code_counts = {}
line_count = 0

for line in sys.stdin:
    # Split the line into its components
    components = line.split()

    # Check if the line matches the expected format
    if len(components) != 7:
        continue

    ip_address, _, _, _, status_code, file_size = components

    # Check if the status code is a valid integer
    try:
        status_code = int(status_code)
    except ValueError:
        continue

    # Update the metrics
    total_file_size += int(file_size)
    status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1
    line_count += 1

    # Print the metrics every 10 lines or on keyboard interruption
    if line_count % 10 == 0:
        print(f"Total file size: {total_file_size}")
        for code in sorted(status_code_counts.keys()):
            print(f"{code}: {status_code_counts[code]}")
        print()
