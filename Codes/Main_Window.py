from tkinter import *
from tkinter import messagebox
import Codes.Start_Threading
from Codes.Start_Sorting import *
from Codes.Start_Searching import *
from Codes.Sudoku import *
from Codes.N_Queens import *
from Codes.Knight_Tour import *


class Window:
    def __init__(self, root):

        # Main Window
        self.root = root

        # Warning sign for close
        self.root.protocol("WM_DELETE_WINDOW", self.Close)

        # Main Window Size and Center Aligned in the screen
        self.wx, self.wy = 300, 220
        self.wxs, self.wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.WINDOW_X, self.WINDOW_Y = (self.wxs / 2) - (self.wx / 2), (self.wys / 2) - (self.wy / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.wx, self.wy, self.WINDOW_X, self.WINDOW_Y))
        self.root.config(bg="LightSkyBlue1")
        self.root.resizable(False, False)

        # Title And Icon
        self.root.title("Algorithm Visualizer")
        try:
            self.root.iconbitmap("Images/algorithm.ico")
        except:
            img = PhotoImage("Images/algorithm.ico")
            self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        # Heading of the main window
        self.MainLabel = Label(self.root, text='Algorithm Visualizer', bg="LightSkyBlue1", fg="blue4",
                               font=("calibri italic", 20))
        self.MainLabel.pack(pady=15)

        # Dictionary On types of Algorithms and their lists
        self.Algo = {'Searching': ['Linear Search', 'Binary Search'],
                     'Sorting': ['Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort',
                                 'Heap Sort', 'Shell Sort', 'Radix Sort'],
                     'Backtracking': ['Sudoku', 'N-Queens', "Knight's Tour"],
                     'DP Table': ['Coming Soon!']}

        # Two dropdown menu on algorithm type and algorithm name
        self.AlgoTypeVar = StringVar()
        self.AlgoNameVar = StringVar()

        # for automatic update on the second list if something is chosen on the 1st list
        self.AlgoTypeVar.trace('w', self.update_options)

        # two drop down menus configurations
        self.AlgoTypeList = OptionMenu(self.root, self.AlgoTypeVar, *self.Algo.keys())
        self.AlgoTypeList.config(bg="pink", activebackground="hot pink", cursor="hand2")
        self.AlgoNameList = OptionMenu(self.root, self.AlgoNameVar, 'None')
        self.AlgoNameList.config(bg="pink", activebackground="hot pink", cursor="hand2")
        # label of the two dropdown menus
        self.AlgoTypeVar.set("Select Algorithm Type")
        self.AlgoNameVar.set("Select Algorithm")
        self.AlgoTypeList.pack(pady=2)
        self.AlgoNameList.pack(pady=2)

        # next button
        self.NextButton = Button(self.root, text="Next>", bg="pale green", activebackground="lime green",
                                 command=self.Run1)
        self.NextButton.pack(pady=20)

    # for automatic update on the 2nd list if something is chosen on the 1st list
    def update_options(self, *args):
        try:
            algo_list = self.Algo[self.AlgoTypeVar.get()]
        except:
            algo_list = ["None"]
        self.AlgoNameVar.set("Select Algorithm")
        menu = self.AlgoNameList['menu']
        menu.delete(0, 'end')
        for algo in algo_list:
            menu.add_command(label=algo, command=lambda x=algo: self.AlgoNameVar.set(x))

    # Exit button
    def Exit(self):
        self.root.destroy()

    # Close warning
    def Close(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()
            exit()

    # Secondary window back button
    def Back(self):
        self.root.destroy()
        Process = Codes.Start_Threading.START()
        Process.start()

    # For running the algorithms
    def Run2(self):
        # If Sorting is selected
        if self.AlgoTypeVar.get() == "Sorting":
            # create a new window for sorting algorithm
            sort_window = Tk()
            # send it to Start_Sort.py file
            Sorting(sort_window, self.AlgoNameVar.get())
            sort_window.mainloop()
        elif self.AlgoTypeVar.get() == "Backtracking":
            if self.AlgoNameVar.get() == "Sudoku":
                speed = self.speed_var.get()
                self.root.destroy()
                sudoku(speed)
            elif self.AlgoNameVar.get() == "N-Queens":
                speed = self.speed_var.get()
                size = self.size_var.get()
                self.root.destroy()
                N_queen(size, speed)
            elif self.AlgoNameVar.get() == "Knight's Tour":
                speed = self.speed_var.get()
                size = self.size_var.get()
                self.root.destroy()
                Knight(size, speed)
        # If Sorting is selected
        elif self.AlgoTypeVar.get() == "Searching":
            # create a new window for sorting algorithm
            search_window = Tk()
            # send it to Start_Sort.py file
            Searching(search_window, self.AlgoNameVar.get())
            search_window.mainloop()

    # For running the secondary window
    def Run1(self):

        # If nothing is selected show an error box
        if self.AlgoTypeVar.get() == "Select Algorithm Type":
            messagebox.showerror("Error!", "Please select Algorithm Type.")

        # If sorting is selected
        elif self.AlgoTypeVar.get() == "Sorting":
            # Destroy the main window
            self.root.destroy()
            # Go to run() function
            self.Run2()

        # if backtracking is selected
        elif self.AlgoTypeVar.get() == "Backtracking":
            # create a new window
            self.root.destroy()
            self.root = Tk()
            # if sudoku is selected
            if self.AlgoNameVar.get() == "Sudoku":
                # size of the window
                wx, wy = 300, 150
                # fit the window at the centre of the screen
                wxs, wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
                WINDOW_X, WINDOW_Y = (wxs / 2) - (wx / 2), (wys / 2) - (wy / 2)
                self.root.geometry('%dx%d+%d+%d' % (wx, wy, WINDOW_X, WINDOW_Y))
                self.root.wm_resizable(False, False)
                # title of the window
                self.root.title("Sudoku Solver Visualizer")
                # icon of the window
                try:
                    self.root.iconbitmap("Images/sudoku.ico")
                except:
                    img = PhotoImage("Images/sudoku.ico")
                    self.root.tk.call('wm', 'iconphoto', self.root._w, img)
                # create a new frame for the speed slider and buttons
                frame = Frame(self.root, width=300, height=150, bg="aquamarine")
                frame.grid_propagate(0)
                frame.pack()
                # slider for speed
                self.speed_var = Scale(frame, label="Select Speed Of Visualizer :", from_=1, to=100, orient=HORIZONTAL,
                                       length=230, bg="powder blue", troughcolor="SteelBlue2", relief="solid",
                                       cursor="hand2")
                self.speed_var.place(relx=0.12, rely=0.06)
                self.speed_var["highlightthickness"] = 0
                # button for starting visualizer
                next = Button(frame, text="Next>", bg="pale green", activebackground="lime green",
                              command=self.Run2)
                next.place(relx=0.55, rely=0.65)
                # button for main menu
                back = Button(frame, text="<Back", bg="pale green", activebackground="lime green",
                              command=self.Back)
                back.place(relx=0.25, rely=0.65)
                self.root.mainloop()
            elif self.AlgoNameVar.get() == "N-Queens" or self.AlgoNameVar.get() == "Knight's Tour":
                # size of the window
                wx, wy = 300, 200
                # fit the window at the centre of the screen
                wxs, wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
                WINDOW_X, WINDOW_Y = (wxs / 2) - (wx / 2), (wys / 2) - (wy / 2)
                self.root.geometry('%dx%d+%d+%d' % (wx, wy, WINDOW_X, WINDOW_Y))
                self.root.wm_resizable(False, False)
                # title of the window
                if self.AlgoNameVar.get() == "N-Queens":
                    self.root.title("N-Queens Solver Visualizer")
                else:
                    self.root.title("Knight's Tour Visualizer")
                # icon of the window
                if self.AlgoNameVar.get() == "N-Queens":
                    try:
                        self.root.iconbitmap("Images/nqueens.ico")
                    except:
                        img = PhotoImage("Images/nqueens.ico")
                        self.root.tk.call('wm', 'iconphoto', self.root._w, img)
                else:
                    try:
                        self.root.iconbitmap("Images/knight.ico")
                    except:
                        img = PhotoImage("Images/knight.ico")
                        self.root.tk.call('wm', 'iconphoto', self.root._w, img)
                # create a new frame for the speed slider and buttons
                frame = Frame(self.root, width=300, height=200, bg="aquamarine")
                frame.grid_propagate(0)
                frame.pack()
                # slider for size
                if self.AlgoNameVar.get() == "N-Queens":
                    self.size_var = Scale(frame, label="Select Size of the Chessboard :", from_=4, to=25,
                                          orient=HORIZONTAL,
                                          length=230, bg="powder blue", troughcolor="SteelBlue2", relief="solid",
                                          cursor="hand2")
                else:
                    self.size_var = Scale(frame, label="Select Size of the Chessboard :", from_=5, to=25,
                                          orient=HORIZONTAL,
                                          length=230, bg="powder blue", troughcolor="SteelBlue2", relief="solid",
                                          cursor="hand2")
                self.size_var.place(relx=0.12, rely=0.06)
                self.size_var["highlightthickness"] = 0
                # slider for speed
                self.speed_var = Scale(frame, label="Select Speed Of Visualizer :", from_=1, to=100, orient=HORIZONTAL,
                                       length=230, bg="powder blue", troughcolor="SteelBlue2", relief="solid",
                                       cursor="hand2")
                self.speed_var.place(relx=0.12, rely=0.4)
                self.speed_var["highlightthickness"] = 0
                # button for starting visualizer
                next = Button(frame, text="Next>", bg="pale green", activebackground="lime green",
                              command=self.Run2)
                next.place(relx=0.55, rely=0.8)
                # button for main menu
                back = Button(frame, text="<Back", bg="pale green", activebackground="lime green",
                              command=self.Back)
                back.place(relx=0.25, rely=0.8)
                self.root.mainloop()
        elif self.AlgoTypeVar.get() == "Searching":
            # Destroy the main window
            self.root.destroy()
            # Go to run() function
            self.Run2()
