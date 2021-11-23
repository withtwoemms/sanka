from unittest import TestCase

from sanka import Sanka


class SankaTest(TestCase):

    def test_can_count_function_calls(self):

        @Sanka
        def function():
            pass

        num_calls = 10

        for i in range(num_calls):
            function()

        assert function('ya dead?') == num_calls

