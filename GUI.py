import tkinter as tk
from Prj.ChatBot import Chat


class Application(tk.Frame):
    def SendMessage(self):
        send = "You:" + self.text_box.get(1.0, tk.END)
        self.display_window.insert(tk.END, "\n" + send)
        self.text_box.delete(0.0, tk.END)

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        # title bar
        self.title_bar = tk.Frame(self.master)
        self.title_bar.place(x=5, y=0)
        self.label = tk.Label(self.title_bar, text="CHATBOT", bg="dodger blue", font=("Helvetica", 20, "bold"),
                              relief="flat", fg="white")
        self.label.pack(fill=tk.X)
        self.close_button = tk.Button(self.label, text="X", command=self.master.destroy)
        self.close_button.pack(side=tk.RIGHT)
        self.title_bar.pack(fill=tk.X)
        self.icon = tk.PhotoImage(file="brain-network.png")
        self.image_label = tk.Label(self.label, width=30, height=30, image=self.icon)
        self.image_label.pack(side=tk.LEFT)
        # chat window
        self.display_window = tk.Text(self.master, height=30, bg="grey75")
        self.display_window.pack(fill=tk.X)
        # type window
        self.type_window = tk.Frame(root)
        self.type_window.pack()
        self.send_button = tk.Button(self.type_window, text="Send", bg="peach puff", command=self.SendMessage)
        self.send_button.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_box = tk.Text(self.type_window, bg="white")
        self.text_box.pack(fill=tk.X)


def MoveWindow(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


root = tk.Tk()
a = Application(root)
a.label.bind('<B1-Motion>', MoveWindow)
root.overrideredirect(True)
root.geometry("400x600+300+100")
root.resizable(0, 0)
root.mainloop()
