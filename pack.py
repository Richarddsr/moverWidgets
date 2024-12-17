import tkinter as tk

root = tk.Tk()
root.title("Gerenciador pack() 🌟")
root.geometry("400x400")
root.configure(bg="lightblue")

label1 = tk.Label(root, text="Label 1 (TOP)", font=("Arial", 10), bg="white", fg="black")
label1.pack(pady=10, fill=tk.X)

label4 = tk.Label(root, text="Label 4 (BOTTOM)", font=("Arial", 10), bg="white", fg="black")
label4.pack(side=tk.BOTTOM, pady=10, fill=tk.X)

label2 = tk.Label(root, text="Label 2 (LEFT)", font=("Arial", 10), bg="white", fg="black")
label2.pack(side=tk.LEFT, padx=10, fill=tk.Y)

label3 = tk.Label(root, text="Label 3 (RIGHT)", font=("Arial", 10), bg="white", fg="black")
label3.pack(side=tk.RIGHT, padx=10, fill=tk.Y)

root.mainloop()