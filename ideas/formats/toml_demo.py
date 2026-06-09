import argparse
import pprint
import tomllib
import sys

toml = [
"""
one = 1
1 = "one"
""",
]


def main(args):
    if not args.input:
        for text in toml:
            data = tomllib.loads(text)
            pprint.pprint(data, indent=1)
        return 0
    return 1


def parser():
    rv = argparse.ArgumentParser(usage=__doc__, fromfile_prefix_chars="=")
    rv.add_argument("input", nargs="*")
    rv.convert_arg_line_to_args = lambda x: x.split()
    return rv


def run():
    p = parser()
    args = p.parse_args()
    rv = main(args)
    sys.exit(rv)


if __name__ == "__main__":
    run()
