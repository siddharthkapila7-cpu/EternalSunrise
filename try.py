code = """
print("hello,
    """


try:
    exec(code)
except IndentationError:
    print("This is so funny, my code just ran code")