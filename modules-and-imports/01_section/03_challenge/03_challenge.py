# Create a greeting variable for the mentor using the data imported from the nested files
# Print the greeting to your terminal

# It should look something like "Good afternoon Simon Jackson!"

from data.file_1 import mentor_first_name
from data.file_2 import mentor_last_name

#import importlib.util

#spec = importlib.util.spec_from_file_location('file_1', 'modules-and-imports/01_section/03_challenge/file_1.py')
#file_1 = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(file_1)
#first_name = file_1.mentor_first_name

#spec_2 = importlib.util.spec_from_file_location('file_2', 'modules-and-imports/01_section/03_challenge/file_2.py')
#file_2 = importlib.util.module_from_spec(spec_2)
#spec_2.loader.exec_module(file_2)
#last_name = file_2.mentor_last_name


print(f"Good afternoon {mentor_first_name} {mentor_last_name}!")