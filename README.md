# About
This project provides a solution to store and manage large data files for use with the Mindstorms Robot Inventor Hub and Spike Prime Hub via their official apps. It has been tested with the SPIKE Legacy firmware and app.

> [!IMPORTANT]
> Spike Prime Disclaimer:
> This concept has been tested only with SPIKE Legacy app and firmware on the Mindstorms hub.
> I haven't had the opportunity to test this concept with the SPIKE 3.

# How to load data file into the Hub:

1.	Create a Python Project with MINDSTORMS app or SPIKE Legacy app.
2.	Delete any existing data within the project.
3.	Input or paste your data.
4.	Select slot and download or run the Project: ![Uploading data into the Hub](https://github.com/GizmoBricks/get_slots_paths/assets/127412675/48f68cbe-36fd-41db-8d46-8f3cd528236a)

> [!NOTE]
> If you choose to press 'Play', the app console return a SyntaxError. This is normal and the file will still be stored on the hub.
> ![SyntaxError](https://github.com/GizmoBricks/get_slot_path/assets/127412675/79eaf3f6-2462-4473-94d1-ebb93c779ac1)
    	
5.	Verify the Stored File:
    - Press 'Open Hub connections', choose 'Programms' tab. Wait patiently until the program appears in the respective slot's line. ![Verifying the Stored File](https://github.com/GizmoBricks/get_slots_paths/assets/127412675/c3a86d4b-1fb0-4451-891f-c4be47b1bfd9)

  
> [!CAUTION]
> Do not disconect the hub during file uploading to avoid interruptions or data loss.

> [!IMPORTANT]
> During the file uploading process, the hub might not respond to any actions.

> [!NOTE]
> Larger data files might take some time to upload.
> For instance, a [file containing 1,000,000 digits of pi](/slot_3) took approximately 6 minutes to store.

# The `get_slots_paths` function

This function retrieves the paths associated with available slots from the `projects/.slots` file.

### Arguments
  
  - `extension` (`str`, optional): The file extension to append the path (default: `'.py'`).
  - `do_check` (`bool`, optional): Flag to indicate whether to perform a file format check (default: `False`).
  - `check_word` (`str`, optional): The word used for file format checking (default: empty string).

### Returns
  - `dict`: The dictionary of available slots and their paths, or empty dictionary, if no available slots.

## File format check:

If the `do_check` argument is `True`, the function compares the first word of the file with `check_word`.

If they match, the test is passed.

If they are different, that slot-path pair is excluded from the dictionary.


## Examples
### File reading
This [code](/get_slots_paths.py) demonstrates how to retrieve the file path associated with the slot number `0` and print the contents of the file if it exists and has a `'.py'` extension. It also handles errors that may occur during path retrieval.
``` python
def get_slots_paths(extension: str = '.py',
                    do_check: bool = False,
                    check_word: str = '') -> dict:
    # Rest of the get_slots_paths implementation...
    return sorted_slots_dict


slot_num = 0

paths = get_slots_paths()
if slot_num in paths:
    with open(paths[slot_num], 'r') as file:
        # Iterate through each line in the file and print its contents:
        for line in file:
            print(line)
else:
    print('Slot {} is empty.'.format(slot_num))
```
Output:

![The result of running the example in the console](https://github.com/GizmoBricks/get_slots_paths/assets/127412675/4005aa95-a8c8-47f9-a44f-fcebb11a656a)

To run this example:
* Upload [this file](/get_slots_paths.py) into slot #19.
* Upload [this data](/slot_0) into slot #0 and run program from slot #19.

### Count occurancy in a large file
This [code](/the_first_1,000,000_digits_of_pi.py) demonstrates how to retrieve the file path associated with the slot number `3`, count and print the occurrences of `'2024'` within data file from the third slot.
``` python
# If you are using SPIKE Legacy, uncomment the spike imports
# and comment out the Mindstorms imports:

# from spike.controls import Timer
from mindstorms.control import Timer


def get_slots_paths(extension: str = '.py',
                    do_check: bool = False,
                    check_word: str = '') -> dict:
    # Rest of the get_slots_paths implementation...
    return sorted_slots_dict


timer = Timer()
timer.reset()

slot_num = 3
word_to_search = '2024'
paths = get_slots_paths()

rest_of_line = ''
number_of_occurrences = 0

if slot_num in paths:
    print('It may take a wail...\nPlease wait.')
    with open(paths[slot_num], 'r') as file:
        # Iterate through each line in the file and print its contents:
        for line in file:
            line_ = rest_of_line + line.replace(' ', '').rstrip()
            number_of_occurrences = number_of_occurrences + line_.count(
                word_to_search)
            rest_of_line = line_[-3:]
    minutes, seconds = divmod(timer.now(), 60)

    print(' \n{} occurs {} times in the first 1,000,000 digits of pi'.format(
        word_to_search, number_of_occurrences))
    print('It took: {}:{:02}'.format(minutes, seconds))
else:
    print('Slot {} is empty.'.format(slot_num))
```
Output:

![The result of running the example in the console](https://github.com/GizmoBricks/get_slots_paths/assets/127412675/e948c489-2bbe-417d-8728-07a90ce132b7)

To run this example:
* Upload [this file](/the_first_1,000,000_digits_of_pi.py) into slot #19.
> [!IMPORTANT]
> If you are using SPIKE Legacy, uncomment the Spike imports and comment out the Mindstorms imports.
> ``` python
> from spike.controls import Timer
> # from mindstorms.control import Timer
> ```
* Upload [this data](/slot_3) into slot #3 and run program from slot #19.
> [!NOTE]
> It may take approximately 6 minutes to store.
