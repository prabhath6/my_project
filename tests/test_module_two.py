from my_project import module_two
from nose.tools import assert_equal


class TestModuleTwo():

    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_module_two(self):
        expected = module_two.custom_count("AAAAsdfsdvver", 3)
        actual = [('A', 4)]
        assert_equal(expected, actual)
