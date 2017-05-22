import sys


def activate_virtual_env(path=None, arg='--venv'):
    """ 
     Activate Python Virtual Environment (virtualenv) within other python interpreter /or default interperter
     @param path: An absolute path to virtual environment folder. 
     @param arg: an argument to parse virtual environment's absolute path, not used if param path is specified 
     @return: True if activation success, False otherwise 
    """
    activate_this = "/bin/activate_this.py"
    path_to_venv = None

    if path is not None or len(sys.argv) > 1:
        try:
            # Non-restrict arg parse
            args = sys.argv[1:]
            path_to_venv = path.rstrip('/') if path is not None else args[args.index(arg) + 1].rstrip('/')
            activate_this = path_to_venv + activate_this
            print "Activate Python Virtual Environment at: " + str(path_to_venv)
            execfile(activate_this, dict(__file__=activate_this))
            return True
        except ValueError:
            print "WARNING: No input path to Virtual ENV, will use default python"
            return False
        except IOError:
            print "WARNING: Wrong Input Path to Virtual ENV, will use default python"
            return False
    else:
        print "WARNING: No input path to Virtual ENV, will use default python"
        return False
