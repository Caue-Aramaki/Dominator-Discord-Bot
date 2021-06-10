def hi(input=None, input_list=None):
  try:
    return "Hello!"
  except Exception as problem:
    return "Oh boi, error at hi: " + str(problem)

def wish_rate_genshin(input=None, input_list=None):
  try:
    from custom_packages.genshin_package.wish_rate import calculate_constellation_rate

    if input is not None:
      return calculate_constellation_rate(float(input))
    else:
      return calculate_constellation_rate(float(input_list[0]))

  except Exception as problem:
    return "Error at wish_rate_genshin: " + str(problem)