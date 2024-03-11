import customtkinter as ctk


class UI(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Asset Library Import")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Settings

        self.frame_settings_title = ctk.CTkFrame(self)
        self.frame_settings_title.grid(row=0, column=0, sticky="new")
        self.frame_settings_title.grid_rowconfigure(0, weight=0)
        self.frame_settings_title.grid_columnconfigure(0, weight=1)

        self.settings_title = ctk.CTkLabel(self.frame_settings_title, text="Settings", font=ctk.CTkFont(size=16, weight="bold"))
        self.settings_title.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.appearance_mode_value = ctk.StringVar()
        self.appearance_mode = ctk.CTkSwitch(self.frame_settings_title, command=self._changeAppearanceMode, variable=self.appearance_mode_value, onvalue="on", offvalue="off", text="", width=36)
        self.appearance_mode.grid(row=0, column=1, sticky="e", padx=10, pady=5)
        
        self.frame_settings = ctk.CTkFrame(self, bg_color="transparent", fg_color="transparent")
        self.frame_settings.grid(row=1, column=0, sticky="new", padx=7, pady=7)
        self.frame_settings.grid_rowconfigure((0, 1), weight=0)
        self.frame_settings.grid_columnconfigure((0, 2), weight=0)
        self.frame_settings.grid_columnconfigure(1, weight=1, minsize=350)
        
        self.source_label = ctk.CTkLabel(self.frame_settings, text="Source")
        self.source_label.grid(row=1, column=0, padx=5, pady=5, sticky="new")

        self.source_path = ctk.CTkEntry(self.frame_settings)
        self.source_path.grid(row=1, column=1, padx=0, pady=5, sticky="new")

        self.source_btn = ctk.CTkButton(self.frame_settings, text="Browse")
        self.source_btn.grid(row=1, column=2, padx=5, pady=5, sticky="new")

        self.destination_label = ctk.CTkLabel(self.frame_settings, text="Destination")
        self.destination_label.grid(row=2, column=0, padx=5, pady=5, sticky="new")

        self.destination_path = ctk.CTkEntry(self.frame_settings)
        self.destination_path.grid(row=2, column=1, padx=0, pady=5, sticky="new")

        self.destination_btn = ctk.CTkButton(self.frame_settings, text="Browse")
        self.destination_btn.grid(row=2, column=2, padx=5, pady=5, sticky="new")

        self.scan_btn = ctk.CTkButton(self.frame_settings, text="Scan")
        self.scan_btn.grid(row=3, column=2, padx=5, pady=5, sticky="e")

        # Files

        self.frame_files_title = ctk.CTkFrame(self)
        self.frame_files_title.grid(row=2, column=0, sticky="new")
        self.frame_files_title.grid_rowconfigure(0, weight=0)
        self.frame_files_title.grid_columnconfigure(0, weight=1)

        self.settings_title = ctk.CTkLabel(self.frame_files_title, text="Files", font=ctk.CTkFont(size=16, weight="bold"))
        self.settings_title.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.frame_files_headers = ctk.CTkFrame(self, bg_color="transparent", fg_color="transparent")
        self.frame_files_headers.grid(row=3, column=0, sticky="nsew")
        self.frame_files_headers.grid_rowconfigure(0, weight=0)
        self.frame_files_headers.grid_columnconfigure((0, 1, 2), weight=1)

        self.file_header_filename = ctk.CTkLabel(self.frame_files_headers, text="Filename")
        self.file_header_filename.grid(row=0, column=0, padx=10, pady=0, sticky="n")

        self.file_header_type = ctk.CTkLabel(self.frame_files_headers, text="Type")
        self.file_header_type.grid(row=0, column=1, padx=10, pady=0, sticky="n")

        self.file_header_material = ctk.CTkLabel(self.frame_files_headers, text="Material")
        self.file_header_material.grid(row=0, column=2, padx=10, pady=0, sticky="n")

        self.frame_files = ctk.CTkScrollableFrame(self, bg_color="transparent", fg_color="transparent")
        self.frame_files.grid(row=4, column=0, sticky="nsew")
        self.frame_files.grid_columnconfigure((0, 1, 2), weight=1)

        for i in range(20):
            file_switch = ctk.CTkCheckBox(self.frame_files, text=f"File_{i}.fbx")
            if i%3 > 0:
                file_switch.select()
            file_switch.grid(row=i, column=0, sticky="n")

            file_types = ["Building", "Road", "Intersection", "Prop"]
            file_type = ctk.CTkComboBox(self.frame_files, values=file_types)
            file_type.grid(row=i, column=1, sticky="n", pady=3)
            file_type.set(file_types[i%len(file_types)])

            file_materials = ["Building_001", "Concrete_Dark", "Metal_Pieces_B", "Trim_01"]
            file_material = ctk.CTkComboBox(self.frame_files, values=file_materials)
            file_material.grid(row=i, column=2, sticky="n", pady=3)
            file_material.set(file_materials[i%len(file_materials)])
        
        self.frame_process = ctk.CTkFrame(self, bg_color="transparent", fg_color="transparent")
        self.frame_process.grid(row=5, column=0, sticky="new", padx=7, pady=7)
        self.frame_process.grid_rowconfigure(0, weight=0)
        self.frame_process.grid_columnconfigure(0, weight=1)

        self.scan_btn = ctk.CTkProgressBar(self.frame_process)
        self.scan_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.scan_btn.configure(mode="indeterminnate")
        self.scan_btn.start()

        self.scan_btn = ctk.CTkButton(self.frame_process, text="Process Files")
        self.scan_btn.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.log = ctk.CTkTextbox(self.frame_process, height=100)
        self.log.insert("0.0", "15:52 - Searching source folder.\n")
        self.log.insert("end", "15:53 - 234 files found in source folder.\n")
        self.log.insert("end", "15:53 - Searching destination folder.\n")
        self.log.insert("end", "15:53 - 351 files found in destination folder.\n")
        self.log.insert("end", "15:53 - 117 new files, 29 updated files from source, 23 file conflicts.\n")
        self.log.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        self.mainloop()
        
    def _changeAppearanceMode(self):
        if self.appearance_mode_value.get() == "off":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
    ctk.set_default_color_theme("ctk_theme.json")
    ui = UI()