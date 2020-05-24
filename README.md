# devsecops_exercise

This program is designed to take two sorted list literals as input, merge-sort them, and output a single sorted list. Duplicate values are preserved, and one or both input lists may be empty.

The program is designed to exit safely if fewer than two lists are provided, if non-digit values are stored in the input lists, and if the input lists are not sorted.

## Requirements

This program does not depend on any external packages, but it does require some of the standard library features introduced in Python 3. Backwards compatibility to Python 2 is not guaranteed.

## How to run this program

This program may be executed from the CLI like so:

`python3 sort_two_lists.py [1, 2, 3] [4, 5, 6]`

The output of this will be `[1, 2, 3, 4, 5, 6]`

N.B., this functionality is only guaranteed to work in `bash`. Other shells may fail to parse the list arguments (`zsh` is known to throw an error).

### Running the program in a Docker container

The enclosed Dockerfile also provides a containerization mechanism for the program. Becuse the program's design called for CLI input of list literals including spaces directly to `docker run`, the Dockerfile uses `bootstrap.sh` as an entrypoint to parse the list arguments and pass them into the Python script.

To build the container, `cd` to the directory containing the repo source files and execute the following command:

`docker build -t sort_two_lists .`

The container can then be run using the following command:

`docker run sort_two_lists [1, 2, 3] [4, 5, 6]`

N.B.: The list literal inputs may include spaces, but the spaces are not necessary. Either way, the mechanism Python uses to parse these arguments into list structures will function.

## Unit Tests

The basic functionality and failure modes of this program are covered by a pytest file. To run unit tests, use the following command:

`python3 -m pytest sort_two_lists_test.py`
