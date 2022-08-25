import subprocess
import sys
from time import time
from tkinter import N
import PySimpleGUI as sg

def main():
    sg.theme('DarkPurple4')
    layout = [  [sg.Text("Path to Dataset"), sg.In(size=(100,1)), 
                 sg.FolderBrowse("Select Folder")], 
                [sg.Text('OutPut Path    '), sg.In( default_text=('Out'),size=(100,1))],  
                [sg.Text('Size of X  ',  size=(10, 1)), sg.InputText()],
                [sg.Text('Size of Y  ', size=(10, 1)), sg.InputText()],
                [sg.Radio('Size Mode!     ', "MODES", default=True,key='-size-'), 
                sg.Radio('Percentage Mode', "MODES",key='-percent-'),
                sg.Radio('Scale Mode', "MODES",key='-scale-'),
                sg.Radio('Target Mode', "MODES",key='-target-'),
                ],   
                [sg.Output(size=(100,30))],         
                [sg.Button('Run'), sg.Button('Exit')],
                ]    

    window = sg.Window('OpenCV Image Resizer GUI', layout, size=(1000,1000) ,resizable=True)  

    while True:             # Event Loop 
        event, values = window.Read() # Grab values and events and assign each to 
        datasetPath = values[0]
        outputPath = values[1]
        xVal = values[2]
        yVal = values[3]
        if event in (None,'Exit'): 
            break
        #  Check which mode user wants to run
        # Default is Size
        elif event == 'Run' and values['-size-'] :
            command = f"python main.py -p {datasetPath} -o {outputPath} -x {xVal} -y {yVal} -m size"
            print(f"Running command \n {command}")
            runScript(cmd=command, window=window)
            
        elif event == 'Run' and values['-scale-'] :
            command = f"python main.py -p {datasetPath} -o {outputPath} -x {xVal} -y {yVal} -m scale"
            print(f"Running command \n {command}")
            runScript(cmd=command, window=window)
            
        elif event == 'Run' and values['-percent-'] :
            command = f"python main.py -p {datasetPath} -o {outputPath} -x {xVal} -y {yVal} -m percentage"
            print(f"Running command \n {command}")
            runScript(cmd=command, window=window)
            
        elif event == 'Run' and values['-target-'] :
            command = f"python main.py -p {datasetPath} -o {outputPath} -x {xVal} -y {yVal} -m target"
            print(f"Running command \n {command}")
            runScript(cmd=command, window=window)
        
    
    
    window.Close()

# This function does the actual "running" of the command.  Also watches for any output. If found output is printed
def runScript(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        if window:
            window.Refresh()
        else:
            p.wait()
            p.kill()       
    retval = p.wait(timeout)
    return(retval,output)
                         # also return the output just for fun

if __name__ == '__main__':
    main()