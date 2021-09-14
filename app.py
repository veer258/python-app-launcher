import tkinter as tk

root = tk.Tk()
apps = []

def addApp():
    from tkinter import filedialog
    filename = filedialog.askopenfilename(initialdir = "/", title="Select File", filetypes = (("executables", "*.exe"), ("all files", "*,*")))
    apps.append(filename)

    for wid in frame.winfo_children():
        wid.destroy()

    for app in apps:
        label= tk.Label(frame, text=app, bg="white")
        label.pack()

def runApps():
    for app in apps:
        import os
        os.startfile(app)


canvas= tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()

frame = tk.Frame(root, bg="#474747")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#474747", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#474747", command=runApps)
runApps.pack()

root.mainloop()