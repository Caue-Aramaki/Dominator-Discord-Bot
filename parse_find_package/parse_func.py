def parse_functions(input_string):
  try:
    if input_string.find(",") == -1 and input_string.find("(") == -1:
      return [input_string]
    else:
      # We need to separate the commas from 1, 3, add(1, 3), 2, add(3), but no the ones inside parenthesis!!
      new_string = input_string.replace(" ", "") #get rid of spaces
      temp_string = ""
      parenthesis_counter = 0

      for index in range(len(new_string)): # lets get rid of the commas outside the func
        if new_string[index] == "(":
          parenthesis_counter += 1
        if new_string[index] == ")":
          parenthesis_counter -= 1
        
        if parenthesis_counter == 0 and new_string[index] == ",": # if its a comma outside the func, replace it with ;
          temp_string += ";"
        else:
          temp_string += new_string[index]
      # end
      temp_list =  temp_string.split(";")

      new_list = []
      new_string = ""

      for string in temp_list: # for every string in the new list, lets extract the parameters on each of them

        if string.find("(") == -1:
          output_list = string
          new_list.append(output_list)
        else:
          output_list = []
          count = 0
          temp = ""
          detect_function = ""
          temp_function = ""

          for character_index in range(0, len(string)): # for each string lets iterate and extract features
            if count == 0:
              detect_function += string[character_index]
            if string[character_index] == ")":
              count -= 1
            if count > 0:
              temp += string[character_index]
            else:
              if len(temp) > 0:
                output_list.append([temp_function.replace("(", ""), temp]) # add the params to the list
                temp = ""
                temp_function = ""
            if string[character_index] == "(":
              count += 1
            if count == 1:
              temp_function += detect_function
              detect_function = ""
          # end of loop
          new_list.append(output_list[0])
      # end of loop

      output_list = new_list

      for index in range(0, len(new_list)):
        if type(new_list[index]) == list:
          output_list[index][1] = parse_functions(new_list[index][1])

      return output_list

  except Exception as problem:
    return problem