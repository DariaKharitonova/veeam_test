import pytest
from task_03.check_files import check_files


@pytest.mark.parametrize('path_to_input_file, path_to_directory, correct_output', [ # noqa E501
    ('path_to_input_file',
     'path_to_directory',
     'correct_output')
])
def test_check_files(path_to_input_file, path_to_directory,
                     correct_output, request):
    print(request.getfixturevalue(path_to_input_file))
    print(request.getfixturevalue(path_to_directory))
    print(open(request.getfixturevalue(correct_output)).read())
    input_file = request.getfixturevalue(path_to_input_file)
    directory = request.getfixturevalue(path_to_directory)
    correct = open(request.getfixturevalue(correct_output)).read()
    assert check_files(input_file, directory) == correct
