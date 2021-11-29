import tkinter as tk
from tkinter import ttk
from tkinter import *
  
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, CustomerPage, AdvisorPage, AdminPage):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # Home, CustomerPage, AdvisorPage respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Home)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame Home
  
class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Solent Campers", font = LARGEFONT, anchor="center")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 1, column = 2, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Customer Login",
        command = lambda : controller.show_frame(CustomerPage))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Advisor Login",
        command = lambda : controller.show_frame(AdvisorPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 2, padx = 10, pady = 10)


        ## button to show frame 3 with text layout2
        button3 = ttk.Button(self, text ="Admin Login",
        command = lambda : controller.show_frame(AdminPage))
        # putting the button in its place by
        # using grid
        button3.grid(row = 2, column = 3, padx = 10, pady = 10)

        ## button to exit
        exitButton = ttk.Button(self, text ="Exit",
        command=quit)
        # putting the button in its place by
        # using grid
        exitButton.grid(row = 3, column = 2, padx = 10, pady = 10)
  
  
# second window frame CustomerPage
class CustomerPage(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Hello Customer!", font = LARGEFONT)
        label.grid(row = 1, column = 2, padx = 10, pady = 10)
        mymessage = ttk.Label(self, text="My Bookings")
        mymessage.grid(row = 2, column = 2, padx = 10, pady = 10)
   
        listbox = Listbox(self)  
        booklist = ["Indore, MP", "Rohtak, Haryana", "Lucknow, UP"]
        
        for book in booklist:
            listbox.insert(END, book)
    
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame AdvisorPage
class AdvisorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Hello Advisor..", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


  
# fourth window frame Adminpage
class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Hey Admin!", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()