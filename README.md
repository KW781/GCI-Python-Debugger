# GCI-Python-Debugger

# Description
This is a debugger that debugs a program, the name of which is input via command line. It'll also create a .gif file that shows the flow
of the program as it runs and also writes the output of a debugger to both the console window and to a text file "Debugger Output.txt". This is a debugger that was written to complete a series of tasks for Google Code In 2019 and these tasks were assigned by the organisation CCExtractor Development.

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

If the function to be debugged requires paarameters to be passed to it, then after the debugger is called via a command line statement, the debugger will prompt the user of the debugger for input of the parameters to be input to the function. 

In the .yml file there are all the video configuration settings. The first is the running speed, which is the amount of seconds each frame should be displayed for in the video. The second is the name of the .ttf file which details the font to use when outputting text to the video. Currently the only font suppported is Antaro but more can be supported later on. The third is the font size to use, the fourth is the intro text to display in the video before the debugging starts and the fifth is a boolean value for whether the name of the program with the function to be debugged should be displayed in the video or not. The sixth is the amount pixels that should be displayed horizontally in each video frame and the seventh is the amount of pixels that should be displayed vertically in the video frame. The eigth setting is a list of variables that the user of the debugger wants muted in the video, if any. This means that the names of the variables won't be mentioned when debugging the program in the video. 

After the debugging process, an image will be created within the same directory as the debugger. This was just created as a part of the 
video generation process, and can be deleted after the debugger has finished running.
