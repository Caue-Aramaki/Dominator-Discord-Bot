def find_command(input_command, parameter_list, key_list):
  try:
    found = False

    for bucket in key_list:
      if bucket[0] == input_command:
        found = bucket[1]
    # we found our command, let us check if the parameter list has functions inside them.

    scalar_list = [] # we will use this as parameters instead, and pass values to it.

    for element in parameter_list:
      if type(element) == list:
        scalar_list.append(find_command(element[0], element[1], key_list)) # this is where our recursion is
      else:
        scalar_list.append(element)

    return found(input_list=scalar_list)
  
  except Exception as problem:
    return "Error in find_command: " + str(problem)
# end