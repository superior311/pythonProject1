import unittest
from voting import User
from unittest import mock
#create the class for testing
class Voting(unittest.TestCase):
	@mock.patch('voting.User.read_file', return_value=['name2\n'])
	def test_user_has_not_voted(self, read_file):
		file = open('users.txt', 'w')
		file.write('name2')
		file.close()
	#execution
		user = User('name1')
		has_voted = user.has_user_already_voted()
	#assertion
		self.assertFalse(has_voted)
	def test_user_voted(self):

		user = User('name2')
		has_voted = user.has_user_already_voted()

		self.assertTrue(has_voted)

	@mock.patch('voting.User.write_file')
	def test_vote_was_registered(self, write_file):
		#execution
		user = User('name2')
		user.register_the_vote(1)
		##assertion
		write_file.assert_called_once_with('1\n')
