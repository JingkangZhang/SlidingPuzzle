import base64
f = open("puzzle.py", "rb")
encoded = base64.b64encode(f.read())
f = open("encoded.py", "wb")
f.write(bytes("import base64\nmyscript ='''", 'utf-8'))
f.write(encoded)
f.write(bytes("'''\n", 'utf-8'))
f.write(bytes("""eval(compile(base64.b64decode(myscript),'<string>','exec'))""",'utf-8'))
f.close()
