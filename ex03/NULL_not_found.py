def NULL_not_found(object: any) -> int:

    # NaN
    if isinstance(object, float) and object != object:
        print(f"Cheese: nan <class 'float'>")
        return 0

    # false or 0
    if object is False:
        print("Fake: False <class 'bool'>")
        return 0
    if object == 0:
        print("Zero: 0 <class 'int'>")
        return 0

    # 'Null'-Typen
    null_types = {
        None: "Nothing: None",
        '': "Empty: "
    }

    # NULL check
    for null_type, message in null_types.items():
        if object is null_type:
            print(f"{message} <class '{type(object).__name__}'>")
            return 0

    print("Type not Found")
    return 1
