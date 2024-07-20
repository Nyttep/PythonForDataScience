def NULL_not_found(object: any) -> int:
	nulls = {
		type(None): "Nothing",
		float: "Cheese",
		int: "Zero",
		str: "Empty",
		bool: "Fake"
	}

	if type(object) in nulls and (not object or object != object): # checking if type is in dict and if object is False or NaN
		print(nulls[type(object)], ":", object, type(object))
		return 0
	else:
		print("Type not Found")
		return 1