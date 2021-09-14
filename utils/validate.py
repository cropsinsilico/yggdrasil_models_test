import os
import glob
import argparse
from yggdrasil import yamlfile, runner


def validate(yamls, run=False):
    for x in yamls:
        yamlfile.parse_yaml(x, model_submission=True)
        if run:
            runner.run(x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Validate a model YAML against the yggdrasil submisison schema.")
    parser.add_argument(
        'yaml', nargs='*',
        help="Model YAML specification file to validate.")
    parser.add_argument(
        '--run', action='store_true',
        help="Run each model after validating it.")
    args = parser.parse_args()
    if not args.yaml:
        args.yaml = sorted(glob.glob(os.path.join(
            os.path.dirname(os.path.dirname(__file__)), '*')))
    validate(args.yaml, run=args.run)
