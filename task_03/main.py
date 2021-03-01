from task_03.check_files import check_files
from task_03.cli import arg_parse


def main():
    args = arg_parse().parse_args()
    print(check_files(args.path_to_input_file,
                      args.path_to_directory_for_check))


if __name__ == "__main__":
    main()
