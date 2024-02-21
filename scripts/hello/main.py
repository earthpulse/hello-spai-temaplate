from spai.storage import Storage
from spai.config import SPAIVars

storage = Storage()
vars = SPAIVars()

data = storage["data"]

data.create(vars["message"], "hola.txt")

print("Files in storage", data.list())
print("Variables", vars)
