from hamcrest import assert_that, equal_to, none, not_none, contains_string


class Assert:

    @staticmethod
    def assert_true(condition, message=""):
        assert_that(condition, equal_to(True), message)

    def assert_false(condition, message=None):
        assert_that(condition, equal_to(False), message)

    def assertEqualTo(actual, expected, error_message):
        assert_that(actual, equal_to(expected), error_message)

    def assert_contains(actual, expected, message=None):
        assert_that(actual, contains_string(expected), message)

    def assert_not_equals(actual, expected, message=None):
        assert_that(actual, not (equal_to(expected)), message)

    def assert_none(condition, message=None):
        assert_that(condition, none, message)

    def assert_not_none(condition, message=None):
        assert_that(condition, not_none, message)

    def assert_fail(message=None):
        assert_that(False, equal_to(True), message)
