# If you are using SPIKE Legacy, uncomment the spike imports
# and comment out the Mindstorms imports:

# from spike.controls import Timer
from mindstorms.control import Timer


def get_slots_paths(extension: str = '.py',
                    do_check: bool = False,
                    check_word: str = '') -> dict:
    """
    This function retrieves the paths associated with available slots
    from the projects/.slots file.

    Args:
    - extension (str, optional): The file extension to append the path
                                 (default: '.py').
    - do_check (bool, optional): Flag to indicate whether to perform
                                 a file format check (default: False).
    - check_word (str, optional): The word used for file format checking
                                  (default: empty string).

    Returns:
    - dict: The dictionary of available slots and their paths,
            or empty dictionary, if no available slots.

    File format check:
    If the do_check argument is True, the function compares
    the first word of the file with check_word.
    If they match, the test is passed.
    If they are different, that slot-path pair is excluded
    from the dictionary.

    Note: the function was tested with Mindstorms app
    and SPIKE Legacy app on Mindstorms hub.
    If you can test it with SPIKE 3 app on the Spike Prime hub,
    please, give me feedback (GizmoBricksChannel@gmail.com)
    """
    with open('projects/.slots', 'r') as slots_file:
        slots_dict = eval(slots_file.readline())

    for key in slots_dict:
        slots_dict[key] = 'projects/{}/__init__{}'.format(
            slots_dict[key]['id'], extension)

        try:
            with open(slots_dict[key], 'r') as test_file:
                if test_file.readline().split()[0] != check_word and do_check:
                    del slots_dict[key]
        except OSError:
            del slots_dict[key]

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
