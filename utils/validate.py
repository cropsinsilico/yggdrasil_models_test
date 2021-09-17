import os
import glob
import argparse
from yggdrasil.services import validate_model_submission


def validate(yamls, run=False):
    for x in yamls:
        validate_model_submission(x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Validate a model YAML against the yggdrasil submisison schema.")
    parser.add_argument(
        'yaml', nargs='*',
        help="Model YAML specification file to validate.")
    args = parser.parse_args()
    if not args.yaml:
        yaml_dir = os.path.dirname(os.path.dirname(__file__))
        args.yaml = sorted(glob.glob(os.path.join(yaml_dir, '*.yml'))
                           + glob.glob(os.path.join(yaml_dir, '*.yaml')))
    validate(args.yaml)
