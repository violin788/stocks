import platform
for item in dir(platform):
    value = getattr(platform, item)
    if callable(value):
        try:
            result = value()
            print(f"{item}(): {result}")
        except Exception as e:
            print(f"{item}(): <function> (Error: {e})")
    else:
        print(f"{item}: {value}")

print(platform.node())