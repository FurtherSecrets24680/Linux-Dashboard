# Overview
A Simple Linux Dashboard made with Python using the CustomTkinter library.

![linuxdb1](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/dfdb38df-2efd-4e84-9824-a23e4cfa96c6)
Dark Mode

![linuxdb2](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/b106740d-0552-45ff-91f8-ae92d97517d5)
Light Mode

# Features
- A customizable quick launch area from where your favourite apps can be launched. (But at first, you have to customize quicklaunch.py).
- Greeting text on the top, with the current time.
- A customizable sidebar with some information about your PC. Such as OS, Storage and Internet info.
- A small area above the sidebar showing the ASCII logo of the current distro you are using.
- Light/Dark mode toggle.
- A "power menu" on the bottom right corner to shutdown, restart or log out.

# Requirements and Dependencies
- Python 3.7+
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
### Demonstration
[![video](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/735ef4fd-c29e-4905-a36b-69cf208f5b1f)](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/e7e430aa-2638-45e7-b754-2ffe12e7953b)

# FAQ
**Q**: Where can I get icons that will suit with this dashboard?

**A**: I recommend downloading white icons for any app. You can get those from these websites - https://simpleicons.org and https://icons8.com/icons

**Q**: There is no logo of my current distro on the top left corner!

**A**: You can add your own distro logo by modifying the asciilogos.py file. Or, wait for it to be added.

**Q**: It shows my IP and MAC address! Can I disable it?

**A**: The IP address that it shows (192.168.0.1 or 192.168.1.1) is your private IP address. If you put it in your address bar, you can access your router settings. You can only do it if you are connected to the internet of that router.This IP is the default for everyone, for every router. So there won't be any problems if you show it to anyone on the internet. And the MAC address is your machine's hardware address. If you accidentally leak it, a person will only be able to know your device manufacturer information. But if you share your mac address with anyone who is on the same network as you, they can do deAuth attacks or intercept your traffic by posing as the networks router. So, there won't be any major security risks if you show your mac address on the internet.

But if you are still skeptical about it, you can freely remove the IP or MAC address section from the code. Just follow these steps:

### 1. Open linux-dashboard.py in any text editor or IDE.
### 2. Go to the create_sidebar function of this code.
![image](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/5447a55e-7b10-450a-98cc-944aae24e68c)
### 3. Remove the IP/MAC address section like this:
![image](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/6181048e-5765-4553-be3f-30e7342ab057)

(While removing the MAC address, make sure to remove the comma after the IP address, otherwise, it'll throw an error.)
### 4. Now, go the update_system_info function.
![image](https://github.com/FurtherSecrets24680/Linux-Dashboard/assets/78081767/1f46ea13-3cac-4e98-b176-6e2c5740b2ac)

Then, remove this: 
```
self.label_mac_address.configure(text=f"MAC Address: {mac_address}")
```




# Credits
- ASCII distro logos from Neofetch.




