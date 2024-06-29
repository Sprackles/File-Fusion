import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


class FileFusionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FileFusion")
        self.root.geometry("500x400")
        self.root.resizable(False, False)  # Lock the resizing of the window
        self.file_list = []

        self.setup_style()

        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.label = ttk.Label(main_frame, text="Selected Files:", style="TLabel")
        self.label.pack(pady=5)

        self.file_display = tk.Text(main_frame, height=10, width=50, bg="#1e1e1e", fg="#d4d4d4",
                                    insertbackground="#d4d4d4")
        self.file_display.pack(pady=5, fill=tk.BOTH, expand=True)

        self.select_button = ttk.Button(main_frame, text="Select Files", command=self.select_files, style="TButton")
        self.select_button.pack(pady=5)

        self.run_button = ttk.Button(main_frame, text="Run", command=self.combine_files, style="Accent.TButton")
        self.run_button.pack(pady=5)

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        # General style
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TLabel", background="#1e1e1e", foreground="#d4d4d4", font=("Helvetica", 10))
        style.configure("TButton", background="#2d2d2d", foreground="#d4d4d4", borderwidth=0, font=("Helvetica", 10))
        style.map("TButton",
                  background=[("active", "#3e3e3e")],
                  foreground=[("active", "#ffffff")])

        # Accent button style
        style.configure("Accent.TButton", background="#007acc", foreground="#ffffff", borderwidth=0,
                        font=("Helvetica", 10))
        style.map("Accent.TButton",
                  background=[("active", "#005bb5")],
                  foreground=[("active", "#ffffff")])

        # Style for text widget (not native ttk, so custom styling)
        self.root.option_add("*Text.Background", "#1e1e1e")
        self.root.option_add("*Text.Foreground", "#d4d4d4")
        self.root.option_add("*Text.Font", "Helvetica 10")
        self.root.option_add("*Text.InsertBackground", "#d4d4d4")

    def select_files(self):
        initial_dir = os.path.dirname(os.path.abspath(__file__))
        files = filedialog.askopenfilenames(title="Select files", initialdir=initial_dir)
        if files:
            self.file_list.extend(files)
            self.update_file_display()

    def update_file_display(self):
        self.file_display.delete(1.0, tk.END)
        for file_path in self.file_list:
            relative_path = os.path.relpath(file_path)
            self.file_display.insert(tk.END, f"{relative_path}\n")

    def combine_files(self):
        output_file = 'all_text_combined.txt'

        try:
            with open(output_file, 'w') as outfile:
                for file_path in self.file_list:
                    if os.path.exists(file_path):
                        relative_path = os.path.relpath(file_path)
                        outfile.write(f"===== {relative_path} =====\n")
                        with open(file_path, 'r') as infile:
                            outfile.write(infile.read())
                        outfile.write("\n\n")
                    else:
                        messagebox.showerror("Error", f"File {file_path} does not exist")

            messagebox.showinfo("Success", f"All text has been combined into {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileFusionApp(root)
    root.mainloop()
