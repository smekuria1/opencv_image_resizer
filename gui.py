import PySimpleGUI as sg
from mainGUI import mainCall

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
            window.perform_long_operation(lambda:mainCall(path=datasetPath,out=outputPath,x=xVal,y=yVal,mode="size"),'-COMPLETED-')
            
        elif event == 'Run' and values['-scale-'] :
            window.perform_long_operation(lambda:mainCall(path=datasetPath,out=outputPath,x=xVal,y=yVal,mode="scale"),'-COMPLETED-')
            
        elif event == 'Run' and values['-percent-'] :
            window.perform_long_operation(lambda:mainCall(path=datasetPath,out=outputPath,x=xVal,y=yVal,mode="percentage"),'-COMPLETED-')
            
        elif event == 'Run' and values['-target-'] :
            window.perform_long_operation(lambda:mainCall(path=datasetPath,out=outputPath,x=xVal,y=yVal,mode="target"),'-COMPLETED-')
        elif event == '-COMPLETED-':
            sg.popup('Done')
        
    
    
    window.Close()

if __name__ == '__main__':
    main()