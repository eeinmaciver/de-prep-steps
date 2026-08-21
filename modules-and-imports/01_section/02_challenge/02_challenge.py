#  Using the data stored in the nested file_1.py create a mentor_name variable
#  which stores the mentor name.

#  Make sure you print only the name, not the whole dictionary!

import importlib.util

spec = importlib.util.spec_from_file_location('file_1', 'modules-and-imports/01_section/01_challenge/file_1.py')
file_1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(file_1)
mentor_name = file_1.mentor

print(mentor_name)