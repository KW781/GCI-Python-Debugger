import sys
#function to be tested should be written HERE
def sample_function():
    b = 5 + 3
    exemplar_list = []
    exemplar_list.append(2)
    exemplar_list.append(42)
    exemplar_list.append(69)
    b = b * 5
#end of function
starting_line_number = 4 #starting line number of function being debugged (not including the function header), HAS TO BE changed appropriately by programmer depending on where they write the function


    
def trace_calls(frame, event, arg): #traces the call of the function to be tested
    if frame.f_code.co_name == "sample_function":
       return trace_lines #calls upon function 'trace_lines' for each frame

var_values = []
var_names = []
previous_line_number = 0 #global variable used later on to solve minor bug
def trace_lines(frame, event, arg):
    global var_values
    global var_names
    global previous_line_number

    if frame.f_lineno > starting_line_number: #checks that the appropriate line number is reached at the start so any new variables can be added to the dictionary
        if len(frame.f_locals) != len(var_values): #checks whether a new variable has been created
            #unpacks the names of the variables and the values of the variables from the dictionary 'frame.f_locals' into 2 separate global lists
            var_names = list(frame.f_locals.keys()) 
            var_values = list(frame.f_locals.values())
            var_name_changed = var_names[len(var_names) - 1]
            var_value_changed = var_values[len(var_values) - 1]
            if type(var_value_changed) is list:
                file = open("List Values.txt", "w")
                for i in range(len(var_value_changed)):
                    file.write(str(var_value_changed[i]) + "\n")
                file.close()
            #outputs the name and value of the new variable/list 
            print("Line " + str(frame.f_lineno - starting_line_number) + ": " + "Value of " + var_name_changed + " is assigned " + str(var_value_changed))  
        else:
            #this statement solves a minor bug where the same line number is output twice towards the end
            if frame.f_lineno == previous_line_number: 
                number_subtracted = starting_line_number - 1
            else:
                number_subtracted = starting_line_number
            #checks whether any previous variabls/lists have been changed
            temp_var_values = list(frame.f_locals.values())
            for i in range(len(temp_var_values)):
                if type(temp_var_values[i]) is list: #checks whether the current object being worked with is a list
                    change_in_list = output_list_changes(frame.f_lineno - number_subtracted, temp_var_values[i], var_names[i])
                    if change_in_list == True:
                        break
                elif temp_var_values[i] != var_values[i]:
                    print("Line " + str(frame.f_lineno - number_subtracted) + ": " + "Value of " + var_names[i] + " is changed from " + str(var_values[i]) + " to " + str(temp_var_values[i]))
                    break
            var_values = temp_var_values
            previous_line_number = frame.f_lineno
            




def output_list_changes(lineno, new_list_values, list_name):
    change_in_list = False
    old_list_values = []
    file = open("List Values.txt", "r")
    file_data = "####"
    while file_data != "":
        file_data = file.readline()
        if file_data != "":
            old_list_values.append(file_data)
    file.close()
    if len(new_list_values) > len(old_list_values):
        print("Line " + str(lineno) + ": element " + str(len(new_list_values) - 1) + " with a value of " + str(new_list_values[len(new_list_values) - 1]) + " added to list " + list_name)
        change_in_list = True
    file = open("List Values.txt", "w")
    for i in new_list_values:
        file.write(str(i) + "\n")
    file.close()
    return change_in_list

sys.settrace(trace_calls)
sample_function() #function to be tested is called

#the tuple 'frame.f_code.co_names' contains the names of the functions caled upon in 'sample_function'
#try writing the list values to a text file to save them; as strange as it may be
