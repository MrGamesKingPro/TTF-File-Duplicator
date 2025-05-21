import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import shutil
import glob

# --- Default Configuration (can be overridden by GUI) ---
DEFAULT_TTF_SOURCE_FOLDER = ".\\TTF_Source" # Renamed for clarity
DEFAULT_NAMING_SOURCE_FOLDER = ".\\Original_Fonts_Game_Names" # Renamed for clarity
DEFAULT_DESTINATION_FOLDER = ".\\Output_Folder_Fonts" # Renamed for clarity

class TtfDuplicatorApp:
    def __init__(self, master):
        self.master = master
        master.title("TTF File Duplicator By MrGamesKingPro")
        master.geometry("600x500") # Adjusted size for better layout

        # --- Variables for Entry fields ---
        self.ttf_source_var = tk.StringVar(value=DEFAULT_TTF_SOURCE_FOLDER)
        self.naming_source_var = tk.StringVar(value=DEFAULT_NAMING_SOURCE_FOLDER)
        self.destination_var = tk.StringVar(value=DEFAULT_DESTINATION_FOLDER)

        # --- GUI Layout ---
        frame = tk.Frame(master, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        # TTF Source Folder
        tk.Label(frame, text="TTF Source (File or Folder):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.ttf_entry = tk.Entry(frame, textvariable=self.ttf_source_var, width=50)
        self.ttf_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        # Changed button text and title passed to browse_folder for specific file selection
        tk.Button(frame, text="Browse File...", command=lambda: self.browse_folder(self.ttf_source_var, "TTF Source File")).grid(row=0, column=2, pady=2)

        # Naming Source Folder
        tk.Label(frame, text="Naming Source Folder:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.naming_entry = tk.Entry(frame, textvariable=self.naming_source_var, width=50)
        self.naming_entry.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)
        tk.Button(frame, text="Browse Folder...", command=lambda: self.browse_folder(self.naming_source_var, "Naming Source Folder")).grid(row=1, column=2, pady=2)

        # Destination Folder
        tk.Label(frame, text="Destination Folder:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.dest_entry = tk.Entry(frame, textvariable=self.destination_var, width=50)
        self.dest_entry.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=2)
        tk.Button(frame, text="Browse Folder...", command=lambda: self.browse_folder(self.destination_var, "Destination Folder")).grid(row=2, column=2, pady=2)

        # Run Button
        self.run_button = tk.Button(frame, text="Run Duplication Process", command=self.run_process, bg="lightblue", font=('Arial', 10, 'bold'))
        self.run_button.grid(row=3, column=0, columnspan=3, pady=15, ipady=5)

        # Log Area
        tk.Label(frame, text="Log:").grid(row=4, column=0, sticky=tk.W, pady=(5,0))
        self.log_area = scrolledtext.ScrolledText(frame, height=15, width=70, wrap=tk.WORD)
        self.log_area.grid(row=5, column=0, columnspan=3, sticky=tk.EW + tk.NS, pady=5)

        frame.grid_columnconfigure(1, weight=1) # Make entry column expandable
        frame.grid_rowconfigure(5, weight=1)    # Make log area expandable

    def browse_folder(self, entry_var, title="Select Folder"):
        # If the title indicates TTF Source File, open a file dialog
        if title == "TTF Source File":
            file_selected = filedialog.askopenfilename(
                title=title,  # This title will appear on the dialog window
                filetypes=(("TTF files", "*.ttf"), ("All files", "*.*"))
            )
            if file_selected:
                entry_var.set(file_selected)
            return # Important to return so it doesn't fall through to askdirectory

        # Default behavior: browse for a folder
        folder_selected = filedialog.askdirectory(title=title)
        if folder_selected:
            entry_var.set(folder_selected)

    def log(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END) # Auto-scroll
        self.master.update_idletasks() # Force GUI update

    def run_process(self):
        self.log_area.delete(1.0, tk.END) # Clear previous logs

        ttf_source_path = self.ttf_source_var.get()
        naming_source_folder = self.naming_source_var.get()
        destination_folder = self.destination_var.get()

        # --- Validate paths ---
        if not ttf_source_path or not naming_source_folder or not destination_folder:
            messagebox.showerror("Error", "All folder paths must be specified.")
            self.log("ERROR: All folder paths must be specified.")
            return

        self.log(f"--- Configuration ---")
        self.log(f"TTF Source Path: \"{ttf_source_path}\"")
        self.log(f"Naming Source Folder: \"{naming_source_folder}\"")
        self.log(f"Destination Folder: \"{destination_folder}\"")
        self.log(f"--- End Configuration ---\n")

        # --- Dynamically find the .ttf file to duplicate ---
        file_to_duplicate = None
        self.log(f"Inspecting TTF source path: \"{ttf_source_path}\"...")

        if os.path.isfile(ttf_source_path) and ttf_source_path.lower().endswith(".ttf"):
            file_to_duplicate = ttf_source_path
            self.log(f"Using direct TTF file as source: \"{file_to_duplicate}\"")
        elif os.path.isdir(ttf_source_path):
            self.log(f"TTF source is a folder. Searching for a .ttf file in \"{ttf_source_path}\"...")
            ttf_files_found = glob.glob(os.path.join(ttf_source_path, "*.ttf"))
            if ttf_files_found:
                file_to_duplicate = ttf_files_found[0] # Take the first one
                self.log(f"Found TTF file to use as source: \"{file_to_duplicate}\"")
            else:
                self.log(f"No .ttf files found in folder \"{ttf_source_path}\".")
                messagebox.showerror("Error", f"No .ttf files found in source folder \"{ttf_source_path}\".")
                return
        else: # Path doesn't exist or is not a valid file/dir
            self.log(f"TTF source path \"{ttf_source_path}\" not found or is not a valid .ttf file or directory.")
            messagebox.showerror("Error", f"TTF source path \"{ttf_source_path}\" not found or is not a valid .ttf file or directory.")
            return

        # Check if the naming source folder exists
        if not os.path.isdir(naming_source_folder):
            self.log(f"Naming source folder \"{naming_source_folder}\" not found or is not a directory.")
            messagebox.showerror("Error", f"Naming source folder \"{naming_source_folder}\" not found.")
            return

        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            self.log(f"Creating destination folder: \"{destination_folder}\"")
            try:
                os.makedirs(destination_folder)
            except OSError as e:
                self.log(f"Failed to create destination folder: {e}")
                messagebox.showerror("Error", f"Failed to create destination folder: {e}")
                return
        elif not os.path.isdir(destination_folder):
            self.log(f"Destination path \"{destination_folder}\" exists but is not a directory.")
            messagebox.showerror("Error", f"Destination path \"{destination_folder}\" exists but is not a directory.")
            return
        else:
            self.log(f"Destination folder \"{destination_folder}\" already exists. Files will be added/overwritten there.")

        self.log(f"\nProcessing files from \"{naming_source_folder}\" to generate names...")
        files_copied_count = 0
        errors_count = 0

        # Iterate through items in naming_source_folder
        for item_name in os.listdir(naming_source_folder):
            item_path = os.path.join(naming_source_folder, item_name)

            if os.path.isfile(item_path):
                new_filename = item_name
                self.log(f"Using name: \"{new_filename}\" (from \"{item_name}\")")

                destination_file = os.path.join(destination_folder, new_filename)

                self.log(f"  Copying \"{file_to_duplicate}\" to: \"{destination_file}\"")
                try:
                    shutil.copy2(file_to_duplicate, destination_file) # copy2 preserves metadata
                    files_copied_count +=1
                except Exception as e:
                    self.log(f"    ERROR: Failed to copy \"{file_to_duplicate}\" to \"{destination_file}\": {e}")
                    errors_count +=1
            else:
                self.log(f"Skipping directory or non-file item: \"{item_name}\" in naming source folder.")


        self.log(f"\n--- Summary ---")
        self.log(f"Done. {files_copied_count} file(s) copied.")
        if errors_count > 0:
            self.log(f"{errors_count} error(s) occurred.")
            messagebox.showwarning("Process Complete with Errors", f"{files_copied_count} file(s) copied.\n{errors_count} error(s) occurred.\nCheck log for details.")
        else:
            self.log("Process completed successfully.")
            messagebox.showinfo("Process Complete", f"Done. {files_copied_count} file(s) copied to \"{destination_folder}\".")

if __name__ == "__main__":
    # --- Create dummy folders and files for testing if they don't exist ---
    # TTF Source Folder setup
    if not os.path.exists(DEFAULT_TTF_SOURCE_FOLDER):
        os.makedirs(DEFAULT_TTF_SOURCE_FOLDER)
        


    # Naming Source Folder setup
    if not os.path.exists(DEFAULT_NAMING_SOURCE_FOLDER):
        os.makedirs(DEFAULT_NAMING_SOURCE_FOLDER)



    # Destination Folder setup
    if not os.path.exists(DEFAULT_DESTINATION_FOLDER):
        os.makedirs(DEFAULT_DESTINATION_FOLDER)
        print(f"Created dummy folder: {DEFAULT_DESTINATION_FOLDER}")
    # --- End dummy creation ---

    root = tk.Tk()
    app = TtfDuplicatorApp(root)
    root.mainloop()
