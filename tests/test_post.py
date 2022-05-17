import unittest
from flaskblog.models import Post


class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(1234, 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))