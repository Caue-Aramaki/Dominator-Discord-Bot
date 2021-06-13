def log_history(last_n=None, input_list=None):

  try:
    if last_n is not None:
      number = int(last_n)
    else:
      number = int(input_list[0])
      
    history_string = open("history.txt", 'r').read()

    log_list = history_string.split('\n')
    log_string = ''

    length = len(log_list)

    for i in range(length - int(number), length):
      log_string = log_string + "\n" + log_list[i]

    return log_string
  
  except Exception as problem:
    return "Error at log_history: " + str(problem)