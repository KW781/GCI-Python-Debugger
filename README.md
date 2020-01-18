# GCI-Python-Debugger

# Description
This is a debugger that debugs a program, the name of which is input via command line. It'll also create a .gif file that shows the flow
of the program as it runs and also writes the output of a debugger to both the console window and to a text file "Debugger Output.txt".

Here's an exemplar of a .gif file created by the debugger:


![](https://github.com/Knob781/GCI-Python-Debugger/blob/master/Test.gif)

# How to use
In order to use the program, 4 parameters need to be input via the command line:

The first parameter is "Python Debugger.py" which is just the name of the debugger.

The second paramter is the name of the function you want to debug within the program. Make sure the function actually exists in the program you want to debug or else an error is produced.

The third parameter is the name of the program of the program you want to debug. If the program exists within the same directory as the 
debugger, then just the program name will work fine eg. "Sample Program.py". If the program doesn't exist within the same directory as the
debugger, then the parameter will have to be the full file path to the program e.g. "C:/directory/directory/Sample Program.py"

The fourth parameter is the name you want to give to the .gif file that the debugger produces of the program flow e.g. "Video.gif". Make 
sure it ends with the file extension '.gif'

The fifth parameter is optional and it's the name of the editable .yml file containing the video configuration settings e.g. font size, font, etc. If this isn't given, then default settings will just be used.

An example of how it would be run via command line is:
python "Python Debugger.py" random_function "Sample Program.py" Video.gif "Debugger Video Configuraton.yml"

After the debugging process, an image will be created within the same directory as the debugger. This was just created as a part of the 
video generation process, and can be deleted after the debugger has finished running.
