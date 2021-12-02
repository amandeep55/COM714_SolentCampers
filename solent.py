import tkinter as tk
from tkinter import ttk
from tkinter import *
from typing import Sized
  
 
LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 25)
  
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
        for F in (Home, CustomerPage, AdvisorPage, AdminPage, AdvisorVansPage, AdvisorSitesPage, AdvisorSummaryPage,
         TripPageHimachal, TripPageRajasthan, TripPageMaharashtra, TripPageMP, AdminVanPage, AdminSitePage):
  
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
        label.grid(row = 1, column = 2, padx = 30, pady = 10)
  
        button1 = ttk.Button(self, text ="Customer Login",
        command = lambda : controller.show_frame(CustomerPage))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 2, column = 1, padx = 30, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Advisor Login",
        command = lambda : controller.show_frame(AdvisorPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 2, padx = 30, pady = 10)


        ## button to show frame 3 with text layout2
        button3 = ttk.Button(self, text ="Admin Login",
        command = lambda : controller.show_frame(AdminPage))
        # putting the button in its place by
        # using grid
        button3.grid(row = 2, column = 3, padx = 30, pady = 10)

        ## button to exit
        exitButton = ttk.Button(self, text ="Exit",
        command=quit)
        # putting the button in its place by
        # using grid
        exitButton.grid(row = 3, column = 2, padx = 30, pady = 10)
  
  
# second window frame CustomerPage
class CustomerPage(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Hello Customer!", font = LARGEFONT)
        label.grid(row = 1, column = 2, padx = 30, pady = 10)
        mymessage = ttk.Label(self, text="My Bookings", font = MEDIUMFONT)
        mymessage.grid(row = 2, column = 2, padx = 30, pady = 10)
   
        def Scankey(event):
            val = event.widget.get()
            print(val)
            if val == '':
                data = booklist
            else:
                data = []
                for item in booklist:
                    if val.lower() in item.lower():
                        data.append(item)
            Update(data)


        def Update(data):
            listbox.delete(0, 'end')
            # put new data
            for item in data:
                listbox.insert('end', item)

          
        booklist = ["Patalpani, Indore, MP", "Nandi Hills, Bangalore, Karnataka", "Lonavala, Maharashtra",
                    "Khandala, Maharashtra", "Chandrashila, Uttarakhand",
                    "Manali, Himachal Pradesh", "Tosh, Himachal Pradesh", "Leh, Jammu", "Jaisalmer, Rajasthan"]

        entry = Entry(self)
        entry.grid(row=3, column=2)
        entry.bind('<KeyRelease>', Scankey)
        
        listbox = Listbox(self, width=20, height=5, justify=CENTER, bg="WHITE", bd=20)
        listbox.grid(row=4, column=2)
        Update(booklist)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 5, column = 1, padx = 30, pady = 10)
  

# third window frame AdvisorPage
class AdvisorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Hello Advisor..", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 30, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 30, pady = 10)

        button3 = ttk.Button(self, text ="Camping Vans",
                            command = lambda : controller.show_frame(AdvisorVansPage))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 1, padx = 30, pady = 10)

        button4 = ttk.Button(self, text ="Camping Sites",
                            command = lambda : controller.show_frame(AdvisorSitesPage))
     
        # putting the button in its place by
        # using grid
        button4.grid(row = 3, column = 2, padx = 30, pady = 10)

        button5 = ttk.Button(self, text ="Summary of Trips",
                            command = lambda : controller.show_frame(AdvisorSummaryPage))
     
        # putting the button in its place by
        # using grid
        button5.grid(row = 3, column = 3, padx = 30, pady = 10)


# Advisor vans page
class AdvisorVansPage(tk.Frame):
    def __init__(self, parent, controller):
        def Scankey(event):
            val = event.widget.get()
            print(val)
            if val == '':
                data = booklist
            else:
                data = []
                for item in booklist:
                    if val.lower() in item.lower():
                        data.append(item)
            Update(data)


        def Update(data):
            listbox.delete(0, 'end')
            # put new data
            for item in data:
                listbox.insert('end', item)


        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Camper Vans", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 30, pady = 10)
          
        booklist = ["motogp van-mercedes", "F1 van-BMW", "F1 van-Ferrari",
                    "Red bull van", "Toyota van - big"]

        entry = Entry(self)
        entry.grid(row=2, column=2)
        entry.bind('<KeyRelease>', Scankey)
        
        listbox = Listbox(self, width=20, height=5, justify=CENTER, bg="WHITE", bd=20)
        listbox.grid(row=3, column=2)
        Update(booklist)
        
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(AdvisorPage))
        
        # putting the button in its place by
        # using grid
        button2.grid(row = 4, column = 1, padx = 30, pady = 10)


# Advisor Sites page
class AdvisorSitesPage(tk.Frame):
    def __init__(self, parent, controller):
        def Scankey(event):
            val = event.widget.get()
            print(val)
            if val == '':
                data = booklist
            else:
                data = []
                for item in booklist:
                    if val.lower() in item.lower():
                        data.append(item)
            Update(data)


        def Update(data):
            listbox.delete(0, 'end')
            # put new data
            for item in data:
                listbox.insert('end', item)


        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Camping Sites", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 30, pady = 10)
          
        booklist = ["Patalpani, Indore, MP", "Nandi Hills, Bangalore, Karnataka", "Lonavala, Maharashtra",
                    "Khandala, Maharashtra", "Panjim, Goa", "Kedarkantha, Uttarakhand", "Chandrashila, Uttarakhand",
                    "Manali, Himachal Pradesh", "Tosh, Himachal Pradesh", "Leh, Jammu", "Jaisalmer, Rajasthan"]

        entry = Entry(self)
        entry.grid(row=2, column=2)
        entry.bind('<KeyRelease>', Scankey)
        
        listbox = Listbox(self, width=20, height=5, justify=CENTER, bg="WHITE", bd=20)
        listbox.grid(row=3, column=2)
        Update(booklist)
        
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(AdvisorPage))
        
        # putting the button in its place by
        # using grid
        button2.grid(row = 4, column = 1, padx = 30, pady = 10)


# Advisor summary page
class AdvisorSummaryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Summary of the Trips", font = LARGEFONT, anchor="center")
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 1, column = 2, padx = 30, pady = 10)
  
        button1 = ttk.Button(self, text ="Trip -  Himachal",
        command = lambda : controller.show_frame(TripPageHimachal))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 3, column = 2, padx = 30, pady = 10)
  
 
        button2 = ttk.Button(self, text ="Trip - Rajasthan",
        command = lambda : controller.show_frame(TripPageRajasthan))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 4, column = 2, padx = 30, pady = 10)


        button3 = ttk.Button(self, text ="Trip - Madhya Pradesh",
        command = lambda : controller.show_frame(TripPageMP))
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 3, padx = 30, pady = 10)

        
        button4 = ttk.Button(self, text ="Trip - Maharashtra",
        command = lambda : controller.show_frame(TripPageMaharashtra))
        # putting the button in its place by
        # using grid
        button4.grid(row = 4, column = 3, padx = 30, pady = 10)

        # layout3
        backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(AdvisorPage))
        
        # putting the button in its place by
        # using grid
        backButton.grid(row = 5, column = 1, padx = 30, pady = 10)


# himachal trip pge
class TripPageHimachal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Trip - Himachal", font = LARGEFONT, anchor="center")
    
        # putting the grid in its place by using grid
        label.grid(row = 1, column = 2, padx = 30, pady = 10)

        # label of frame Layout 2
        # Create text widget and specify size.
        T = Text(self, height = 5, width = 52)
        sumText = "Trips in Himachal are done using Toyota camping vans and Toofans vehicles and cover places like Manali, Tosh, Kasol etc."
        T.grid(row = 2, column = 2, padx = 20, pady = 10)
        T.insert(tk.END, sumText)
  
        # layout3
        backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(AdvisorSummaryPage))
        
        # putting the button in its place by
        # using grid
        backButton.grid(row = 4, column = 1, padx = 30, pady = 10)

# Rajasthan trip pge
class TripPageRajasthan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Trip - Rajasthan", font = LARGEFONT, anchor="center")
    
        # putting the grid in its place by using grid
        label.grid(row = 1, column = 2, padx = 30, pady = 10)

        # label of frame Layout 2
        # Create text widget and specify size.
        T = Text(self, height = 5, width = 52)
        sumText = "Trips in Rajasthan are done using F1 camping vehicles from BMW and Ferrari and also Hummer vehicles in few cases. Cover places like Jaiselmair, Jaipur, Mount abu, Udaipur etc."
        T.grid(row = 2, column = 2, padx = 20, pady = 10)
        T.insert(tk.END, sumText)
  
        # layout3
        backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(AdvisorSummaryPage))
        
        # putting the button in its place by
        # using grid
        backButton.grid(row = 4, column = 1, padx = 30, pady = 10)


# maharashtra trip pge
class TripPageMaharashtra(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Trip - Maharashtra", font = LARGEFONT, anchor="center")
    
        # putting the grid in its place by using grid
        label.grid(row = 1, column = 2, padx = 30, pady = 10)

        # label of frame Layout 2
        # Create text widget and specify size.
        T = Text(self, height = 5, width = 52)
        sumText = "Trips in Maharashtra are done using carrier truck camping vans and Toofans vehicles and cover places like Lonavala, khandala, mumbai, pune, etc."
        T.grid(row = 2, column = 2, padx = 20, pady = 10)
        T.insert(tk.END, sumText)
  
        # layout3
        backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(AdvisorSummaryPage))
        
        # putting the button in its place by
        # using grid
        backButton.grid(row = 4, column = 1, padx = 30, pady = 10)


# mp trip pge
class TripPageMP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Trip - Madhya Pradesh", font = LARGEFONT, anchor="center")
    
        # putting the grid in its place by using grid
        label.grid(row = 1, column = 2, padx = 30, pady = 10)

        # label of frame Layout 2
        # Create text widget and specify size.
        T = Text(self, height = 5, width = 52)
        sumText = "Trips in MP are done using Moto gp camping vans and red bull branded carrier trucks with large tyres and cover places Patalpani, mandu, sanchi, chidiya bhadak, etc."
        T.grid(row = 2, column = 2, padx = 20, pady = 10)
        T.insert(tk.END, sumText)
  
        # layout3
        backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(AdvisorSummaryPage))
        
        # putting the button in its place by
        # using grid
        backButton.grid(row = 4, column = 1, padx = 30, pady = 10)
  
# fourth window frame Adminpage
class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Hey Admin!", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 30, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 30, pady = 10)

        # layout3
        backButton = ttk.Button(self, text ="Add Camping site",
                            command = lambda : controller.show_frame(AdminSitePage))
        
        # putting the button in its place by
        # using grid
        backButton.grid(row = 4, column = 2, padx = 30, pady = 10)

        # layout3
        backButton = ttk.Button(self, text ="Add Camping van",
                            command = lambda : controller.show_frame(AdminVanPage))
        
        # putting the button in its place by
        # using grid
        backButton.grid(row = 4, column = 3, padx = 30, pady = 10)


# fourth window frame Adminpage
class AdminSitePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def printInput():
            inp = inputtxt.get(1.0, "end-1c")
            lbl.config(text = "Provided Input: "+inp)

        label = ttk.Label(self, text ="Hey Admin!", font = LARGEFONT)
        label.grid(row = 1, column = 2, padx = 30, pady = 10)

        label = ttk.Label(self, text ="Add a Camping Site", font = MEDIUMFONT)
        label.grid(row = 2, column = 2, padx = 30, pady = 10)

        # TextBox Creation
        inputtxt = tk.Text(self, height = 5, width = 20)
        inputtxt.grid(row = 3, column = 2, padx = 30, pady = 10)
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(AdminPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 6, column = 1, padx = 30, pady = 10)

        # layout3
        backButton = ttk.Button(self, text = "Print", command = printInput)
        
        # putting the button in its place by
        # using grid
        backButton.grid(row = 6, column = 2, padx = 30, pady = 10)

        lbl = tk.Label(self, text = "")
        lbl.grid(row = 6, column = 3, padx = 30, pady = 10)


# fourth window frame Adminpage
class AdminVanPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def printInput():
            inp = inputtxt.get(1.0, "end-1c")
            lbl.config(text = "Provided Input: "+inp)

        label = ttk.Label(self, text ="Hey Admin!", font = LARGEFONT)
        label.grid(row = 1, column = 2, padx = 30, pady = 10)

        label = ttk.Label(self, text ="Add a van", font = MEDIUMFONT)
        label.grid(row = 2, column = 2, padx = 30, pady = 10)

        # TextBox Creation
        inputtxt = tk.Text(self, height = 5, width = 20)
        inputtxt.grid(row = 3, column = 2, padx = 30, pady = 10)
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(AdminPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 6, column = 1, padx = 30, pady = 10)

        # layout3
        backButton = ttk.Button(self, text = "Print", command = printInput)
        
        # putting the button in its place by
        # using grid
        backButton.grid(row = 6, column = 2, padx = 30, pady = 10)

        lbl = tk.Label(self, text = "")
        lbl.grid(row = 6, column = 3, padx = 30, pady = 10)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()