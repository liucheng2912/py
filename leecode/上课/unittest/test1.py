import unittest

class Search:
    def search_func(self):
        print("search")
        return True

class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")
        cls.search = Search()

    def setUp(self) -> None:
        print("setup")
        self.search=Search()

    def tearDown(self) -> None:
        print("teardown")

    def test_search1(self):
        print("testsearch1")
        assert True == self.search.search_func()

    def test_search2(self):
        print("testsearch2")
        assert True == self.search.search_func()

    def test_search3(self):
        print("testsearch3")
        assert True == self.search.search_func()

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

class TestSearch1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class1")
        cls.search = Search()

    def setUp(self) -> None:
        print("setup1")
        self.search=Search()

    def tearDown(self) -> None:
        print("teardown1")

    def test_search1(self):
        print("testsearch1")
        assert True == self.search.search_func()

    def test_search2(self):
        print("testsearch2")
        assert True == self.search.search_func()

    def test_search3(self):
        print("testsearch3")
        assert True == self.search.search_func()

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class1")
if __name__ == '__main__':
    unittest.main()