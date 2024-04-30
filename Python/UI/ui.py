import tkinter as tk
from tkinter import ttk
from Python.conversion_handler import Converter
import threading
from Python.Dockers.docker_controller import DockerController
import json
CONFIGS_PATH = 'configs.json'
FONT = ("Consolas", "12", "bold")


def run_on_different_thread(func):
    def wrapper(*args, **kwargs):
        threading.Thread(target=func, args=args).start()
    return wrapper


with open(CONFIGS_PATH, mode='r') as f:
    conversions: dict = json.load(f).get('conversions')


def turn_on_docker_image(docker_name: str):
    return DockerController.turn_on(docker_name)


def turn_off_docker_image(docker_name: str):
    return DockerController.turn_off(docker_name)


def create_converter():
    def dollar_shekel(val): return Converter.dollar_to_shekel(val)
    def euro_shekel(val): return Converter.euro_to_shekel(val)
    def pound_shekel(val): return Converter.pound_to_shekel(val)
    def yen_shekel(val): return Converter.yen_to_shekel(val)
    def rupee_shekel(val): return Converter.rupee_to_shekel(val)
    def wan_shekel(val): return Converter.wan_to_shekel(val)
    mapper = {'dollar_shekel': dollar_shekel, 'euro_shekel': euro_shekel,
              'pound_shekel': pound_shekel, 'yen_shekel': yen_shekel, 'rupee_shekel': rupee_shekel, 'wan_shekel': wan_shekel}

    def convert(op: str, val):
        op = op.replace(' ', '_').lower()
        operation = mapper.get(op)
        if not operation:
            return 'Illegal operation.'
        return operation(val)

    return convert


def run_ui():
    # Create the main window
    root = tk.Tk()
    root.title('Conversion Calcualtor')
    root.geometry('460x400')  # Set the size of the window
    converter = create_converter()

    def convert_click():
        nonlocal textbox, label_with_border, dropdown
        op = dropdown.get()
        val = textbox.get()
        res = converter(op, val)
        try:
            label_with_border.config(text=f'{float(res)} ₪')
        except:
            label_with_border.config(text=res)

    def create_docker_button_event(docker_name):
        def on_click(event):
            button = event.widget
            color = button.cget('bg')
            button.config()
            if color == 'red':
                if turn_on_docker_image(docker_name):
                    button.config(bg='green')
            elif color == 'green':
                if turn_off_docker_image(docker_name):
                    button.config(bg='red')
        return on_click

    # Create buttons on the left side
    button1 = tk.Button(root, text='Py Dollar to Shekel',
                        background='red', font=FONT)
    button1.grid(row=2, column=0, pady=5, padx=5)
    button1.bind('<Button-1>', create_docker_button_event('py-dollar-shekel'))

    button2 = tk.Button(root, text='Py Euro to Shekel',
                        background='red', font=FONT)
    button2.bind('<Button-1>', create_docker_button_event('py-euro-shekel'))
    button2.grid(row=2, column=1, pady=5, padx=5)

    button4 = tk.Button(root, text='JS Dollar to Shekel',
                        background='red', font=FONT)
    button4.grid(row=3, column=0, pady=5, padx=5)
    button4.bind('<Button-1>', create_docker_button_event('js-dollar-shekel'))

    button5 = tk.Button(root, text='JS Euro to Shekel',
                        background='red', font=FONT)
    button5.grid(row=3, column=1, pady=5, padx=5)
    button5.bind('<Button-1>', create_docker_button_event('js-euro-shekel'))

    button6 = tk.Button(root, text='JS Pound to Shekel',
                        background='red', font=FONT)
    button6.grid(row=4, column=0, pady=5, padx=5)
    button6.bind('<Button-1>', create_docker_button_event('js-pound-shekel'))

    button7 = tk.Button(root, text='JS Rupee to Shekel',
                        background='red', font=FONT)
    button7.grid(row=4, column=1, pady=5, padx=5)
    button7.bind('<Button-1>', create_docker_button_event('js-rupee-shekel'))

    button8 = tk.Button(root, text='JS Wan to Shekel',
                        background='red', font=FONT)
    button8.grid(row=5, column=0, pady=5, padx=5)
    button8.bind('<Button-1>', create_docker_button_event('js-wan-shekel'))

    button9 = tk.Button(root, text='JS Yen to Shekel',
                        background='red', font=FONT)
    button9.grid(row=5, column=1, pady=5, padx=5)
    button9.bind('<Button-1>', create_docker_button_event('js-yen-shekel'))

    button3 = tk.Button(root, text='Main JS handler',
                        background='red', font=FONT)
    button3.grid(row=6, column=0, pady=5, padx=5)
    button3.bind('<Button-1>', create_docker_button_event('js-handler'))

    # Create the dropdown list and textbox in the center
    options = [c.replace('_', ' ').title() for c in conversions]
    dropdown = ttk.Combobox(root, values=options)
    dropdown.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
    dropdown.set(options[0])

    textbox = tk.Entry(root)
    textbox.grid(row=1, column=0, padx=10, pady=2, sticky='ew')

    # Create the button on the top right
    right_button = tk.Button(root, text='Convert', command=convert_click)
    right_button.grid(row=0, column=2, padx=10, pady=10, sticky='e')

    # Create the label with border at the bottom
    label_with_border = tk.Label(
        root, text='', relief='solid', borderwidth=1, height=5, font=FONT)
    label_with_border.grid(row=7, column=0, columnspan=3,
                           padx=10, pady=10, sticky='ew')

    # Configure the rows and columns
    # Gives the bottom row some weight to push everything up
    # root.grid_rowconfigure(8, weight=1)
    # Makes the center column expandable
    # root.grid_columnconfigure(1, weight=1)

    # Start the Tkinter event loop
    root.mainloop()

    DockerController.turn_off_all()
