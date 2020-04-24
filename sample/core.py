# -*- coding: utf-8 -*-
# from . import helpers
#
# def get_hmm():
#     """Get a thought."""
#     return 'hmmm...'
#
#
# def hmm():
#     """Contemplation..."""
#     if helpers.get_answer():
#         print(get_hmm())

import edn_format
import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
file = "../definition.edn"
full_file_path = os.path.join(script_dir, file)


def main():
    f = open(full_file_path, "r")
    contents = f.read()
    print(edn_format.loads(contents))


main()
