from tkinter import *
from tkinter import ttk
from disk_scheduling import *
from visualization import *
from graph import *


def Main():

    # List of colours
    WHITE = "#DAFFFB"
    BLACK = "#001C30"
    BLUE = "#176B87"
    LIGHT_GRAY = "#64CCC5"
    DARK_GRAY = "#001C30"

    window = Tk()
    window.title("Disk Scheduling Algorithms")
    window.overrideredirect(False)
    window.geometry("710x620+300+25")
    window.resizable(False, False)
    window.configure(bg=WHITE)

    # Title Frame
    title_frame = Frame(window, bg=DARK_GRAY)
    title_frame.pack(side=TOP, fill=X)

    # Title Label
    title = Label(title_frame, text="Disk Scheduling Algorithms", anchor=CENTER, bd=12,
                  padx=100, bg=DARK_GRAY, fg=WHITE, font=("Inter", 30), pady=2)
    title.grid(row=0, column=0)

    # Body Frame
    body_frame = Frame(window, bg=WHITE)
    body_frame.pack(side=TOP, fill=BOTH, expand=True)

    # List of options in dropdown window
    optionlist = ('FCFS', 'SSTF', 'SCAN', 'CSCAN', 'CLOOK')

    # Variables
    Option = StringVar()
    Start = IntVar()
    Option.set("FCFS")

    # Set the styles
    style = ttk.Style()
    style.configure("Custom.TLabel", font=("Inter", 16),
                    bg=WHITE, fg=BLACK)
    style.configure("Custom.TEntry", font=("Inter", 16), width=30,
                    height=1, background=LIGHT_GRAY, foreground=BLUE)
    style.configure("Custom.TMenubutton",
                    background=LIGHT_GRAY,
                    foreground=BLUE,
                    padding=10,
                    font=("Inter", 12))
    style.configure("Custom.TButton", font=("Inter", 12),
                    background=DARK_GRAY, foreground=DARK_GRAY)
    style.map("Custom.TButton", borderwidth=[("active", 0)])

    # Label 1
    L1 = ttk.Label(body_frame, text="Choose Algorithm:", style="Custom.TLabel")
    L1.grid(row=1, column=0, pady=50, padx=25)

    # Dropdown window
    OM = ttk.OptionMenu(body_frame, Option, *optionlist)
    OM.grid(row=1, column=1)
    # Apply custom style to the OptionMenu
    OM.configure(style="Custom.TMenubutton")

    # empty label
    L = Label(body_frame, text="", font=("Inter", 16),
              bg=WHITE, fg=WHITE, pady=5)
    L.grid(row=2, column=0)

    # Label 2
    L2 = ttk.Label(body_frame, text="Enter your values:",
                   style="Custom.TLabel")
    L2.grid(row=3, column=0)

    user_inp = ttk.Entry(body_frame, font=("Inter", 16),
                         style="Custom.TEntry", width=30)
    user_inp.grid(row=3, column=1)

    # Configure the frame's highlight background color
    body_frame.config(highlightbackground="red")

    # empty label
    L = Label(body_frame, text="", font=("Inter", 16),
              bg=WHITE, fg=WHITE, pady=5)
    L.grid(row=4, column=0)

    # Label 3
    L3 = ttk.Label(body_frame, text="Position of head:", style="Custom.TLabel")
    L3.grid(row=5, column=0, pady=30)

    # Textbox
    E1 = ttk.Entry(body_frame, textvariable=Start, font=("Inter", 16),
                   style="Custom.TEntry", justify=CENTER, width=5)
    E1.grid(row=5, column=1)

    # empty label
    L = Label(body_frame, text="", font=("Inter", 16),
              bg=WHITE, fg=WHITE, pady=5)
    L.grid(row=6, column=1)

    # Button 1
    B1 = ttk.Button(body_frame, text="Visualise", command=lambda: Visualise(
        Option.get(), user_inp.get(), Start.get()), style="Custom.TButton")
    B1.grid(row=7, column=1, pady=10)

    # empty label
    L = Label(body_frame, text="", font=("Inter", 16),
              bg=WHITE, fg=WHITE, pady=5)
    L.grid(row=8, column=1)

    # Button 2
    B2 = ttk.Button(body_frame, text="Graph", command=lambda: graphy(
        user_inp.get(), Start.get()), style="Custom.TButton")
    B2.grid(row=9, column=1, pady=10)

    window.mainloop()


Main()
