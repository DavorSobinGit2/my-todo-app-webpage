FILENAME = "todos.txt"


def read_files(filename=FILENAME):
    """
    :param filename: The file we are passing to read the lines and store them in a local variable local_contents
    :return: A list of contents that are inside the textfile
    """
    with open(filename, "r") as files:
        local_contents = files.readlines()
    return local_contents


def write_files(contents, filename=FILENAME):
    """
    :param contents: takes the contents of a list or string and writes them inside a textfile todos.txt
    :param filename: the file we are passing to write the contents inside of it.
    :return: None; just performing a writeln method on our file
    """
    with open(filename, "w") as files:
        files.writelines(contents)
