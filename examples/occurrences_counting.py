def get_data_paths(do_check: bool = False, check_word: str = '') -> dict:
    """
    This function retrieves the paths associated with available slots
    with '.py' files from the '/projects/.slots' file.
    The function ignores slots with successfully compiled programs -
    '.mpy' files.

    Args:
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

    Note: this function does not work with SPIKE 3.
    """
    with open('projects/.slots', 'r') as slots_file:
        paths_dict = eval(slots_file.readline())

    for key in paths_dict:
        paths_dict[key] = '/projects/{}/__init__.py'.format(
            paths_dict[key]['id'])

        try:
            with open(paths_dict[key], 'r') as test_file:
                # File format check:
                if test_file.readline().split()[0] != check_word and do_check:
                    del paths_dict[key]

        # If the file has '.mpy' extension - its slot-path pair will be deleted:
        except OSError:
            del paths_dict[key]

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
