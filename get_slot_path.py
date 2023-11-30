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


# This code snippet demonstrates how to retrieve
# the file path associated with a given slot number and print
# the contents of the file if it exists and has a '.py' extension.
# It also handles errors that may occur during path retrieval.
slot_num = 0
try:
    path = get_slot_path(slot_num)
except (RuntimeError, OSError) as error:
    # Handle errors that may occur during path retrieval:
    print('ERROR: {}'.format(error))
else:
    # If the path retrieval was successful, attempt to open the file:
    with open(path, 'r') as file:
        # Iterate through each line in the file and print its contents:
        for line in file:
            print(line)
