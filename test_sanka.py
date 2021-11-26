from unittest import TestCase

from sanka import Sanka
from sanka import YaDead


class SankaTest(TestCase):

    def test_count_calls_for_no_arg_function(self):

        @Sanka
        def function():
            pass

        num_calls = 2

        for i in range(num_calls):
            function()

        assert function(YaDead) == num_calls

    def test_count_calls_for_function_with_args(self):

        @Sanka
        def function(takes, some_args):
            pass

        num_calls = 2

        for i in range(num_calls):
            function('takes', 'some_args')

        assert function(YaDead) == num_calls

    def test_count_calls_for_multiple_functions(self):

        @Sanka
        def function1():
            pass
        @Sanka
        def function2():
            pass

        num_calls_for_first_function = 2
        num_calls_for_second_function = 3

        for i in range(num_calls_for_first_function):
            function1()
        for i in range(num_calls_for_second_function):
            function2()

        assert function1(YaDead) == num_calls_for_first_function
        assert function2(YaDead) == num_calls_for_second_function

