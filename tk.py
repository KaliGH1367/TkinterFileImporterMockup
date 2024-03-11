import tkinter as tk


class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Asset Library Import")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Settings

        self.frame_settings_title = tk.Frame(self)
        self.frame_settings_title.grid(row=0, column=0, sticky="new")
        self.frame_settings_title.grid_rowconfigure(0, weight=0)
        self.frame_settings_title.grid_columnconfigure(0, weight=1)

        self.settings_title = tk.Label(self.frame_settings_title, text="Settings")
        self.settings_title.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        self.frame_settings = tk.Frame(self)
        self.frame_settings.grid(row=1, column=0, sticky="new", padx=7, pady=7)
        self.frame_settings.grid_rowconfigure((0, 1), weight=0)
        self.frame_settings.grid_columnconfigure((0, 2), weight=0)
        self.frame_settings.grid_columnconfigure(1, weight=1, minsize=350)
        
        self.source_label = tk.Label(self.frame_settings, text="Source")
        self.source_label.grid(row=1, column=0, padx=5, pady=5, sticky="new")
        
        self.source_path_var = tk.StringVar()
        self.source_path_var.set("D:\\Rebelway_Project\\Source_Files\\")
        self.source_path = tk.Entry(self.frame_settings, textvariable=self.source_path_var)
        self.source_path.grid(row=1, column=1, padx=0, pady=5, sticky="new")

        self.source_btn = tk.Button(self.frame_settings, text="Browse")
        self.source_btn.grid(row=1, column=2, padx=5, pady=5, sticky="new")

        self.destination_label = tk.Label(self.frame_settings, text="Destination")
        self.destination_label.grid(row=2, column=0, padx=5, pady=5, sticky="new")

        self.destination_path_var = tk.StringVar()
        self.destination_path_var.set("D:\\Rebelway_Project\\Output_Files\\")
        self.destination_path = tk.Entry(self.frame_settings, textvariable=self.destination_path_var)
        self.destination_path.grid(row=2, column=1, padx=0, pady=5, sticky="new")

        self.destination_btn = tk.Button(self.frame_settings, text="Browse")
        self.destination_btn.grid(row=2, column=2, padx=5, pady=5, sticky="new")

        self.scan_btn = tk.Button(self.frame_settings, text="Scan")
        self.scan_btn.grid(row=3, column=2, padx=5, pady=5, sticky="e")
        
        # Files

        self.frame_files_title = tk.Frame(self)
        self.frame_files_title.grid(row=2, column=0, sticky="new")
        self.frame_files_title.grid_rowconfigure(0, weight=0)
        self.frame_files_title.grid_columnconfigure(0, weight=1)
        
        self.settings_title = tk.Label(self.frame_files_title, text="Files")
        self.settings_title.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        self.scrollbar_files = tk.Scrollbar(self, orient="vertical")
        self.scrollbar_files.grid(row=4, column=1, sticky="nse")
        
        self.canvas_files = tk.Canvas(self, height=200, wrap=None, yscrollcommand=self.scrollbar_files.set)
        self.canvas_files.grid(row=4, column=0, sticky="new")
        self.canvas_files.grid_columnconfigure(0, weight=1)

        self.scrollbar_files.config(command=self.canvas_files.yview)

        self.frame_files = tk.Frame(self.canvas_files)
        self.frame_files.grid(row=0, column=0, sticky="nsew")
        self.frame_files.grid_columnconfigure(0, weight=1)
        self.frame_files.bind("<Configure>", self.on_frame_configure)
        self.canvas_files.create_window((10,0), window=self.frame_files, anchor="nw")

        for i in range(50):
            file_switch = tk.Checkbutton(self.frame_files, text=f"File_{i}.fbx")
            if i%3 > 0:
                file_switch.select()
            file_switch.grid(row=i, column=0, sticky="n", padx=20)
            
            types = ["Building", "Road", "Intersection", "Prop"]
            type_label = tk.Label(self.frame_files, text=types[i%len(types)])
            type_label.grid(row=i, column=1, sticky="n", padx=20)
            
            materials = ["Building_001", "Concrete_Dark", "Metal_Pieces_B", "Trim_01"]
            material_label = tk.Label(self.frame_files, text=materials[i%len(materials)])
            material_label.grid(row=i, column=2, sticky="n", padx=20)
        
        
        self.frame_process = tk.Frame(self)
        self.frame_process.grid(row=5, column=0, sticky="new", padx=7, pady=7)
        self.frame_process.grid_rowconfigure(0, weight=0)
        self.frame_process.grid_columnconfigure(0, weight=1)

        self.scan_btn = tk.Button(self.frame_process, text="Process Files")
        self.scan_btn.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        
        self.log = tk.Text(self.frame_process, height=10)
        self.log.insert("0.0", "15:52 - Searching source folder.\n")
        self.log.insert("end", "15:53 - 234 files found in source folder.\n")
        self.log.insert("end", "15:53 - Searching destination folder.\n")
        self.log.insert("end", "15:53 - 351 files found in destination folder.\n")
        self.log.insert("end", "15:53 - 117 new files, 29 updated files from source, 23 file conflicts.\n")
        self.log.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        
        self.mainloop()
    
    def on_frame_configure(self, event):
        self.canvas_files.configure(scrollregion=self.canvas_files.bbox("all"))

if __name__ == "__main__":
    ui = UI()