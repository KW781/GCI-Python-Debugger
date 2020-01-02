import sys
import timeit
#function to be tested should be written HERE
def sample_function():
    b = 11 + 3
    a = b - 7
    for i in range(3):
        d = b * 3
#end of function
starting_line_number = 5 #starting line number of function being debugged (not including the function header), HAS TO BE changed appropriately by programmer depending on where they write the function


    
def trace_calls(frame, event, arg): #traces the call of the function to be tested
    if frame.f_code.co_name == "sample_function":
       return trace_lines #calls upon function 'trace_lines' for each frame

var_values = []
var_names = []
var_data_types = []
var_line_numbers = []
record_of_values = []
line_counters = []
times = []
overall_total = 0.0
previous_line_number = 0 #global variable used later on to solve minor bug
def trace_lines(frame, event, arg):
    global var_values
    global var_names
    global var_data_types
    global var_line_numbers
    global record_of_values
    global times
    global overall_total
    global previous_line_number

    if frame.f_lineno > starting_line_number: #checks that the appropriate line number is reached at the start so any new variables can be added to the dictionary
        #this statement solves a minor bug where the same line number is output twice towards the end
        if frame.f_lineno == previous_line_number: 
           number_subtracted = starting_line_number - 1
        else:
            number_subtracted = starting_line_number

        if len(line_counters) - 1 < frame.f_lineno - number_subtracted - 1:
            line_counters.append(1)
            times.append([])
        else:
            line_counters[frame.f_lineno - number_subtracted - 1] += 1
                
        if len(frame.f_locals) != len(var_values): #checks whether a new variable has been created
            #unpacks the names of the variables and the values of the variables from the dictionary 'frame.f_locals' into 2 separate global lists
            var_names = list(frame.f_locals.keys()) 
            var_values = list(frame.f_locals.values())
            var_name_changed = var_names[len(var_names) - 1]
            var_value_changed = var_values[len(var_values) - 1]
            if type(var_value_changed) is int:
                var_data_types.append("Integer")
            elif type(var_value_changed) is float:
                var_data_types.append("Floating point")
            elif type(var_value_changed) is str:
                var_data_types.append("String")
            elif type(var_value_changed) is bool:
                var_data_types.append("Boolean")
            
            var_line_numbers.append(frame.f_lineno - number_subtracted)
            record_of_values.append([])
            record_of_values[len(record_of_values) - 1].append(var_value_changed)
            #outputs the name and value of the new variable/list 
            print("Line " + str(frame.f_lineno - number_subtracted) + ", running " + str(line_counters[frame.f_lineno - number_subtracted - 1]) + " times: " + "Value of " + var_name_changed + " is assigned " + str(var_value_changed))  
        else:
            #checks whether any previous variabls/lists have been changed
            temp_var_values = list(frame.f_locals.values())
            for i in range(len(temp_var_values)):
                if temp_var_values[i] != var_values[i]:
                    record_of_values[i].append(temp_var_values[i])
                    print("Line " + str(frame.f_lineno - number_subtracted) + ", running " + str(line_counters[frame.f_lineno - number_subtracted - 1])+ " times: " + "Value of " + var_names[i] + " is changed from " + str(var_values[i]) + " to " + str(temp_var_values[i]))
                    break
            var_values = temp_var_values
            previous_line_number = frame.f_lineno

        times[frame.f_lineno - number_subtracted - 1].append(timeit.default_timer())
        overall_total += times[frame.f_lineno - number_subtracted - 1][len(times[frame.f_lineno - number_subtracted - 1]) - 1]
        total = 0.0
        for i in range(len(times[frame.f_lineno - number_subtracted - 1])):
            total += times[frame.f_lineno - number_subtracted - 1][i]
        average = total / len(times[frame.f_lineno - number_subtracted - 1])
        print("Total time spent on line: " + str(total) + " seconds     Average time spent on line: " + str(average) + " seconds")
        
sys.settrace(trace_calls)
sample_function() #function to be tested is called
print()
for i in range(len(var_names)):
    print(var_data_types[i] + " variable of name " + var_names[i] + " instantiated on line " + str(var_line_numbers[i]) + " function 'sample_function'")
    print("List of values that " + var_names[i] + " had been assigned: " + str(record_of_values[i]))
    print()

print()
for i in range(len(line_counters)):
    print("Line " + str(i + 1) + " was executed " + str(line_counters[i]) + " times")

print()
print("Total time for execution: " + str(overall_total) + " seconds")
