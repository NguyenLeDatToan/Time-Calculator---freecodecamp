# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main
# from test import add_time


# print(add_time("3:00 PM", "3:10"), '\n')
# print(add_time("11:30 AM", "2:32", "Monday"), '\n')
# print(add_time("11:43 AM", "00:20"), '\n')
# print(add_time("10:10 PM", "3:30"), '\n')
# print(add_time("11:43 PM", "24:20", "tueSday"), '\n')
# print(add_time("6:30 PM", "205:12"), '\n')
# print(add_time("8:16 PM", "466:02", "tuesday"), '\n')
# print(add_time("2:59 AM", "24:00", "saturDay"), '\n')


# Run unit tests automatically
main(module='test_module', exit=False)