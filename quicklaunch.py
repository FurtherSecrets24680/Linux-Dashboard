# Here, you can add your own shortcuts for your desired apps.

# Import Modules
import customtkinter as ctk
from PIL import Image
import subprocess
import os

def create_app_button(parent, app_name, command, icon_path, row, column, script_dir):
    def open_app():
        subprocess.Popen(command)

    # Use absolute path for the icon
    full_icon_path = os.path.join(script_dir, icon_path)

    # Load and resize the icon
    icon = ctk.CTkImage(Image.open(full_icon_path), size=(60, 60))

    button = ctk.CTkButton(parent, text=app_name, image=icon, compound="top", command=open_app,
                           width=100, height=100, corner_radius=10)
    button.grid(row=row, column=column, padx=10, pady=10)

# Edit the "create_app_button" parts like these to add your own apps -
# create_app_button{app_frame, "App Label", "Command/App to execute", "/path/to/app/icon.png", x, y, script_dir}
# "true" is a dummy executable, used to test if the buttons are working. Replace with it other executable commands.
# You can drop your own icons for your shortcut in the "icons" folder, then identify it in the code, or provide an absolute path for the icon.
# x is the row and y is the column. Keep script_dir untouched.

def shortcuts(app_frame, script_dir):
    #                             "App Label"  "Command"        "icon.png"       x  y
    create_app_button(app_frame, "Placeholder", "true", "icons/placeholder.png", 0, 0, script_dir)
    create_app_button(app_frame, "Placeholder", "true", "icons/placeholder.png", 0, 1, script_dir)
    create_app_button(app_frame, "Placeholder", "true", "icons/placeholder.png", 0, 2, script_dir)
    create_app_button(app_frame, "Placeholder", "true", "icons/placeholder.png", 0, 3, script_dir)
    create_app_button(app_frame, "Placeholder", "true", "icons/placeholder.png", 0, 4, script_dir)
