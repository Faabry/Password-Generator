import PySimpleGUI as sg
import random

# ------- Creating lists to receive letters, numbers and symbols ----------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['@', '!', '$', '*', '-', '+']
# -------------------------------------------------------------------------


# ---------------- Creating the layout of the Program ---------------------
sg.theme_background_color('#505050')
line = [
    [sg.Text(" Gerador de Senhas ", font='Times 45',
             background_color='#505050', text_color='#FF9900')]]

amount = [
    [sg.Text(" Quantidade de letras ", font='Times 25',
             background_color='#505050',size=18),
     sg.Input(font='Times 20', size=(5, 3), key='-letters-')],

    [sg.Text(" Quantidade de números ", font='Times 25',
             background_color='#505050', size=18),
     sg.Input(font='Times 20', size=(5, 3), key='-numbers-')],

    [sg.Text(" Quantidade de simbolos ", font='Times 25',
             background_color='#505050', size=18),
     sg.Input(font='Times 20', size=(5, 3), key='-symbols-')]
 ]

layout = [
    [sg.Frame("", layout=line, background_color='#505050')],
    [sg.Frame("", layout=amount, background_color='#505050')],
    [sg.Button(button_text="Gerar Senha", font='Times 18',
               button_color='#000000 on #FF9900', key='-generate-'),
     sg.Button(button_text="Cancelar", font='Times 18',
               button_color='#000000 on #FF9900', key='-cancel-')],
    [sg.Text(font='Times 25', text_color='#FF9900',
             background_color='#505050', key='-output-')]
]
# -------------------------------------------------------------------------


# ----------------- Creating the Window of the Program --------------------
window = sg.Window("Developed by Tom Faabry", layout=layout)
# -------------------------------------------------------------------------


# ------------------------ Creating the rules -----------------------------
while True:
    events, values = window.read()
    password = []
    if events == sg.WIN_CLOSED or events == '-cancel-':
        break
    elif events == '-generate-':
        letter = values['-letters-']
        number = values['-numbers-']
        symbol = values['-symbols-']
        for c in range(0, int(letter)): 
            password.append(random.choice(letters))
        
        for c in range(0, int(number)):
            password += random.choice(numbers)
        
        for c in range(0, int(symbol)):
            password += random.choice(symbols)

        # Creating the suffle for the letters in order to be showed mixed
        random.shuffle(password)
        new_password = ''
        for item in password:
            new_password += item
        window['-output-'].update(f"A sua senha é >> {new_password} <<")
# ----------------------- End of the Program ----------------------------