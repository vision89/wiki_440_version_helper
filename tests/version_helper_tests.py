from wiki_440_version_helper.wiki_440_version_helper import Version_Helper
from unittest import TestCase

class Version_Helper_Test_Case(TestCase):

    file_path_one = '/Users/dustingulley/PycharmProjects/wiki_440_version_helper/tests/test_files/test_file_v1.md'
    file_path_two = '/Users/dustingulley/PycharmProjects/wiki_440_version_helper/tests/test_files/test_file_v2.md'
    file_path_no_file = '/Users/dustingulley/PycharmProjects/wiki_440_version_helper/tests/test_files'
    file_one = 'test_file_v1.md'
    file_two = 'test_file_v2.md'

    def test_get_filename_from_path(self):
        val = Version_Helper.get_filename_from_path(self.file_path_one)
        assert val == self.file_one

    def test_get_path_without_filename(self):
        val = Version_Helper.get_path_without_filename(self.file_path_one)
        assert val == self.file_path_no_file

    def test_get_highest_version_of_file_path(self):
        val = Version_Helper.get_highest_version_of_file_path(self.file_path_one)
        assert val == self.file_path_two
