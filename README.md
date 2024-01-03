# About
This project provides a solution to store and manage large data files 
for use with the Mindstorms Robot Inventor Hub and Spike Prime Hub 
via their official apps.
It has been tested with the SPIKE Legacy firmware and app.

> [!IMPORTANT]
> This method doesn't work with Spike 3.
> [Here](https://github.com/GizmoBricks/storing_data_on_spike_3) 
> solution for Spike 3.

# An "exploit"

If a project doesn't contain any Syntax Errors, 
it will be precompiled by the app into a MicroPython `.mpy` file 
and stored in the Hub.

A MicroPython file is a binary file. 
More importantly, as it's a pre-compiled file, 
its content will differ from the original file.


However, if a project contains any Syntax Errors, 
it'll be stored in the Hub as a regular Python `.py` file, 
essentially a text file.
Text files are easily navigable using Python. 
This method capitalizes on this “exploit”.

# Project Storage in the Hub

All projects reside in the `/projects/` directory, 
each having its own directory. 
These directories are labeled with specific digits, 
acting as unique IDs. All these IDs are recorded in the `.slots` file.

The full path to a project file looks like this: 
`/projects/{ID}/__init__.mpy` for SyntaxError-free files
or `/projects/{ID}/__init__.py` for files with any SyntaxErrors. 
This path is stored within the `__file__` variable.

How to print this variable:
```python
print(__file__)
```

The ID of each project changes every time you run or upload the program
from the app. However, this ID remains unchanged 
if you run the program directly from the Hub.

The `.slots` file can be read with this code:
```python
with open('projects/.slots', 'r') as file:
    for line in file:
        print(line)
```
Output:

![The ` slots` file content](https://github.com/GizmoBricks/get_slots_paths/assets/127412675/c1bac7d6-a951-4d20-8d7f-5084e07adff1)

The `.slots` file structure resembles a typical Python dictionary
— a dictionary of dictionaries, to be precise.

The top-level dictionary includes all available slots as keys 
and dictionaries of project attributes as values.

These secondary-level dictionaries contain project attributes such as:
  - the project's name in Base64 format
  - the project's ID
  - Unix timestamps of modification and creation
  - the project folder's name (ID)
  - the project type. It is “scratch” for “Word Blocks” projects 
    and “python” for Python projects.

The `.slots` file can be utilized to access paths 
for all programs available on the Hub.

# Uploading Data Files to the Hub

1.	Create a Python Project with the MINDSTORMS or SPIKE Legacy apps.
2.	Delete any existing data within the project.
3.	Input or paste your data.
4.	Select a slot and upload or run the Project: 
    ![Uploading data into the Hub](https://github.com/GizmoBricks/get_slots_paths/assets/127412675/b80a6d0c-0ce9-42ef-b7c7-075e3136e513)

> [!NOTE]
> If you choose to press 'Play', the app console returns a SyntaxError. 
> This is normal and the file will still be stored on the hub.
> ![SyntaxError](https://github.com/GizmoBricks/get_slot_path/assets/127412675/79eaf3f6-2462-4473-94d1-ebb93c779ac1)
    	
5.	Verify the Stored File:
    - Press 'Open Hub connections' and choose the 'Programs' tab. 
    Wait patiently until the program appears in the respective slot's line. 
    ![Verifying the Stored File](https://github.com/GizmoBricks/get_slots_paths/assets/127412675/0f3f936a-1ae9-45d0-9b5d-7cdd05d86b29)
  
> [!CAUTION]
> Do not disconnect the hub during file uploading to avoid 
> or data loss.

> [!IMPORTANT]
> During the file uploading process, the hub might not respond to any actions.

> [!NOTE]
> Larger data files might take some time to upload.
> For instance, a [file containing 1,000,000 digits of pi](/examples/slot_3)
> took approximately 6 minutes to store.

# The `get_data_paths` function

[This function](/get_data_paths.py) retrieves the paths associated 
with available slots with '.py' files from the `projects/.slots` file.

### Arguments

  - `do_check` (`bool`, optional): Flag to indicate whether to perform 
    a file format check (default: `False`).
  - `check_word` (`str`, optional): The word used for file format checking 
    (default: empty string).

### Returns
  - `dict`: The dictionary of available slots and their paths, 
    or empty dictionary, if no available slots.
> [!NOTE]
> The dictionary is not sorted.

### What the function exactly does

The `get_data_path` function converts the `.slots` file data into 
a dictionary using the `eval()` function. 
For each available slot in the dictionary, it replaces the value, 
a dictionary of project attributes, with the path to the project file.

The function then applies a two-step check of the file.

1. The first step tries to open the file, and if successful, 
   the first step passes. If an `OSError` occurs, 
   the slot number – path pair is deleted from the dictionary.
   It filters out files with extensions different from `.py`.

2. Second check step (file format check):
* If the `do_check` argument is `True`, 
  the function compares the first word of the file with `check_word`.
* If they match, the test is passed.
* If they are different, that slot-path pair is excluded from the dictionary.


## Examples
### File reading
This code demonstrates how to retrieve 
the file path associated with the slot number `0` and print the contents 
of the file, if it exists and has a `.py` extension. 
```python
def get_data_paths(do_check: bool = False, check_word: str = '') -> dict:
    # Rest of the function implementation...
    return paths_dict


slot = 0

paths = get_data_paths()
if slot in paths:
    with open(paths[slot], 'r') as file:
        # Iterate through each line in the file and print its contents:
        for line in file:
            print(line)
else:
    print("Slot {} is empty or this slot contains precompiled '.mpy' file."
          "".format(slot))
```
Output:

![The result of running the example in the console](https://github.com/GizmoBricks/get_slots_paths/assets/127412675/956944d6-64e3-4cc7-a640-525742b62f01)

To run this example:
* Upload [this data](/examples/slot_0) into slot #0.
* Upload [this code](/examples/file_content_reading.py) into slot #19.
* Run the program from slot #19.

### Count occurrences in a large file
This code demonstrates how to retrieve 
the file path associated with the slot number `3`, 
count and print the occurrences of each digit (0-9) within the data file 
from the third slot.
```python
def get_data_paths(do_check: bool = False, check_word: str = '') -> dict:
    # Rest of the function implementation...
    return paths_dict


slot = 3
paths = get_data_paths()

if slot in paths:
    print('It may take a wail...\nPlease wait.')
    number_of_occurrences = [0 for _ in range(10)]
    
    with open(paths[slot], 'r') as file:
        # Skip the first line to avoid counting '3' before the decimal point:
        next(file)
        
        for line in file:
            for i in range(10):
                number_of_occurrences[i] += line.count(str(i))

    for i in range(10):
        print('{} occurs {} times.'.format(i, number_of_occurrences[i]))
    print('Total: {}'.format(sum(number_of_occurrences)))

else:
    print("Slot {} is empty or this slot contains precompiled '.mpy' file."
          "".format(slot))
```
Output:

![The result of running the example in the console](https://github.com/GizmoBricks/get_slots_paths/assets/127412675/ae995cf9-50ab-42d7-b8e5-5684632cc7cb)

To run this example:
* Upload [this data](/examples/slot_3) into slot #3.
* Upload [this file](/examples/occurrences_counting.py) into slot #19.
* Run the program from slot #19.
> [!NOTE]
> It may take approximately 6 minutes to store data and 2 and a half minutes 
> to complete the program.
