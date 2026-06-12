import argparse
import email
import pathlib
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

    for path in args.input:
        text = path.read_text()
        if path.suffix == ".eml":
            msg = email.message_from_string(text)
            for n, part in enumerate(msg.walk()):
                if not n: continue
                pprint.pprint(dict(part, n=n, text=str(part)))
    return 0


def parser():
    rv = argparse.ArgumentParser(usage=__doc__, fromfile_prefix_chars="=")
    rv.add_argument("input", type=pathlib.Path, nargs="*")
    rv.convert_arg_line_to_args = lambda x: x.split()
    return rv


def run():
    p = parser()
    args = p.parse_args()
    rv = main(args)
    sys.exit(rv)


if __name__ == "__main__":
    run()
