def all_thing_is_obj(object: any) -> int:
    """
    Diese Funktion nimmt ein beliebiges Objekt und druckt seinen
    Typ in einer speziellen Formatierung. Sie gibt immer 42 zurück,
    es sei denn, der Typ ist nicht gefunden.
    """
    type_name = type(object).__name__
    if isinstance(object, str):
        print(f"{object} is in the kitchen : <class '{type_name}'>")
    else:
        type_msg = {
            list: "List",
            tuple: "Tuple",
            set: "Set",
            dict: "Dict"
        }.get(type(object), "Type not found")

        if type_msg == "Type not found":
            print(type_msg)
            return 42
        else:
            print(f"{type_msg} : <class '{type_name}'>")

    return 42
