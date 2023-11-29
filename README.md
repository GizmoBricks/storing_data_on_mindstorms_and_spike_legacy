# About
This projecty provides a solution to store and manage large data files for use with the Mindstorms Robot Inventor Hub and Spike Prime Hub via their official apps. It has been tested with the SPIKE Legacy firmware and app.

> [!IMPORTANT]
> Spike Prime Disclaimer:
> This concept has been tested only with SPIKE Legacy app and firmware on the Mindstorms hub.
> I haven't had the opportunity to test this concept with the SPIKE 3.

# How to load data file into the Hub:

1.	Create a Python Project with MINDSTORMS app or SPIKE Legacy app.
2.	Delete any existing data within the project.
3.	Input or paste your data.
4.	Select slot and download or run the Project:
    - Select the appropriate slot on the hub and press the 'Download' button. Alternatively, you can press the 'Run' button.
> [!NOTE]
> If you choose to press 'Run,' the app console return a SyntaxError. This is normal and the file will still be stored on the hub.
    	
5.	Verify the Stored File:
    - Navigate to Hub -> Programs. Wait patiently until the program appears in the respective slot's line.
  
> [!CAUTION]
> Do not disconect the hub during file uploading to avoid interruptions or data loss.

> [!IMPORTANT]
> During the file uploading process, the hub might not respond to any actions.

> [!NOTE]
> Larger data files might take some time to upload.
> For instance, a file containing 1,000,000 digits of pi took approximately 5 and a half minutes to store.

# The `get_slot_path` function

The function retrieve the path associated with a given slot number from the `projects/.slots` file.

### Arguments
  
  - `slot` (`int`, optional): The slot number (0-19 inclusive) to retrieve the path for (default: `0`).
  - `extension` (`str`, optional): The file extension to append the path (default: `'.py'`).
  - `do_check` (`bool`, optional): Flag to indicate whether to perform a file format check (default: `False`).
  - `check_word` (`str`, optional): The word used for file format checking (default: empty string).

### Returns
  - `str`: The path corresponding to the provided slot number.

### Raises
  - `ValueError`: If the slot is not within the range 0-19 (both inclusive).
  - `RuntimeError`: If the slot is empty. If the file format check fails.
  - `OSError`: If the file extension is different from the extension argument.
  - 
## Validation process in the `get_slot_path` function

When the `do_check` argument is set to `False` and a file exists for a specified slot, the function promptly returns the path to that file.

If the `do_check` argument is set to `True` and a file exists for the given slot, the function performs an additional validation process. 

It opens the file and reads its first line. Subsequently, it compares the first word from this line with the provided `check_word` argument. If the first word matches the `check_word` argument, indicating a successful check, the function proceeds to return the path to the file. However, if there's a mismatch, signifying a failed check, the function raises a `RuntimeError`.


## Example
This code snippet demonstrates how to retrieve the file path associated with the slot number `0` and print the contents of the file if it exists and has a `'.py'` extension. It also handles errors that may occur during path retrieval.
```
def get_slot_path...

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
```
