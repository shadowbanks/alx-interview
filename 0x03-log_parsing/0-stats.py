#!/usr/bin/python3
import sys
import re


def print_output(status_code, total_Size):
    print(f"File size: {total_Size}")
    for key, value in status_code.items():
        if value > 0:
            print(f"{key}: {value}")


if '__main__' == __name__:
    status_code = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }
    count = 0
    total_Size = 0
    try:
        for line in sys.stdin:
            r = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} -.+G.+\" (\d{3}) (\d{3})"
            result = re.search(r, line)
            if result:
                count += 1
                code = int(result.group(1))
                file_size = int(result.group(2))
                total_Size += file_size
                if code in status_code.keys():
                    status_code[code] += 1
                if count == 10:
                    print_output(status_code, total_Size)
                    count = 0
    except KeyboardInterrupt:
        print_output(status_code, total_Size)
