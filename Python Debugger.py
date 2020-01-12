import importlib.util #library used to import modules by their file path
import sys
import timeit

if len(sys.argv) != 3:
    print("Error: Ensure that 3 arguments are provided. The first one is 'Python Debugger.py', which is the debugger. The second should be the function name and the third should be the program you want to debug")
    sys.exit()
global func_name
func_name = sys.argv[1]
file_path = sys.argv[2]
spec = importlib.util.spec_from_file_location("", file_path)
mod = importlib.util.module_from_spec(spec) 
spec.loader.exec_module(mod)
    

text_file = open("Debugger Output.txt", "w") #opens the text file for which the output is written to


def trace_calls(frame, event, arg): #traces the call of the function to be tested
    if frame.f_code.co_name == func_name:
        global starting_line_number
        starting_line_number = frame.f_lineno + 1
        return trace_lines #calls upon function 'trace_lines' for each frame

var_values = [] #list that stores the values of the current variables
var_names = [] #list that stores the names of the current variables 
var_data_types = [] #list that stores the data type of each variable, for it to be output at the end
var_line_numbers = [] #list that stores the line number on which each variable was instantiated on
record_of_values = [] #a list in which each element will be list, and each of these elements will record the values thaat each value was assigned throughout the debugging process, for it to be output at the end
line_counters = [] #each element keeps track of a particular line number and counts how many times it has run e.g. for a for loop
times = [] #a list in which each element is a list that tracks the time for each particular line to execute e.g. if line 3 was executed twice the element for line 3 will store the time for each of the 2 instances where the line was executed
overall_total = 0.0 #a running total to calculate how long the program took to execute
previous_line_number = 0 #global variable used later on to solve minor bug
step_number = 1 #global variable that is a step number output to the text file
def trace_lines(frame, event, arg):
    global var_values
    global var_names
    global var_data_types
    global var_line_numbers
    global record_of_values
    global times
    global overall_total
    global previous_line_number
    global step_number

    if frame.f_lineno > starting_line_number: #checks that the appropriate line number is reached at the start so any new variables can be added to the dictionary
        #this statement solves a minor bug where the same line number is output twice towards the end
        if frame.f_lineno == previous_line_number: 
           number_subtracted = starting_line_number - 1
        else:
            number_subtracted = starting_line_number
            
        if len(line_counters) - 1 < frame.f_lineno - number_subtracted - 1:
            line_counters.append(1) #adds a new element to line_counters if a new line has been reached i.e. not in a loop
            times.append([]) #adds a new list element to times so that the times of execution of this new line can be tracked
        else:
            line_counters[frame.f_lineno - number_subtracted - 1] += 1 #if an already existing line is being executed, then increment the appropriate element of line_counters           

        if len(frame.f_locals) != len(var_values): #checks whether a new variable has been created
            #unpacks the names of the variables and the values of the variables from the dictionary 'frame.f_locals' into 2 separate global lists
            var_names = list(frame.f_locals.keys()) 
            var_values = list(frame.f_locals.values())
            var_name_changed = var_names[len(var_names) - 1]
            var_value_changed = var_values[len(var_values) - 1]
            #checks the data type of the new variable and adds the data type of the new variable to var_data_types
            if type(var_value_changed) is int:
                var_data_types.append("Integer")
            elif type(var_value_changed) is float:
                var_data_types.append("Floating point")
            elif type(var_value_changed) is str:
                var_data_types.append("String")
            elif type(var_value_changed) is bool:
                var_data_types.append("Boolean")
            elif type(var_value_changed) is list:
                var_data_types.append("List")
            var_line_numbers.append(frame.f_lineno - number_subtracted) #a new variable has been created and therefore var_line_numbers needs to be appended with the line number this new variable was instantiated on
            record_of_values.append([]) #record_of_values also needs to be appended with a new list element to track the values this variable is assigned throughout the debugging of the program
            record_of_values[len(record_of_values) - 1].append(var_value_changed) #appends the appropriate list element of record_of_values with the value with which this new variable has been instantiated with
            #outputs the name and value of the new variable/list to both the console window and the text file
            text_file.write("Line " + str(frame.f_lineno - number_subtracted) + ", running " + str(line_counters[frame.f_lineno - number_subtracted - 1]) + " times: Value of " + var_name_changed + " is assigned " + str(var_value_changed) + "  " + str(overall_total) + " seconds   " + str(step_number) + "\n")
            print("Line " + str(frame.f_lineno - number_subtracted) + ", running " + str(line_counters[frame.f_lineno - number_subtracted - 1]) + " times: Value of " + var_name_changed + " is assigned " + str(var_value_changed))  
        else:
            #checks whether any previous variabls/lists have been changed
            temp_var_values = list(frame.f_locals.values()) 
            for i in range(len(temp_var_values)):
                if temp_var_values[i] != var_values[i]:
                    record_of_values[i].append(temp_var_values[i]) #updates the appropriate list element of record_of_values with the new value of the variable
                    #outputs the new and old values of the variable to both the console window and the text file
                    text_file.write("Line " + str(frame.f_lineno - number_subtracted) + ", running " + str(line_counters[frame.f_lineno - number_subtracted - 1]) + " times: Value of " + var_names[i] + " is changed from " + str(var_values[i]) + " to " + str(temp_var_values[i]) + "  " + str(overall_total) + " seconds   " + str(step_number) + "\n")
                    print("Line " + str(frame.f_lineno - number_subtracted) + ", running " + str(line_counters[frame.f_lineno - number_subtracted - 1]) + " times: Value of " + var_names[i] + " is changed from " + str(var_values[i]) + " to " + str(temp_var_values[i]))
                    break
            var_values = temp_var_values

        previous_line_number = frame.f_lineno

        times[frame.f_lineno - number_subtracted - 1].append(timeit.default_timer()) #times how long it took to execute the line
        overall_total += times[frame.f_lineno - number_subtracted - 1][len(times[frame.f_lineno - number_subtracted - 1]) - 1] #increments the overall total for the execution of the whole program
        step_number += 1
        #the following lines average the time spent on the current line, if the line has been executed multiple times in a loop and outputs the results
        total = 0.0
        for i in range(len(times[frame.f_lineno - number_subtracted - 1])):
            total += times[frame.f_lineno - number_subtracted - 1][i]
        average = total / len(times[frame.f_lineno - number_subtracted - 1])
        text_file.write("Total time spent on line: " + str(total) + " seconds     Average time spent on line: " + str(average) + " seconds\n")
        print("Total time spent on line: " + str(total) + " seconds     Average time spent on line: " + str(average) + " seconds")



sys.settrace(trace_calls)
eval("mod." + func_name)() #function to be tested is called. Note: if there are any parameters for the function to be debugged they NEED to be passed in this statement
#this outputs the results of the debugging i.e. all the variables, their data types, the lines they were instantiated on and the total time for execution
print()
for i in range(len(var_names)):
    text_file.write(var_data_types[i] + " variable of name " + var_names[i] + " instantiated on line " + str(var_line_numbers[i]) + " function '" + func_name + "'\n")
    print(var_data_types[i] + " variable of name " + var_names[i] + " instantiated on line " + str(var_line_numbers[i]) + " function '" + func_name + "'")
    text_file.write("List of values that " + var_names[i] + " had been assigned: " + str(record_of_values[i]) + "\n")
    print("List of values that " + var_names[i] + " had been assigned: " + str(record_of_values[i]))
    text_file.write("\n")
    print()

text_file.write("\n")
print()
for i in range(len(line_counters)):
    text_file.write("Line " + str(i + 1) + " was executed " + str(line_counters[i]) + " times\n")
    print("Line " + str(i + 1) + " was executed " + str(line_counters[i]) + " times")

text_file.write("\n")
print()
text_file.write("Total time for execution: " + str(overall_total) + " seconds\n")
print("Total time for execution: " + str(overall_total) + " seconds")
text_file.close()
