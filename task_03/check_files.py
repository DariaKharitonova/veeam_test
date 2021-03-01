import hashlib

AVAILABLE_ALGORITHMS = ['MD5', 'SHA1', 'SHA256']


def check_files(file_path, directory_path):
    result = ''
    with open(file_path, 'r') as input_file:
        lines = input_file.read().splitlines()

        for line in lines:
            parsed_lines = line.split()
            file_name = parsed_lines[0]
            hash_algorithm = parsed_lines[1].upper()
            hash_sum = parsed_lines[2]
            path_to_check_files = f'{directory_path}/{file_name}'
            if hash_algorithm not in AVAILABLE_ALGORITHMS:
                result += f'{file_name} WRONG ALGORITHM\n'

            else:
                try:
                    with open(path_to_check_files, 'r') as file:
                        if hash_algorithm == 'MD5':
                            h = hashlib.md5()
                        elif hash_algorithm == 'SHA1':
                            h = hashlib.sha1()
                        else:
                            h = hashlib.sha256()
                        h.update(bytes(file.read(), 'utf-8'))
                        if hash_sum == h.hexdigest():
                            result += f'{file_name} OK\n'
                        else:
                            result += f'{file_name} FAIL\n'

                except FileNotFoundError:
                    result += f'{file_name} NOT FOUND\n'
        return result.rstrip('\n')
