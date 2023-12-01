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
        path = 'projects/{}/__init__{}'.format(slot_data.get('id'), extension)

        # open() can reach OSError, if the file extension is different
        # from the extension argument.
        with open(path) as file:
            if file.readline().split()[0] != check_word and do_check:
                raise RuntimeError('File format check failed.')
        return path
    else:
        raise RuntimeError('Slot {} is empty.\nTry to upload file again, '
                           'or try another slot.'.format(slot))


timer = Timer()
timer.reset()

slot_num = 3
word_to_search = '2024'

path = get_slot_path(slot_num)
rest_of_line = ''
number_of_occurrences = 0

print('It may take a wail...\nPlease wait.')

with open(path, 'r') as file:
    for line in file:
        line_ = rest_of_line + line.replace(' ', '').rstrip()
        number_of_occurrences = number_of_occurrences + line_.count(
            word_to_search)
        rest_of_line = line_[-3:]

minutes, seconds = divmod(timer.now(), 60)

print('{} occurs {} times in the first 1,000,000 digits of pi'.format(
    word_to_search, number_of_occurrences))
print('It took: {}:{:02}'.format(minutes, seconds))
