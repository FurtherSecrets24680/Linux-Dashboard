# A Simple Linux Dashboard made with Python.
# Edit quicklaunchapps.py to add more app shortcuts.
# Edit asciilogo.py to add more ascii logos.

# Import Modules
import customtkinter as ctk
import psutil
import platform
import os
from datetime import datetime
import subprocess
from PIL import Image
import distro
import socket
import cpuinfo
from quicklaunch import shortcuts
from asciilogos import get_logo

# Set up the dashboard window
class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Get the directory of the dashboard
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        self.title("Linux Dashboard")

        # Window Size
        window_width = 1020
        window_height = 875
        self.geometry(f"{window_width}x{window_height}")
        
        # Allow window resizing
        self.resizable(True, True)

        # Set minimum window size
        self.minsize(800, 500)

        # Default Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar frame with border
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0, border_width=1, border_color="gray30")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(14, weight=1)

        # Main area frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        self.create_greeting()
        self.create_sidebar()
        self.create_main_area()
        self.create_power_options()

        self.after(1000, self.update_system_info)

    # Set greeting text
    def create_greeting(self):
        current_time = datetime.now()
        hour = current_time.hour
        greetings = {
            (5, 12): "Good Morning",
            (12, 18): "Good Afternoon",
            (18, 22): "Good Evening",
            (22, 5): "Good Night"
        }
        greeting = next((v for k, v in greetings.items() if k[0] <= hour < k[1]), "Hello")
    
        # Display current time (12H)
        self.time_label = ctk.CTkLabel(self.main_frame, text=current_time.strftime("%I:%M %p"), font=("Noto Sans", 40))
        self.time_label.grid(row=0, column=0, pady=(20, 0), sticky="n")

        # Display the greeting
        self.greeting_label = ctk.CTkLabel(self.main_frame, text=f"{greeting}, User!", font=("Noto Sans", 50 , "bold"))
        self.greeting_label.grid(row=1, column=0, pady=(5, 20), sticky="n")

    # Set up the sidebar
    def create_sidebar(self):
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        
        # Add ASCII art section
        self.create_ascii_art()

        sections = [                    # Remove any section/information you don't want it to show.
            ("Device Information", [
                ("CPU:", "cpu"),
                ("CPU Usage:", "cpu_usage"),
                ("RAM:", "ram"),
                ("RAM Usage:", "ram_usage")
            ]),
            ("Storage Information", [
                ("Disk:", "disk"),
                ("Disk Usage:", "disk_usage"),
                ("Free Space:", "free_space")
            ]),
            ("Internet Information", [
                ("IP Address:", "ip_address"),
                ("MAC Address:", "mac_address")
            ]),
            ("OS Information", [
                ("OS:", "os"),
                ("Kernel:", "kernel"),
                ("Uptime:", "uptime")
            ])
        ]

        for i, (title, items) in enumerate(sections, start=1):
            frame = ctk.CTkFrame(self.sidebar_frame, corner_radius=10, border_width=1, border_color="gray30")
            frame.grid(row=i, column=0, padx=10, pady=10, sticky="ew")
            
            ctk.CTkLabel(frame, text=title, font=("Noto Sans", 20, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky="w")
            
            for j, (text, attr) in enumerate(items, start=1):
                label = ctk.CTkLabel(frame, text=text)
                label.grid(row=j, column=0, padx=10, pady=2, sticky="w")
                setattr(self, f"label_{attr}", label)

        # Toggle button for light/dark mode
        self.mode_toggle = ctk.CTkSwitch(self.sidebar_frame, text="Light/Dark Mode", command=self.toggle_mode)
        self.mode_toggle.grid(row=len(sections) + 1, column=0, padx=10, pady=10, sticky="ew")

    # Set up the distro ASCII art on the top left corner
    def create_ascii_art(self):
        distro_id = distro.id()
        
        # Get the ASCII logo for the current distribution using the imported "asciilogos" module
        logo = get_logo(distro_id)
        
        ascii_frame = ctk.CTkFrame(self.sidebar_frame, corner_radius=10, border_width=1, border_color="gray30")
        ascii_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        ascii_label = ctk.CTkLabel(ascii_frame, text=logo, font=("Courier", 8), justify="left")
        ascii_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    def create_main_area(self):
        center_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        center_frame.grid(row=2, column=0, sticky="nsew")
        center_frame.grid_rowconfigure(0, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)

        # Bordered area for Quick Launch
        quick_launch_frame = ctk.CTkFrame(center_frame, corner_radius=10, border_width=2, border_color="gray30")
        quick_launch_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        quick_launch_frame.grid_rowconfigure(0, weight=1)
        quick_launch_frame.grid_columnconfigure(0, weight=1)

        apps_label = ctk.CTkLabel(quick_launch_frame, text="Quick Launch", font=("Noto Sans", 20, "bold"))
        apps_label.grid(row=0, column=0, pady=(10, 10), sticky="n")

        app_frame = ctk.CTkFrame(quick_launch_frame, fg_color="transparent")
        app_frame.grid(row=1, column=0, pady=(10, 10), sticky="n")

        # Use the imported "quicklaunchapps" module to add app buttons
        shortcuts(app_frame, self.script_dir)

    # Set up the Power Menu
    def create_power_options(self):
        self.power_button = ctk.CTkButton(self.main_frame, text="⏻", width=30, height=30, 
                                  command=self.toggle_power_menu)
        self.power_button.grid(row=3, column=0, padx=(0, 20), pady=(0, 20), sticky="se")
        self.power_menu = None

    def toggle_power_menu(self):
        if self.power_menu and self.power_menu.winfo_exists():
            self.power_menu.destroy()
            self.power_menu = None
        else:
            self.power_menu = ctk.CTkFrame(self.main_frame, corner_radius=5, fg_color="#333333")
            self.power_menu.grid(row=3, column=0, sticky="se", padx=(0, 20), pady=(0, 80))

            ctk.CTkButton(self.power_menu, text="Shutdown", command=lambda: subprocess.run(["shutdown", "now"])).pack(fill="x", padx=10, pady=5)
            ctk.CTkButton(self.power_menu, text="Restart", command=lambda: subprocess.run(["reboot"])).pack(fill="x", padx=10, pady=5)
            ctk.CTkButton(self.power_menu, text="Log Out", command=self.logout).pack(fill="x", padx=10, pady=5)

            self.power_menu.bind("<FocusOut>", self.close_power_menu)
            self.after(100, lambda: self.power_menu.focus_set())  # Set focus after a short delay

    def close_power_menu(self, event):
        if not event.widget.focus_get() or not event.widget.focus_get().winfo_parent() == str(self.power_menu):
            if self.power_menu and self.power_menu.winfo_exists():
                self.power_menu.destroy()
                self.power_menu = None

    def logout(self):
        subprocess.run(["pkill", "-u", subprocess.getoutput("whoami")])

    def toggle_mode(self):
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("Light")
        else:
            ctk.set_appearance_mode("Dark")

    def update_system_info(self):
        current_time = datetime.now()
        cpu_info = cpuinfo.get_cpu_info()['brand_raw']
        cpu_usage = psutil.cpu_percent()
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
        network = psutil.net_if_addrs()
    
        ip_address = next((info.address for info in network.get('wlan0', []) if info.family == socket.AF_INET), "N/A")
        mac_address = next((info.address for info in network.get('wlan0', []) if info.family == psutil.AF_LINK), "N/A")
        dist_name = distro.name(pretty=True)
    
        self.label_cpu.configure(text=f"CPU: {cpu_info}")
        self.label_cpu_usage.configure(text=f"CPU Usage: {cpu_usage}%")
        self.label_ram.configure(text=f"RAM: {ram.total / (1024**3):.2f} GB")
        self.label_ram_usage.configure(text=f"RAM Usage: {ram.percent}%")
        self.label_disk.configure(text=f"Disk: {disk.total / (1024**3):.2f} GB")
        self.label_disk_usage.configure(text=f"Disk Usage: {disk.percent}%")
        self.label_free_space.configure(text=f"Free Space: {disk.free / (1024**3):.2f} GB")
        self.label_ip_address.configure(text=f"IP Address: {ip_address}")
        self.label_mac_address.configure(text=f"MAC Address: {mac_address}")
        self.label_os.configure(text=f"OS: {dist_name}")
        self.label_kernel.configure(text=f"Kernel: {platform.release()}")
        self.label_uptime.configure(text=f"Uptime: {str(uptime).split('.')[0]}")
        self.time_label.configure(text=current_time.strftime("%I:%M %p"))

        self.after(1000, self.update_system_info)

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()