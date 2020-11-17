from tkinter import *
from tkinter import messagebox
from random import shuffle, sample
from Codes.Searching_Algorithms import algochooser
from threading import *
from tkinter import *
import Codes.Start_Threading


# Main sorting class
class Searching:
    def __init__(self, root, AlgoNameVar):

        # Sorting window
        self.root = root

        # warning for close/exit
        self.root.protocol("WM_DELETE_WINDOW", self.Close)

        # Selected Algorithm Name
        self.AlgoNameVar = AlgoNameVar

        # Window Size
        self.wx, self.wy = 1200, 700

        # Screen Size
        self.wxs, self.wys = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # Aligning the window in the center of the screen
        self.WINDOW_X, self.WINDOW_Y = (self.wxs / 2) - (self.wx / 2), (self.wys / 2) - (self.wy / 2)

        # Sorting canvas size
        self.CANVAS_X, self.CANVAS_Y = 950, 700

        # Left side information frame size
        self.FRAME1_X, self.FRAME1_Y = 250, 700

        # Apply changes to window
        self.root.geometry('%dx%d+%d+%d' % (self.wx, self.wy, self.WINDOW_X, self.WINDOW_Y))
        self.root.config(bg="grey")
        self.root.wm_resizable(False, False)

        # Title And Icon
        self.root.title("Searching Algorithm Visualizer")
        try:
            self.root.iconbitmap("Images/search.ico")
        except:
            img = PhotoImage("Images/search.ico")
            self.root.tk.call('wm', 'iconphoto', self.root._w, img)

        # Starting size of the array
        self.size_var = IntVar()
        self.size_var.set(30)

        # Starting speed of the array
        self.speed_var = IntVar()
        self.speed_var.set(20)

        # Starting point of the graph
        self.starting_point = 2

        # Creating frame in the left side
        self.frame1 = Frame(root, width=self.FRAME1_X, height=self.FRAME1_Y, bg="light salmon")
        self.frame1.grid_propagate(0)
        self.frame1.pack(side=LEFT)

        # Algorithm Information Table
        self.information = {'Linear Search': "Worst Case:O(n)\nAverage Case:O(n/2)\nBest Case:O(1)",
                            'Binary Search': "Worst Case:O(log n)\nAverage Case:O(log n)\nBest Case:O(1)"}

        # Algorithm Names
        self.algorithm = ['Linear Search', 'Binary Search']

        # Creating a drop down menu for algorithm selection
        self.algo_var = StringVar()
        # Setting it default value to what we selected previously in the main window
        self.algo_var.set(self.AlgoNameVar)
        self.algo_menu = OptionMenu(self.frame1, self.algo_var, *self.algorithm, command=self.case_chooser)
        self.algo_menu.config(font="calibri", bg="pink", activebackground="sandy brown", cursor="circle")
        self.algo_menu["highlightthickness"] = 0
        self.algo_menu["padx"] = 20
        self.algo_menu["pady"] = 8
        self.algo_menu.pack_propagate(0)
        # Place for the dropdown menu
        self.algo_menu.place(rely=0.07, relx=0.5, anchor=CENTER)

        # Creating a frame for new buttons
        self.frame_btn1 = Frame(self.frame1, width=230, height=40, bg="light salmon")
        self.frame_btn1.pack_propagate(0)
        self.frame_btn1.place(relx=0.0, rely=0.14)
        # Button for generating new array
        self.btn_new = Button(self.frame_btn1, text="Generate", padx=13, pady=3, command=self.new_list, bg="RoyalBlue3",
                              fg="azure", cursor="hand2")
        self.btn_new.place(relx=0.15, rely=0)
        # Button for shuffling the array
        self.btn_shuffle = Button(self.frame_btn1, text="Shuffle", padx=13, pady=3, command=self.shuffle_list,
                                  bg="RoyalBlue3", fg="azure", cursor="hand2")
        self.btn_shuffle.place(relx=0.60, rely=0)

        # text box for search entry
        self.search_element = Entry(self.frame1, width=24, bd=3, bg='light pink')
        self.search_element.insert(END, 'Enter an element to search')
        self.search_element.pack_propagate(0)
        self.search_element.place(relx=0.22, rely=0.22)

        # Creating a frame for a new button
        self.frame_btn2 = Frame(self.frame1, width=230, height=40, bg="light salmon")
        self.frame_btn2.grid_propagate(0)
        self.frame_btn2.place(relx=0.0, rely=0.26)
        # Creating a sort button
        self.btn_sort = Button(self.frame_btn2, text="Search", padx=13, pady=3, command=self.search_list,
                               bg="RoyalBlue3", fg="azure", cursor="hand2")
        self.btn_sort.place(relx=0.39, rely=0)

        # Slider for changing size of array
        self.scale_size = Scale(self.frame1, label="Size :", orient=HORIZONTAL, from_=10, to=200, length=230,
                                bg="pale goldenrod", troughcolor="#024e76", variable=self.size_var,
                                command=self.change_size,
                                relief="solid", cursor="hand2")
        self.scale_size.place(relx=0.04, rely=0.35)
        self.scale_size["highlightthickness"] = 0

        # Slider for changing speed of the operations
        self.scale_speed = Scale(self.frame1, label="Speed :", orient=HORIZONTAL, from_=1, to=500, length=230,
                                 bg="pale goldenrod", troughcolor="#024e76", variable=self.speed_var,
                                 command=self.change_speed, relief="solid", cursor="hand2")
        self.scale_speed.place(relx=0.04, rely=0.45)
        self.scale_speed["highlightthickness"] = 0

        # Label for showing the number of comparisons
        self.label_comparison = Label(self.frame1, text="No. of comparisons: 0", bg="light salmon", fg="midnight blue",
                                      font=("Fixedsys", 12))
        self.label_comparison.place(relx=0.1, rely=0.65)

        # Label for showing the searched element index
        self.label_index = Label(self.frame1, text="", bg="light salmon", fg="VioletRed4",
                                 font=("Fixedsys", 12))
        self.label_index.place(relx=0.2, rely=0.58)

        # Frame for algorithm info
        self.frame_algo_info = Frame(self.frame1, bg="tomato", width=230, height=150, relief="sunken", bd=4)
        self.frame_algo_info.grid_propagate(0)
        self.frame_algo_info.place(relx=0.03, rely=0.7)
        # Label for algorithm info
        self.label_avg = Label(self.frame_algo_info, bg="tomato", fg="midnight blue",
                               text=self.information[self.algo_var.get()], font=("comic sans ms", 13, "bold"))
        self.label_avg.pack_propagate(0)
        self.label_avg.place(relx=0.06, rely=0.25)

        # Back button to the main window
        self.BackButton = Button(self.frame1, bg="burlywood1", fg="RoyalBlue4", text="< Go Back to main menu",
                                 command=self.Back, cursor="hand2")
        self.BackButton.grid_propagate(0)
        self.BackButton.place(relx=0.2, rely=0.94)

        # Canvas for the graph
        self.frame2 = Frame(self.root, width=self.CANVAS_X, height=self.CANVAS_Y)
        self.frame2.pack(side=LEFT)
        self.frame2.grid_propagate(0)
        self.canva = Canvas(self.frame2, width=self.CANVAS_X, height=self.CANVAS_Y, bg="light goldenrod")
        self.canva.pack()

        # creating the new array
        self.numbers = sample(range(20, self.CANVAS_Y - 20), self.size_var.get())
        shuffle(list(set(self.numbers)))
        self.rec_width = self.CANVAS_X // self.size_var.get()
        for num in self.numbers:
            self.canva.create_rectangle(self.starting_point, self.CANVAS_Y - num, self.starting_point + self.rec_width,
                                        self.CANVAS_Y, fill="sandy brown")
            self.label_value = Label(self.canva, text=num, bg="sandy brown", fg="midnight blue", font=("Fixedsys", 12))
            self.canva.create_window(self.starting_point + 16, self.CANVAS_Y - num + 12, window=self.label_value)
            self.starting_point += self.rec_width

    # Function for back button to main window
    def Back(self):
        self.root.destroy()
        Process = Codes.Start_Threading.START()
        Process.start()

    # Function for exit
    def Close(self):
        if messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()
            exit()

    # function for painting the bars
    def paint(self, colortype):
        # delete the previous graph
        self.canva.delete("all")
        # start painting from here
        self.starting_point = 2
        # width of each bar
        self.rec_width = self.CANVAS_X / self.size_var.get()
        for i in range(len(self.numbers)):
            self.canva.create_rectangle(
                self.starting_point, self.CANVAS_Y - self.numbers[i], self.starting_point + self.rec_width,
                self.CANVAS_Y, fill=colortype[i])
            self.label_value = Label(self.canva, text=self.numbers[i], bg="sandy brown",
                                     fg="midnight blue",
                                     font=("Fixedsys", 12))
            self.canva.create_window(self.starting_point + 16, self.CANVAS_Y - self.numbers[i] + 12,
                                     window=self.label_value)
            self.starting_point += self.rec_width
        # update the graph frame
        self.frame2.update()

    # function for creating new list
    def new_list(self):
        numbers = []
        self.label_comparison.configure(text="No. of comparisons: 0")
        self.label_index.configure(text="")
        # enter random numbers into the new array
        self.numbers = sample(range(20, self.CANVAS_Y - 20), self.size_var.get())
        # shuffle the numbers
        shuffle(list(set(numbers)))
        colortype = ["sandy brown" for x in self.numbers]
        # paint the colored array
        self.paint(colortype)

    # function for shuffling the array
    def shuffle_list(self):
        shuffle(self.numbers)
        self.label_comparison.configure(text="No. of comparison: 0")
        self.label_index.configure(text="")
        colortype = ["sandy brown" for x in self.numbers]
        self.paint(colortype)

    # function for changing the size of the array
    def change_size(self, event):
        self.label_comparison.configure(text="No. of comparisons: 0")
        self.label_index.configure(text="")
        self.numbers = sample(range(20, self.CANVAS_Y - 20), self.size_var.get())
        shuffle(list(set(self.numbers)))
        colortype = ["sandy brown" for x in self.numbers]
        self.paint(colortype)

    # function for changing the speed of the array
    def change_speed(self, event):
        pass

    # function for choosing the sorting algorithm
    def case_chooser(self, event):
        self.label_avg.pack_forget()
        self.label_avg.configure(text=self.information[self.algo_var.get()])

    # function for sorting the list
    def search_list(self):
        self.label_comparison.configure(text="No. of comparisons: 0")
        self.label_index.configure(text="")
        print(self.search_element.get(), self.algo_var.get())
        if self.search_element.get().isdigit():
            startsearch = Thread(target=algochooser(self.numbers, self.paint, self.label_comparison, self.label_index,
                                                    self.algo_var.get(), self.speed_var.get(),
                                                    self.search_element.get()))
            startsearch.start()
        else:
            messagebox.showerror("Error!", "Please enter an integer!")
