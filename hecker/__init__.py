# SPDX-License-Identifier: GPL-2.0

import sys


def main() -> None:
    args_count = len(sys.argv)
    if args_count != 2:
        print("Usage: hecker TEXT")
        sys.exit(1)

    print(f"*in hacker voice*: {sys.argv[1]}")


if __name__ == "__main__":
    main()
