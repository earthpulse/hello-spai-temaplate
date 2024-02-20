from spai.storage import Storage

storage = Storage()

data = storage["data"]

data.create("Hello, SPAI!", "hello.txt")

print("Hello, SPAI!")

print(data.list())
