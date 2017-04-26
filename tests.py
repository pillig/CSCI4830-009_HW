import helloworld as hw
import unittest


class TestHelloWorld(unittest.TestCase):
    def test_hello_world_string(self):
        self.assertEqual("Hello World", hw.hello_world_string())

if __name__ == "__main__":
    unittest.main()