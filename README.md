# Overview
A Simple Linux Dashboard made with Python!

![linuxdb1](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/dfdb38df-2efd-4e84-9824-a23e4cfa96c6)
Dark Mode

![linuxdb2](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/b106740d-0552-45ff-91f8-ae92d97517d5)
Light Mode

# Requirements and Dependencies
1. Python 3.7+
   ### Modules
   - CustomTkinter
     
     ```
     pip3 install customtkinter
     ```
   - CpuInfo
     
     ```
     pip3 install py-cpuinfo
     ```
   - Psutil [Built-in]
   - Platform [Built-in]
   - OS [Built-in]
   - Subprocess [Built-in]
   - Distro [Built-in]
   - Datetime [Built-in]
   - PIL (Pillow) [Built-in]
   - Socket [Built-in]

# Installation and Launching (Any Distro or DE)

```
> git clone https://github.com/FurtherSecrets24680/Linux-Dashboard.git
> cd Linux-Dashboard
> python3 linux-dashboard.py
```
# On Hyprland WM
On Hyprland, if you launch the linux-dashboard.py file directly, then it will start maximized. Run the linux-dashboard.sh script to launch it as a floating and resizeable window.

```
> git clone https://github.com/FurtherSecrets24680/Linux-Dashboard.git
> cd Linux-Dashboard
> chmod +x linux-dashboard.sh
> ./linux-dashboard.sh
```

# Adding your own shortcuts to the Quick Launch Area
When you first launch the app, you will see only placeholders in the quick launch area.
To replace it with the shortcut of any app, follow these steps:

### 1. Open quicklaunch.py in any text editor or IDE.
![image](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/62af0f79-fa06-45f1-9048-4649245ee02d)

### 2. Go to the shortcuts function.
![image](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/ceed08c7-f9d9-42b1-856f-5b530bfa45cc)

Edit the "create_app_button" parts like these to add your own apps -
```
create_app_button{app_frame, "App Label", "Command/App to execute", "/path/to/app/icon.png", x, y, script_dir}
```
- Replace the "Placeholder" text with your app label.
- "true" is a dummy executable, used to test if the buttons are working. Replace with it other executable commands, like "code", "firefox", "thunar" etc.
- Replace "icons/placeholder.png" with your own icons. You can drop your the icons for your shortcut in the "icons" folder, then identify it in the code, or provide an absolute path for the icon.
- **x** is the row and **y** is the column. For example, for the first placeholder, the row is 0 and the column is also 0. That means the app shortcut button in the first column of the first row.

**Example**: VS Code
```
create_app_button{app_frame, "VS Code", "code", "code.png", x, y, script_dir}
```
### Demostration
![video](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/e8c78eb0-08e4-4380-9921-c824fcb04a44)

# Credits
- ASCII logos from Neofetch.




