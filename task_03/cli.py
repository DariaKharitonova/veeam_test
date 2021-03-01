import argparse


def arg_parse():
    parser = argparse.ArgumentParser(description='File integrity check')
    parser.add_argument('path_to_input_file', type=str)
    parser.add_argument('path_to_directory_for_check', type=str)
    return parser
