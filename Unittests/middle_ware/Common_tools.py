__author__ = 'andrei'

import unittest
from configs import app_home
from API_spec_generator import get_API_list
from app import get_routes


class TestDatabaseInterfaces(unittest.TestCase):

    def test_API_sp(self):
        self.assertTrue(True)

class TestImplementedInterfaces(unittest.TestCase):

    def test_API_sp(self):
        self.assertTrue(open(app_home+'/API_specs.md', 'r'))

    def test_url_entry_points(self):
        routes = get_routes()[1]
        for API in get_API_list():
            self.assertTrue(API[1]["address"] in routes, msg = "%s not in routes" % API[1]["address"] )





if __name__ == '__main__':
    unittest.main()
