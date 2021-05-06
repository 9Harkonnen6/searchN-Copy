import PySimpleGUI as sg
import shutil
import os

sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND': '#ff85af',
                                            'TEXT': 'black',
                                            'INPUT': 'black',
                                            'TEXT_INPUT': '#cccccc',
                                            'SCROLL': '#c7e78b',
                                            'BUTTON': ('black', '#03f4fc'),
                                            'PROGRESS': ('#01826B', '#D0D0D0'),
                                            'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                            }
sg.theme('MyNewTheme')
photos_number = 0
photos_id = None
origin = ''
destination = ''
layout = [[sg.Frame("Folders",
         [[sg.FolderBrowse('From', key='-from-', size=(8,1)), sg.Text('', size=(45,1))],
          [sg.FolderBrowse('To', key='-to-', size=(8,1)), sg.Text('', size=(45,1))]]), sg.Frame("Photo's ID", [[sg.Button("Add photo's numers", key='-add-')],
          [sg.Text(f'Photos: {photos_number}', key='-photos_number-', size=(16,1))]]), sg.Button('Next')],
          [sg.Button('Exit')]]
window_main = sg.Window("Search N' Copy", layout)
# main window loop
while True:
    event, values = window_main.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Next':
        origin = values['-from-']
        source = os.listdir(origin)
        source_list = []
        destination = values['-to-']
        # source list
        for e in source:
            source_list.append(e[4:-4])
        # whole magic!
        photos_id_list = []
        for e in photos_id:
            if e[0] ==' ':
                photos_id_list.append(e[1:])
            else:
                photos_id_list.append(e)
        
        for e in photos_id_list:
            if e in source_list:
                shutil.copyfile(f'{origin}/{source[source_list.index(e)]}', f'{destination}/{source[source_list.index(e)]}')
                
    elif event == '-add-':
        window_main.Hide()
        layout_add = [[sg.Text('Add numbers:')],
                      [sg.Input(key='-input-'), sg.Button('Add', key='-add-')],
                      [sg.Button('Back')]]
        window_add = sg.Window('Add numbers', layout_add)
        # photo's ID loop
        while True:
            event, values = window_add.read()
            if event == '-add-':
                photos_id = values['-input-']
                photos_id = photos_id.split(',')
                photos_number = len(photos_id)                
                window_main['-photos_number-'].update(f'Photos: {photos_number}')
                window_add.Close()
                window_main.UnHide()
                break
            
            elif event == sg.WIN_CLOSED or event == 'Back':                
                window_add.Close()
                window_main.UnHide()
                break            