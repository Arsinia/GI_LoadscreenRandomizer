# GI Loading Screen Randomizer

# What does it do?
This tool lets you take any images and prep them to be used as loading screens in a certain game. It also sets up the .ini file to be able to load these loading screens in game. This mod also replaces the annoying white flash when the game opens.

This is what it looks like in game by default
![alt text](https://github.com/Arsinia/GI_LoadscreenRandomizer/blob/main/README_Pictures/Example.png?raw=true)

# How do I use it?
#### Basic instructions
Just put the pictures you want to see in a folder called "InputLoadingScreens" and run GI_LoadingScreen.exe or GI_LoadingScreen.py. Then just run the game and it'll work. If you change the images while the game is running, press F10 to reload.

#### Toggling Subfolders
You can have multiple folders inside of "InputLoadingScreens" and running the program will search through all images in these folders. If you want to disable a folder, rename it to start with a hyphen "-" and rerun the program. This will prevent any images in this folder from being used as a loading screen.

#### Options
You can configure the resolution of the pictures by editing config.txt. Set the first two numbers to the width and height of your monitor and it'll resize the outputs automatically for you. When you change the resolution, you will need to delete all files in "OutputLoadingScreens" to force it to use the new size.

You can toggle showing the loading UI in the LSMod.ini file. Open it in a text editor and set the first 3 options to whatever you want (0 to show, 1 to skip). 

#### Required Files
Most mods you download will have all of the files needed present. Also if you download from the releases, all of the files will be present. If you want to make sure, you need [texconv.exe](https://github.com/Microsoft/DirectXTex/wiki/Texconv), the LSMod.ini file, and config.txt in the same folder as the main executable.

#### I don't want to run it as an EXE
EXE files can be a huge security risk if you don't trust where they came from. If you want to use this without an EXE, you can just run the Python file instead. Mods using this should provide the Python file for anyone who doesn't want to use EXEs. To run the Python file, you will need to install Python and the package Pillow. Then you should be able to run it just like the EXE. You can also build the EXE yourself using Pyinstaller and running the build.bat file.

# Other stuff
Feel free to use this project for whatever you want, just make sure you credit DiXiao for figuring out how to make loading screen mods. 90% of the Python code was just forcing ChatGPT to code it for me.

## Special Thanks
[DiXiao](https://gamebanana.com/members/2182818) for figuring out how to make loading screen mods

The [Anime Game Modding Group Discord](https://discord.gg/gR2Ts6ApP7) for helping me mod a certain game
