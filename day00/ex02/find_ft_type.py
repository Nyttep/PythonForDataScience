def all_thing_is_obj(object: any) -> int:
	if isinstance(object, str): # check if object is a string
		print(f"{object.capitalize()} is in the kitchen :", type(object))
	else: # if object is not a string
		print("{} :".format(str(type(object)).split("'")[1].capitalize()), type(object))
	return 42