import unittest


def check_password(password):
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters long')
    return True
class TestCheckPassword(unittest.TestCase):
    def test_check_password(self):
        with self.assertRaises(ValueError):
            check_password(password="234")
    def test_load_password(self):
        self.assertTrue(check_password(password="Aa123456"))
        # .assetTrue(check_password(password="Aa123456"))

