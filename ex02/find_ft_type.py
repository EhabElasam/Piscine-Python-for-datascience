def all_thing_is_obj(object: any) -> int:

    type_name = type(object).__name__
    if isinstance(object, str): #and object in ["Brian", "Toto"]:
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
 