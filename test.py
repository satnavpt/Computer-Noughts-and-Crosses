import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import random



class Start:
    def __init__(self, master):
        self.master = master

        self.menu_frame = tk.Frame(self.master, width=620, height=620, bg="black")
        self.menu_frame.pack()

        self.one = tk.Button(self.menu_frame, width=30, height=4, text="One player (AI)", command=self.o_player)
        self.one.place(x=200, y=200)

        self.two = tk.Button(self.menu_frame, width=30, height=4, text="Two player", command=self.t_player)
        self.two.place(x=200, y=300)

        self.frame_change = None

    def o_player(self):
        self.menu_frame.destroy()
        self.frame_change = One(self.master)

    def t_player(self):
        self.menu_frame.destroy()
        self.frame_change = Two(self.master)


class One:
    def __init__(self, master):
        self.master = master

        self.space = tk.Frame(self.master, width=630, height=630, bg="black")
        self.space.pack()

        self.counter = 0

        self.nought = ImageTk.PhotoImage(Image.open("nought.jpg").resize((190, 190),Image.ANTIALIAS))
        self.cross = ImageTk.PhotoImage(Image.open("cross.jpg").resize((190, 190), Image.ANTIALIAS))

        self.pos_1 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_1")
        self.pos_1.bind("<Button-1>", self.click)
        self.pos_1.grid(column=0, row=0)

        self.pos_2 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_2")
        self.pos_2.bind("<Button-1>", self.click)
        self.pos_2.grid(column=1, row=0)

        self.pos_3 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_3")
        self.pos_3.bind("<Button-1>", self.click)
        self.pos_3.grid(column=2, row=0)

        self.pos_4 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_4")
        self.pos_4.bind("<Button-1>", self.click)
        self.pos_4.grid(column=0, row=1)

        self.pos_5 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_5")
        self.pos_5.bind("<Button-1>", self.click)
        self.pos_5.grid(column=1, row=1)

        self.pos_6 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_6")
        self.pos_6.bind("<Button-1>", self.click)
        self.pos_6.grid(column=2, row=1)

        self.pos_7 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_7")
        self.pos_7.bind("<Button-1>", self.click)
        self.pos_7.grid(column=0, row=2)

        self.pos_8 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_8")
        self.pos_8.bind("<Button-1>", self.click)
        self.pos_8.grid(column=1, row=2)

        self.pos_9 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_9")
        self.pos_9.bind("<Button-1>", self.click)
        self.pos_9.grid(column=2, row=2)

        self.widget = None
        self.nought_l = None
        self.cross_l = None

    def click(self, event):
        self.widget = ("self" + (str(event.widget)[8:]))
        self.nought_l = tk.Label(eval(self.widget), image=self.nought, name="o")
        self.nought_l.pack()
        self.checker()
        self.comp()

    def comp(self):
        positions = []
        for x in range(1, 10):
            command = "self.pos_" + str(x) + ".winfo_children()"
            if str(eval(command)) == "[]":
                positions.append("e")
            else:
                positions.append(str(eval(command))[38])
        empties = [index for index, item in enumerate(positions) if item == "e"]
        empties = [x + 1 for x in empties]
        if str(empties) == "[]":
            self.checker()
        else:

            #vertical winners
            if empties[3] == "x" and empties[6] == "x":
                x = 1
            elif empties[0] == "x" and empties[6] == "x":
                x = 4
            elif empties[0] == "x" and empties[3] == "x":
                x = 7

            elif empties[4] == "x" and empties[7] == "x":
                x = 2
            elif empties[1] == "x" and empties[7] == "x":
                x = 5
            elif empties[1] == "x" and empties[4] == "x":
                x = 8

            elif empties[5] == "x" and empties[8] == "x":
                x = 3
            elif empties[2] == "x" and empties[8] == "x":
                x = 6
            elif empties[2] == "x" and empties[5] == "x":
                x = 9

            #horizontal winners
            elif empties[1] == "x" and empties[2] == "x":
                x = 1
            elif empties[0] == "x" and empties[2] == "x":
                x = 2
            elif empties[0] == "x" and empties[1] == "x":
                x = 3

            elif empties[4] == "x" and empties[5] == "x":
                x = 4
            elif empties[3] == "x" and empties[5] == "x":
                x = 5
            elif empties[3] == "x" and empties[4] == "x":
                x = 6

            elif empties[7] == "x" and empties[8] == "x":
                x = 7
            elif empties[6] == "x" and empties[8] == "x":
                x = 8
            elif empties[6] == "x" and empties[7] == "x":
                x = 9

            # vertical blockers
            if empties[3] == "o" and empties[6] == "o":
                x = 1
            elif empties[0] == "o" and empties[6] == "o":
                x = 4
            elif empties[0] == "o" and empties[3] == "o":
                x = 7

            elif empties[4] == "o" and empties[7] == "o":
                x = 2
            elif empties[1] == "o" and empties[7] == "o":
                x = 5
            elif empties[1] == "o" and empties[4] == "o":
                x = 8

            elif empties[5] == "o" and empties[8] == "o":
                x = 3
            elif empties[2] == "o" and empties[8] == "o":
                x = 6
            elif empties[2] == "o" and empties[5] == "o":
                x = 9

            # horizontal blockers
            elif empties[1] == "o" and empties[2] == "o":
                x = 1
            elif empties[0] == "o" and positions[2] == "o":
                x = 2
            elif positions[0] == "o" and positions[1] == "o":
                x = 3

            elif positions[4] == "o" and positions[5] == "o":
                x = 4
            elif positions[3] == "o" and positions[5] == "o":
                x = 5
            elif positions[3] == "o" and positions[4] == "o":
                x = 6

            elif positions[7] == "o" and positions[8] == "o":
                x = 7
            elif positions[6] == "o" and positions[8] == "o":
                x = 8
            elif positions[6] == "o" and positions[7] == "o":
                x = 9

            else:
                x = str(random.choice(empties))
            self.widget = ("self.pos_" + str(x))
            self.cross_l = tk.Label(eval(self.widget), image=self.cross, name="x")
            self.cross_l.pack()
            self.counter -= 1
            self.checker()

    def checker(self):
        positions = []
        for x in range(1,10):
            command = "self.pos_" + str(x) + ".winfo_children()"
            if str(eval(command)) == "[]":
                positions.append("e")
            else:
                positions.append(str(eval(command))[38])
        if positions[0] == "o" and positions[3] == "o" and positions[6] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[1] == "o" and positions[4] == "o" and positions[7] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[2] == "o" and positions[5] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[0] == "o" and positions[1] == "o" and positions[2] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[3] == "o" and positions[4] == "o" and positions[5] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[6] == "o" and positions[7] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[0] == "o" and positions[4] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[2] == "o" and positions[4] == "o" and positions[6] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()

        if positions[0] == "x" and positions[3] == "x" and positions[6] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[1] == "x" and positions[4] == "x" and positions[7] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[2] == "x" and positions[5] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[0] == "x" and positions[1] == "x" and positions[2] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[3] == "x" and positions[4] == "x" and positions[5] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[6] == "x" and positions[7] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[0] == "x" and positions[4] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[2] == "x" and positions[4] == "x" and positions[6] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()

        x = False

        for position in positions:
            if position == "e":
                x = True

        if x == False:
            mb.showinfo("DRAW", "There are no winners in life.")
            quit()


class Two:
    def __init__(self, master):
        self.master = master

        self.space = tk.Frame(self.master, width=630, height=630)
        self.space.pack()

        self.counter = 0

        self.nought = ImageTk.PhotoImage(Image.open("nought.jpg").resize((190, 190),Image.ANTIALIAS))
        self.cross = ImageTk.PhotoImage(Image.open("cross.jpg").resize((190, 190), Image.ANTIALIAS))

        self.pos_1 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_1")
        self.pos_1.bind("<Button-1>", self.click)
        self.pos_1.grid(column=0, row=0)

        self.pos_2 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_2")
        self.pos_2.bind("<Button-1>", self.click)
        self.pos_2.grid(column=1, row=0)

        self.pos_3 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_3")
        self.pos_3.bind("<Button-1>", self.click)
        self.pos_3.grid(column=2, row=0)

        self.pos_4 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_4")
        self.pos_4.bind("<Button-1>", self.click)
        self.pos_4.grid(column=0, row=1)

        self.pos_5 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_5")
        self.pos_5.bind("<Button-1>", self.click)
        self.pos_5.grid(column=1, row=1)

        self.pos_6 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_6")
        self.pos_6.bind("<Button-1>", self.click)
        self.pos_6.grid(column=2, row=1)

        self.pos_7 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_7")
        self.pos_7.bind("<Button-1>", self.click)
        self.pos_7.grid(column=0, row=2)

        self.pos_8 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_8")
        self.pos_8.bind("<Button-1>", self.click)
        self.pos_8.grid(column=1, row=2)

        self.pos_9 = tk.Frame(self.space, width=205, height=205, highlightthickness=5, highlightbackground="black", name="pos_9")
        self.pos_9.bind("<Button-1>", self.click)
        self.pos_9.grid(column=2, row=2)

        self.widget = None
        self.nought_l = None
        self.cross_l = None

    def click(self, event):
        self.widget = ("self" + (str(event.widget)[8:]))
        if self.counter == 0:
            self.nought_l = tk.Label(eval(self.widget), image=self.nought, name="o")
            self.nought_l.pack()
            self.counter += 1
        elif self.counter == 1:
            self.cross_l = tk.Label(eval(self.widget), image=self.cross, name="x")
            self.cross_l.pack()
            self.counter -= 1
        self.checker()

    def checker(self):
        positions = []
        for x in range(1,10):
            command = "self.pos_" + str(x) + ".winfo_children()"
            if str(eval(command)) == "[]":
                positions.append("e")
            else:
                positions.append(str(eval(command))[38])
        if positions[0] == "o" and positions[3] == "o" and positions[6] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[1] == "o" and positions[4] == "o" and positions[7] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[2] == "o" and positions[5] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[0] == "o" and positions[1] == "o" and positions[2] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[3] == "o" and positions[4] == "o" and positions[5] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[6] == "o" and positions[7] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[0] == "o" and positions[4] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()
        if positions[2] == "o" and positions[4] == "o" and positions[6] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            quit()

        if positions[0] == "x" and positions[3] == "x" and positions[6] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[1] == "x" and positions[4] == "x" and positions[7] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[2] == "x" and positions[5] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[0] == "x" and positions[1] == "x" and positions[2] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[3] == "x" and positions[4] == "x" and positions[5] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[6] == "x" and positions[7] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[0] == "x" and positions[4] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()
        if positions[2] == "x" and positions[4] == "x" and positions[6] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            quit()

        x = False

        for position in positions:
            if position == "e":
                x = True

        if x == False:
            mb.showinfo("DRAW", "There are no winners in life.")
            quit()


root = tk.Tk()
root.title("Noughts and Crosses")
start = Start(root)
root.mainloop()