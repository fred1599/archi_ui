import sys
from importlib import import_module

try:
    option = sys.argv[1]
except IndexError:
    sys.exit("Ajouter une option tk ou qt")

if option in ("tk", "qt"):
    module = f"main_{option}"
    import_module(module)
else:
    sys.exit(f"L'option {option} n'existe pas, seulement (tk ou qt)")
