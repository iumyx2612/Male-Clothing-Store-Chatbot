import tkinter as tk


def SendMessage():
    send = "You:" + text_box.get(1.0, tk.END)
    display_window.insert(tk.END, "\n" + send)
    text_box.delete(0.0, tk.END)

root = tk.Tk()
#Window
root.geometry("400x600+300+100")
root.resizable(0, 0)
#Title Bar
title_bar = tk.Frame(root)
title_bar.place(x=5, y=0)
label = tk.Label(title_bar, text="CHATBOT", bg="dodger blue", font=("Helvetica", 20, "bold"), relief="flat", fg="white")
label.pack(fill=tk.X)
close_button = tk.Button(label, text="X", command=root.destroy).pack(side=tk.RIGHT)
title_bar.pack(fill=tk.X)
icon = tk.PhotoImage(file="brain-network.png")
image_label = tk.Label(label, width=30, height=30, image=icon)
image_label.pack(side=tk.LEFT)
#Chat window
display_window = tk.Text(root, height=30, bg="gray75")
display_window.pack(fill=tk.X)
#Type window
type_window = tk.Frame(root)
type_window.pack()
send_button = tk.Button(type_window, text="Send", bg="peach puff", command=SendMessage)
send_button.pack(side=tk.RIGHT, fill=tk.Y)
text_box = tk.Text(type_window, bg="white")
text_box.pack(fill=tk.X)



tk.mainloop()
