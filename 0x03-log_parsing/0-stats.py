#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    parts = line.split()
    if len(parts) >= 9:
        ip_address = parts[0]
        date = parts[3][1:]
        status_code = parts[-2]
        file_size = int(parts[-1])
        return ip_address, date, status_code, file_size
    return None, None, None, None

def main():
    total_size = 0
    status_codes = {}

    try:
        for line_count, line in enumerate(sys.stdin, 1):
            ip, _, status_code, file_size = parse_line(line.strip())
            if ip and status_code and isinstance(file_size, int):
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass  # Continue processing even if interrupted with CTRL + C

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()

