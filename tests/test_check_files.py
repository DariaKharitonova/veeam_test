import pytest
from task_03.check_files import check_files


@pytest.mark.parametrize('input_file_path, check_directory, correct_view', [ # noqa E501
    ('path_to_input_file',
     'path_to_directory',
     'correct_output')
])
def test_check_files(input_file_path, check_directory,
                     correct_view, request):

    input_file = request.getfixturevalue(input_file_path)
    directory = request.getfixturevalue(check_directory)
    correct = open(request.getfixturevalue(correct_view)).read()
    assert check_files(input_file, directory) == correct
