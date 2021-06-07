def linear(input=None, input_list=None):
  try:
    if input != None:
      return input
    else:  
      return input_list[0]
  except Exception as problem:
    return f"in linear(): {str(problem)}"