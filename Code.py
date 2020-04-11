import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import random
import os


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
        x = ((str(event.widget)).split("."))[2]
        self.widget = ("self." + x)
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
            if positions[0] == "e" and positions[3] == "x" and positions[6] == "x":
                x = 1
            elif positions[3] == "e" and positions[0] == "x" and positions[6] == "x":
                x = 4
            elif positions[6] == "e" and positions[0] == "x" and positions[3] == "x":
                x = 7

            elif positions[1] == "e" and positions[4] == "x" and positions[7] == "x":
                x = 2
            elif positions[4] == "e" and positions[1] == "x" and positions[7] == "x":
                x = 5
            elif positions[7] == "e" and positions[1] == "x" and positions[4] == "x":
                x = 8

            elif positions[2] == "e" and positions[5] == "x" and positions[8] == "x":
                x = 3
            elif positions[5] == "e" and positions[2] == "x" and positions[8] == "x":
                x = 6
            elif positions[8] == "e" and positions[2] == "x" and positions[5] == "x":
                x = 9

            #horizontal winners
            elif positions[0] == "e" and positions[1] == "x" and positions[2] == "x":
                x = 1
            elif positions[1] == "e" and positions[0] == "x" and positions[2] == "x":
                x = 2
            elif positions[2] == "e" and positions[0] == "x" and positions[1] == "x":
                x = 3

            elif positions[3] == "e" and positions[4] == "x" and positions[5] == "x":
                x = 4
            elif positions[4] == "e" and positions[3] == "x" and positions[5] == "x":
                x = 5
            elif positions[5] == "e" and positions[3] == "x" and positions[4] == "x":
                x = 6

            elif positions[6] == "e" and positions[7] == "x" and positions[8] == "x":
                x = 7
            elif positions[7] == "e" and positions[6] == "x" and positions[8] == "x":
                x = 8
            elif positions[8] == "e" and positions[6] == "x" and positions[7] == "x":
                x = 9

            #diagonal winners
            elif positions[0] == "e" and positions[4] == "x" and positions[8] == "x":
                x = 1
            elif positions[4] == "e" and positions[0] == "x" and positions[8] == "x":
                x = 5
            elif positions[8] == "e" and positions[4] == "x" and positions[0] == "x":
                x = 9

            elif positions[2] == "e" and positions[4] == "x" and positions[6] == "x":
                x = 3
            elif positions[4] == "e" and positions[2] == "x" and positions[6] == "x":
                x = 5
            elif positions[6] == "e" and positions[4] == "x" and positions[2] == "x":
                x = 7

            # vertical blockers
            elif positions[0] == "e" and positions[3] == "o" and positions[6] == "o":
                x = 1
            elif positions[3] == "e" and positions[0] == "o" and positions[6] == "o":
                x = 4
            elif positions[6] == "e" and positions[0] == "o" and positions[3] == "o":
                x = 7

            elif positions[1] == "e" and positions[4] == "o" and positions[7] == "o":
                x = 2
            elif positions[4] == "e" and positions[1] == "o" and positions[7] == "o":
                x = 5
            elif positions[7] == "e" and positions[1] == "o" and positions[4] == "o":
                x = 8

            elif positions[2] == "e" and positions[5] == "o" and positions[8] == "o":
                x = 3
            elif positions[5] == "e" and positions[2] == "o" and positions[8] == "o":
                x = 6
            elif positions[8] == "e" and positions[2] == "o" and positions[5] == "o":
                x = 9

            # horizontal blockers
            elif positions[0] == "e" and positions[1] == "o" and positions[2] == "o":
                x = 1
            elif positions[1] == "e" and positions[0] == "o" and positions[2] == "o":
                x = 2
            elif positions[2] == "e" and positions[0] == "o" and positions[1] == "o":
                x = 3

            elif positions[3] == "e" and positions[4] == "o" and positions[5] == "o":
                x = 4
            elif positions[4] == "e" and positions[3] == "o" and positions[5] == "o":
                x = 5
            elif positions[5] == "e" and positions[3] == "o" and positions[4] == "o":
                x = 6

            elif positions[6] == "e" and positions[7] == "o" and positions[8] == "o":
                x = 7
            elif positions[7] == "e" and positions[6] == "o" and positions[8] == "o":
                x = 8
            elif positions[8] == "e" and positions[6] == "o" and positions[7] == "o":
                x = 9

            # diagonal blockers
            elif positions[0] == "e" and positions[4] == "o" and positions[8] == "o":
                x = 1
            elif positions[4] == "e" and positions[0] == "o" and positions[8] == "o":
                x = 5
            elif positions[8] == "e" and positions[4] == "o" and positions[0] == "o":
                x = 9

            elif positions[2] == "e" and positions[4] == "o" and positions[6] == "o":
                x = 3
            elif positions[4] == "e" and positions[2] == "o" and positions[6] == "o":
                x = 5
            elif positions[6] == "e" and positions[4] == "o" and positions[2] == "o":
                x = 7


            #positions start at 0 and x starts at 1

            #corner for centre
            elif positions[0] == "e" and positions[1] == "e" and positions[2] == "e" and positions[3] == "e" and positions[4] == "o" and positions[5] == "e" and positions[6] == "e" and positions[7] == "e" and positions[8] == "e":
                x = str(random.choice([1, 3, 7, 9]))

            #centre or adjacent corner for edge
            elif len(empties) == 8 and positions[1] == "o":
                x = str(random.choice([1, 3, 5]))
            elif len(empties) == 8 and positions[3] == "o":
                x = str(random.choice([1, 5, 7]))
            elif len(empties) == 8 and positions[5] == "o":
                x = str(random.choice([3, 5, 9]))
            elif len(empties) == 8 and positions[7] == "o":
                x = str(random.choice([5, 7, 9]))

            #centre for corner
            elif len(empties) == 8 and positions[0] == "o":
                x = 5
            elif len(empties) == 8 and positions[2] == "o":
                x = 5
            elif len(empties) == 8 and positions[6] == "o":
                x = 5
            elif len(empties) == 8 and positions[8] == "o":
                x = 5

            #dominate centre
            elif len(empties) == 7 and positions[5] == "o" and positions[7] == "o":
                x = 5
            elif len(empties) == 7 and positions[3] == "o" and positions[7] == "o":
                x = 5
            elif len(empties) == 7 and positions[1] == "o" and positions[3] == "o":
                x = 5
            elif len(empties) == 7 and positions[1] == "o" and positions[5] == "o":
                x = 5

            #block opposite diagonal forks
            elif len(empties) == 6 and positions[0] == "o" and positions[8] == "o":
                x = str(random.choice([2, 4, 6, 8]))
            elif len(empties) == 6 and positions[2] == "o" and positions[6] == "o":
                x = str(random.choice([2, 4, 6, 8]))

            #block triangle forks
            elif len(empties) == 6 and positions[4] == "o" and positions[0] == "o":
                temp = empties
                temp = list(filter(lambda x: x!= 2 and 4 and 6 and 8, temp))
                x = str(random.choice(temp))
            elif len(empties) == 6 and positions[4] == "o" and positions[2] == "o":
                temp = empties
                temp = list(filter(lambda x: x != 2 and 4 and 6 and 8, temp))
                x = str(random.choice(temp))
            elif len(empties) == 6 and positions[4] == "o" and positions[6] == "o":
                temp = empties
                temp = list(filter(lambda x: x != 2 and 4 and 6 and 8, temp))
                x = str(random.choice(temp))
            elif len(empties) == 6 and positions[4] == "o" and positions[8] == "o":
                temp = empties
                temp = list(filter(lambda x: x != 2 and 4 and 6 and 8, temp))
                x = str(random.choice(temp))

            #block fork 4
            elif len(empties) == 6 and positions[7] == "o" and positions[2] == "o" and positions[4] == "e":
                x = 5
            elif len(empties) == 6 and positions[7] == "o" and positions[0] == "o" and positions[4] == "e":
                x = 5
            elif len(empties) == 6 and positions[3] == "o" and positions[2] == "o" and positions[4] == "e":
                x = 5
            elif len(empties) == 6 and positions[3] == "o" and positions[8] == "o" and positions[4] == "e":
                x = 5
            elif len(empties) == 6 and positions[1] == "o" and positions[6] == "o" and positions[4] == "e":
                x = 5
            elif len(empties) == 6 and positions[1] == "o" and positions[8] == "o" and positions[4] == "e":
                x = 5
            elif len(empties) == 6 and positions[5] == "o" and positions[0] == "o" and positions[4] == "e":
                x = 5
            elif len(empties) == 6 and positions[5] == "o" and positions[6] == "o" and positions[4] == "e":
                x = 5

            #block fork 5
            elif len(empties) == 6 and positions[7] == "o" and positions[8] == "o":
                x = str(random.choice([1, 2]))
            elif len(empties) == 6 and positions[7] == "o" and positions[6] == "o":
                x = str(random.choice([2, 3]))
            elif len(empties) == 6 and positions[0] == "o" and positions[1] == "o":
                x = str(random.choice([8, 9]))
            elif len(empties) == 6 and positions[1] == "o" and positions[2] == "o":
                x = str(random.choice([7, 8]))
            elif len(empties) == 6 and positions[0] == "o" and positions[3] == "o":
                x = str(random.choice([6, 9]))
            elif len(empties) == 6 and positions[3] == "o" and positions[6] == "o":
                x = str(random.choice([3, 6]))
            elif len(empties) == 6 and positions[2] == "o" and positions[5] == "o":
                x = str(random.choice([4, 7]))
            elif len(empties) == 6 and positions[5] == "o" and positions[8] == "o":
                x = str(random.choice([1, 4]))

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
            os._exit(1)
        if positions[1] == "o" and positions[4] == "o" and positions[7] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[2] == "o" and positions[5] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[0] == "o" and positions[1] == "o" and positions[2] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[3] == "o" and positions[4] == "o" and positions[5] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[6] == "o" and positions[7] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[0] == "o" and positions[4] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[2] == "o" and positions[4] == "o" and positions[6] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)

        if positions[0] == "x" and positions[3] == "x" and positions[6] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[1] == "x" and positions[4] == "x" and positions[7] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[2] == "x" and positions[5] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[0] == "x" and positions[1] == "x" and positions[2] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[3] == "x" and positions[4] == "x" and positions[5] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[6] == "x" and positions[7] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[0] == "x" and positions[4] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[2] == "x" and positions[4] == "x" and positions[6] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)

        x = False

        for position in positions:
            if position == "e":
                x = True

        if not x:
            mb.showinfo("DRAW", "There are no winners in life.")
            os._exit(1)


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
            os._exit(1)
        if positions[1] == "o" and positions[4] == "o" and positions[7] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[2] == "o" and positions[5] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[0] == "o" and positions[1] == "o" and positions[2] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[3] == "o" and positions[4] == "o" and positions[5] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[6] == "o" and positions[7] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[0] == "o" and positions[4] == "o" and positions[8] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)
        if positions[2] == "o" and positions[4] == "o" and positions[6] == "o":
            mb.showinfo("WINNER", "Noughts wins")
            os._exit(1)

        if positions[0] == "x" and positions[3] == "x" and positions[6] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[1] == "x" and positions[4] == "x" and positions[7] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[2] == "x" and positions[5] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[0] == "x" and positions[1] == "x" and positions[2] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[3] == "x" and positions[4] == "x" and positions[5] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[6] == "x" and positions[7] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[0] == "x" and positions[4] == "x" and positions[8] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)
        if positions[2] == "x" and positions[4] == "x" and positions[6] == "x":
            mb.showinfo("WINNER", "Crosses wins")
            os._exit(1)

        x = False

        for position in positions:
            if position == "e":
                x = True

        if not x:
            mb.showinfo("DRAW", "There are no winners in life.")
            os._exit(1)


root = tk.Tk()
root.title("Noughts and Crosses")
x = 0
start = Start(root)
root.mainloop()
