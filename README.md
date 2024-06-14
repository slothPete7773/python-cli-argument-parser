# Python CLI Argument Parser

> **Note!**
> 
> **This documentation was generated from Gemini AI because I was lazy to write a documentation.**

This module provides a command-line interface (CLI) argument parser for a Python script. It defines functions to validate input/output paths and parse arguments passed from the command line.

## Functions

### `parse_arguments()`

**Purpose:** Parses command-line arguments using the `argparse` module.

**Returns:**

- `args_namespace` (Namespace): A namespace object containing the parsed arguments and their values.

**CLI Arguments:**

- `-i`, `--input-path` (required): Input path for a `.json` file.
- `-o`, `--output-path` (required): Output path for a `.json` file (in an existing directory).
- `-m`, `--output-mode` (optional, default: "all"): Output mode for file transformation ("all", "single", or "multi").

**Implementation Notes:**

- Creates an `ArgumentParser` object to handle argument parsing.
- Adds arguments using `add_argument`, specifying their names, types, help messages, and whether they are required.
- Parses the arguments using `parse_args()`.
- Validates the input and output paths using `validate_path_dir`.
- Returns the parsed arguments as a namespace.

### `validate_path_dir(dir)`

**Purpose:** Validates whether a given path `dir` represents a valid file path leading to a `.json` file within an existing directory.

**Parameters:**

- `dir` (str): The file path to be validated.

**Returns:**

- `True` if the path is valid (leads to a `.json` file within an existing directory).

**Raises:**

- `FileNotFoundError` if the path is not valid (e.g., not a `.json` file, directory doesn't exist).

**Implementation Notes:**

- Splits the path to extract the directory part.
- Checks if the file extension is `.json`.
- Verifies if the extracted directory exists using `Path.is_dir()`.
- Includes print statements for debugging purposes (remove in production).



## Main Execution

**Purpose:** The entry point for the script when executed directly.

**Actions:**

- Calls `parse_arguments` to get the parsed arguments.
- Extracts the values of `OUTPUT_MODE`, `INPUT_PATH`, and `OUTPUT_PATH` from the namespace.
- Placeholder comment (`# Do operations`) indicates where you would add the main logic of your file transformation script.

## Example Usage

```bash
python cli_argument_parser.py -i data/input.json -o results/output.json -m single 
