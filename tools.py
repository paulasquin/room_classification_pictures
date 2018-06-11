import subprocess
import os


def get_files_names(extension, path=""):
    """" Send a list of file with given extension under given (optional) path.
    Path can be relative or absolute
    example : '.pgm', 'carte' """
    p = subprocess.Popen(["ls", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', extension], stdin=p.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    p.stdout.close()  # Allow proc1 to receive a SIGPIPE if proc2 exits.
    out, err = p2.communicate()
    names = out.decode('utf-8')
    names = names.split('\n')
    names.pop()  # We delete last, empty, element
    return names


def get_subfolders(path=""):
    # If relative path is given, we transform it to absolute path
    path = relative_to_absolute_path(path)

    p = subprocess.Popen(["ls " + path], stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    subfolders = out.decode('utf-8')
    subfolders = subfolders.split('\n')
    subfolders.pop()  # We delete last, empty, element
    return subfolders


def relative_to_absolute_path(path=""):
    # Check if not already absolute path
    if path=="":
        path = os.getcwd()
    elif path[0] != "/":
        path = os.getcwd() + "/" + path
    return path


def locate_files(extension, path="", dbName="locate"):
    print("Creating the database \"" + dbName + ".db\" for the \"local\" command")
    print("Searching " + extension + " in " + path)
    subprocess.call(["updatedb -l 0 -o " + dbName + ".db -U " + os.getcwd() + "/"], shell=True)
    p = subprocess.Popen(["locate -d " + dbName + ".db " + relative_to_absolute_path(path) + "/*." + extension],
                         stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    paths = out.decode('utf-8')
    paths = paths.split('\n')
    paths.pop()  # We delete last, empty, element
    return paths


def getImage(filename, path=""):
    """" Load an image with given filename and path (optional) """
    if path != "":
        path += "/"
    return Image.open(path + filename)
