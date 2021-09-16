import os
import glob
import argparse
# from yggdrasil.services import validate_model_submission
from yggdrasil import yamlfile, runner


def validate(yamls, run=False):
    for x in yamls:
        # validate_model_submission(x)
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
        yaml_dir = os.path.dirname(os.path.dirname(__file__))
        args.yaml = sorted(glob.glob(os.path.join(yaml_dir, '*.yml'))
                           + glob.glob(os.path.join(yaml_dir, '*.yaml')))
    validate(args.yaml, run=args.run)
