import tkinter as tk

root = tk.Tk()

try:
    text_file = open('database.txt', 'r')
    lines = text_file.readlines()
    apps = []
    for i in lines:
        apps.append(i.rstrip(i[-1]))
        # print("HI THIS IS " + (i.rstrip(i[-1])))
    print(apps)
    
except:
    apps = []


def addApp():
    from tkinter import filedialog
    filename = filedialog.askopenfilename(initialdir = "/", title="Select File", filetypes = (("executables", "*.exe"), ("all files", "*,*")))

    if filename == "":
        return "Operation Cancelled"

    apps.append(filename)

    for wid in frame.winfo_children():
        wid.destroy()

    for app in apps:
        label= tk.Label(frame, text=app, bg="white")
        label.pack()

    # app_list = '['
    # for app in apps:
    #     app_list += (app + ",")
    # app_list = app_list.rstrip(app_list[-1])
    # app_list += "]"

    app_list = ''''''
    for app in apps:
        app_list += (
            app + '\n'
        )

    import os
    with open('database.txt', 'w') as f:
        f.write(app_list)


def runApps():
    for app in apps:
        import os
        os.startfile(app)

canvas= tk.Canvas(root, height=500, width=600, bg="#000000")
canvas.pack()

frame = tk.Frame(root, bg="#474747")
frame.place(relwidth=0.7, relheight=0.7, relx=0.1, rely=0.1)

for app in apps:
    label= tk.Label(frame, text=app, bg="white")
    label.pack()

chooseFile = tk.Button(root, text="Choose File", padx=10, pady=5, fg="white", bg="#474747", command=addApp)
chooseFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#474747", command=runApps)
runApps.pack()

root.mainloop()