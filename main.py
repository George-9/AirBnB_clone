#!/usr/bin/env python3

import Popen

"""
    this is a shell scripting module
"""
def main():
    """
        excecute bash commands
    """
    with Popen(["/bin/bash"], stdout=PIPE) as result:
        print(result.stdout.read())

if __name__ == 'main':
    main()
