import tkinter as tk
from tkinter import messagebox


class MullerLyerIllusion:
    def __init__(self, root):
        self.root = root
        self.root.title("Müller-Lyer Illusion")
        
        self.canvas_width = 800
        self.canvas_height = 500
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()
        
        self.line_x1, self.line_x2 = 150, 650
        self.center_x = (self.line_x1 + self.line_x2) // 2
        self.arrow_offset = 40
        self.line_y = 250
        
        self.midpoint_marker = None
        self.draw_illusion()
        
        self.draggable = self.canvas.create_line(self.center_x, self.line_y, self.center_x - self.arrow_offset, self.line_y - 30, width=4, fill="red")
        self.draggable2 = self.canvas.create_line(self.center_x, self.line_y, self.center_x - self.arrow_offset, self.line_y + 30, width=4, fill="red")
        
        self.canvas.tag_bind(self.draggable, "<B1-Motion>", self.move_arrow)
        self.canvas.tag_bind(self.draggable2, "<B1-Motion>", self.move_arrow)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_position)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.result_button = tk.Button(root, text="Show Result", command=self.show_result)
        self.result_button.pack(side=tk.RIGHT, padx=10, pady=10)
    
    def draw_illusion(self):
        self.canvas.create_line(self.line_x1, self.line_y, self.line_x2, self.line_y, width=6, fill="blue", tags="base_line")
        
        # Left arrows
        self.canvas.create_line(self.line_x1, self.line_y, self.line_x1 - self.arrow_offset, self.line_y - 30, width=4, fill="blue")
        self.canvas.create_line(self.line_x1, self.line_y, self.line_x1 - self.arrow_offset, self.line_y + 30, width=4, fill="blue")
        
        # Right arrows
        self.canvas.create_line(self.line_x2, self.line_y, self.line_x2 + self.arrow_offset, self.line_y - 30, width=4, fill="blue")
        self.canvas.create_line(self.line_x2, self.line_y, self.line_x2 + self.arrow_offset, self.line_y + 30, width=4, fill="blue")
    
    def move_arrow(self, event):
        new_x = event.x
        if self.line_x1 < new_x < self.line_x2:
            self.canvas.coords(self.draggable, new_x, self.line_y, new_x - self.arrow_offset, self.line_y - 30)
            self.canvas.coords(self.draggable2, new_x, self.line_y, new_x - self.arrow_offset, self.line_y + 30)
    
    def reset_position(self):
        self.canvas.coords(self.draggable, self.center_x, self.line_y, self.center_x - self.arrow_offset, self.line_y - 30)
        self.canvas.coords(self.draggable2, self.center_x, self.line_y, self.center_x - self.arrow_offset, self.line_y + 30)
        if self.midpoint_marker:
            self.canvas.delete(self.midpoint_marker)
            self.midpoint_marker = None
    
    def show_result(self):
        user_x = self.canvas.coords(self.draggable)[0]
        offset = user_x - self.center_x
        
        if self.midpoint_marker:
            self.canvas.delete(self.midpoint_marker)
        self.midpoint_marker = self.canvas.create_oval(self.center_x - 5, self.line_y - 5, self.center_x + 5, self.line_y + 5, fill="green")
        
        messagebox.showinfo("Result", f"Your selection is {offset:.2f} pixels from the actual center.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MullerLyerIllusion(root)
    root.mainloop()