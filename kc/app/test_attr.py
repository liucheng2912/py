from hamcrest import assert_that, equal_to, close_to,  contains_string


class TestAttr:
    def test_hamcrest(self):
        assert_that(10,equal_to(10))
        assert_that(10,close_to(8,2))
        assert_that('constains a string',contains_string('string'))

