from functions import *
from functions import TurnOn

root=tk.Tk()
canvas = tk.Canvas(root,height = 300,width=700,bg="black")
canvas.pack()

start=tk.Button(root,text = "Turn On Jarvis",padx=10,pady=5,fg="Sky Blue",bg="black",command = TurnOn )
start.pack()
end=tk.Button(root,text = "Turn Off Jarvis",padx=10,pady=5,fg="Sky Blue",bg="black",command = TurnOff )
end.pack()

root.mainloop()