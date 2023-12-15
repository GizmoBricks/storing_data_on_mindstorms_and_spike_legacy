def get_slots_paths(extension: str = '.py',
                    do_check: bool = False,
                    check_word: str = '') -> dict:
    """
    This function retrieves the paths associated with available slots
    from the projects/.slots file.

    Args:
    - extension (str, optional): The file extension to append the path.
                                 Valid values: '.py', '.mpy'.
                                 (default: '.py').
    - do_check (bool, optional): Flag to indicate whether to perform
                                 a file format check (default: False).
    - check_word (str, optional): The word used for file format checking
                                  (default: empty string).

    Returns:
    - dict: The dictionary of available slots and their paths,
            or empty dictionary, if no available slots.

    Raises:
        ValueError if extension is not one of valid values:
        '.py', '.mpy'.

    File format check:
    If the do_check argument is True, the function compares
    the first word of the file with check_word.
    If they match, the test is passed.
    If they are different, that slot-path pair is excluded
    from the dictionary.

    Note: this function does not work with SPIKE 3.
    """
    valid_extensions = '.py', '.mpy'
    if extension not in valid_extensions:
        raise ValueError('Extension is not one of valid extensions: {}.'
                         ''.format(valid_extensions))

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

    return slots_dict


slot_num = 3
paths = get_slots_paths()

if slot_num in paths:
    print('It may take a wail...\nPlease wait.')
    number_of_occurrences = [0 for _ in range(10)]
    with open(paths[slot_num], 'r') as file:
        next(file)  # skip first line
        for line in file:
            for i in range(10):
                number_of_occurrences[i] += line.count(str(i))

    for i in range(10):
        print('{} occurs {} times.'.format(i, number_of_occurrences[i]))
    print('Total: {}'.format(sum(number_of_occurrences)))

else:
    print('Slot {} is empty.'.format(slot_num))
