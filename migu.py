import tkinter as tk

class migu():
    def __init__(self):
        self.window = tk.Tk()
        
        self._migu = []
        self.frame = 0
        
        for i in range(20):
            self._migu.append(tk.PhotoImage(file="migu.gif", format=f"gif -index {i}"))

        self.image = self._migu[self.frame]
    
        self.window.config(highlightbackground='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'black')
        self.label = tk.Label(self.window, bd=0, bg='black')
        
        self.window.bind("<ButtonPress-1>", self.OnMouseDown)
        self.window.bind("<B1-Motion>", self.OnMouseMove)
        self.window.bind("<ButtonPress-3>", self.close)
        
        self.window.after(0, self.render)
        self.window.mainloop()
        
    def render(self):
        
        self.frame = (self.frame + 1) % len(self._migu)
        self.image = self._migu[self.frame]
        
        self.window.geometry("136x110")
        
        self.label.configure(image=self.image)
        
        self.label.pack()
        
        self.window.after(80, self.render)
        
    def OnMouseDown(self, event):
        self.x = event.x
        self.y = event.y
        
    def OnMouseMove(self, event):
        x = self.window.winfo_pointerx() - self.x
        y = self.window.winfo_pointery() - self.y
        self.window.geometry(f"+{x}+{y}")
        
    def close(self, event):
        self.window.destroy()
    
migu()