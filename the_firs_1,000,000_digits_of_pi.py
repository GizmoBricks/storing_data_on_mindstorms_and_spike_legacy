# If you are using SPIKE Legacy, uncomment the spike imports
# and comment out the Mindstorms imports:

# from spike.controls import Timer
from mindstorms.control import Timer


def get_slot_path(slot: int = 0,
                  extension: str = '.py',
                  do_check: bool = False,
                  check_word: str = '') -> str:
    """
    Retrieve the path associated with a given slot number
    from the 'projects/.slots' file.

    Args:
    - slot (int, optional): The slot number (0-19 inclusive) to retrieve
                            the path for (default: 0).
    - extension (str, optional): The file extension to append the path
                                (default: '.py').
    - do_check (bool, optional): Flag to indicate whether to perform
                                a file format check (default: False).
    - check_word (str, optional): The word used for file format checking
                                (default: empty string).

    Returns:
    - str: The path corresponding to the provided slot number.

    Raises:
    - ValueError: If the slot is not within
                the range 0-19 (both inclusive).
    - RuntimeError: If the slot is empty.
                    If the file format check fails.
    - OSError: If the file extension is different
            from the extension argument.

    Note: the function was tested with Mindstorms app
    and SPIKE Legacy app on Mindstorms hub.
    If you can test it with SPIKE 3 app on the Spike Prime hub,
    please, give me feedback (GizmoBricksChannel@gmail.com)
    """

    if not (0 <= slot <= 19):
        raise ValueError('Slot is not in the range 0-19 (both inclusive).\n'
                         'Check the slot argument. It is {}, '
                         'but it should be in range [0-19].'.format(slot))

    with open('projects/.slots', 'r') as slots_file:
        slot_data = eval(slots_file.readline()).get(slot)
    if slot_data:
        path = 'projects/{}/__init__{}'.format(slot_data('id'), extension)

        # open() can reach OSError, if the file extension is different
        # from the extension argument.
        with open(path) as file:
            if file.readline().split()[0] != check_word and do_check:
                raise RuntimeError('File format check failed.')
        return path
    else:
        raise RuntimeError('Slot {} is empty.\nTry to upload file again, '
                           'or try another slot.'.format(slot))


def seconds_to_time(seconds: int, mode: str = 'hh:mm:ss') -> str:
    """
    Converts a given number of seconds into a specified time format.

    Args:
    - seconds (int): The number of seconds to be converted.
    - mode (str): The desired time format mode. (default: 'hh:mm:ss')
    Allowed modes are: 'mm:ss', 'hh:mm:ss', 'D.hh:mm:ss', 'hh:mm',
                        'D.hh:mm'.

    Returns:
    - str: A string representing the time in the specified format.

    Raises:
    - ValueError: If the provided mode is not one of the allowed modes.
    """

    valid_modes = ('mm:ss', 'hh:mm:ss', 'D.hh:mm:ss', 'hh:mm', 'D.hh:mm')
    if mode not in valid_modes:
        raise ValueError(
            "Invalid mode. Allowed modes are: {}".format(valid_modes)
        )

    days = hours = minutes = 0

    if 'D' in mode:
        days, seconds = divmod(seconds, 86400)  # 86400 sec in a day

    if 'hh' in mode:
        hours, seconds = divmod(seconds, 3600)  # 3600 sec in an hour

    # It is allways True. It is here in case valid_modes changes.
    if 'mm' in mode:
        minutes, seconds = divmod(seconds, 60)

    if seconds >= 30 and 'ss' not in mode:
        minutes += 1

    time_format = mode.replace('D', str(days))
    time_format = time_format.replace('hh', "{:02}".format(hours))
    time_format = time_format.replace('mm', "{:02}".format(minutes))
    time_format = time_format.replace('ss', "{:02}".format(seconds))

    return time_format


timer = Timer()
timer.reset()

slot_num = 3
word_to_search = '2024'

path = get_slot_path(slot_num)
rest_of_line = ''
number_of_occurrences = 0

with open(path, 'r') as file:
    for line in file:
        line_ = rest_of_line + line.replace(' ', '').rstrip()
        number_of_occurrences = number_of_occurrences + line_.count(
            word_to_search)
        rest_of_line = line_[-3:]

time = timer.now()

print('{} occurs {} times in the first 1,000,000 digits of pi'.format(
    word_to_search, number_of_occurrences))
print('It took: {}'.format(seconds_to_time(time)))
