from argparse import ArgumentParser
from pathlib import Path

def validate_path_dir(dir):
        is_output_dir = "/".join(dir.split("/")[:-1])
        is_json = dir[-5:] == ".json"
        print(f"dir: {is_json}\n{dir}")
        print(f"output_dir: {Path(is_output_dir).is_dir()}\n{is_output_dir}")
        if is_json and Path(is_output_dir).is_dir():
            return True
        else:
            raise FileNotFoundError("Error: Ensure that the file path is correct.")


def parse_arguments():
    """
    Parse arguments from CLI execution.
    """

    arg_parser = ArgumentParser()

    arg_parser.add_argument(
        "-i",
        "--input-path",
        required=True,
        help="Input path for a file.",
    )
    arg_parser.add_argument(
        "-o",
        "--output-path",
        required=True,
        help="Output path for a file.",
    )
    arg_parser.add_argument(
        "-m",
        "--output-mode",
        default="all",
        required=False,
        choices=["all", "single", "multi"],
        help="Select the output mode for a file transformation.",
    )
    args_namespace = arg_parser.parse_args()

    validate_path_dir(args_namespace.input_path)
    validate_path_dir(args_namespace.output_path)

    return args_namespace

if __name__ == "__main__":
    args = parse_arguments()
    OUTPUT_MODE = args.output_mode
    INPUT_PATH = args.input_path
    OUTPUT_PATH = args.output_path

    # Do operations