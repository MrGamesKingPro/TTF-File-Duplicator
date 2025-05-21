
# Based on extracted files by 

[FModel](https://fmodel.app/)

# TTF File Duplicator

Simple tool to duplicate a single Font (`.ttf`) file multiple times, renaming each copy based on the filenames found in a specified "naming source" folder. This is useful, for example, when you want to use the same font file for various in-game fonts but need them to have specific filenames recognized by a game engine or tool.

![duplicate_file](https://github.com/user-attachments/assets/ac2ee23b-6772-4b2c-bfef-1e6eecc5d57c)

## Features

*   Select a single source `.ttf` file, or a folder containing the `.ttf` file to be duplicated.
*   Specify a "Naming Source Folder" – the filenames within this folder will be used to name the duplicated TTF files.
*   Choose a "Destination Folder" for the output.
*   Creates default folders (`TTF_Source`, `Original_Fonts_Game_Names`, `Output_Folder_Fonts`) in the script's directory on first run if they don't exist, for convenience.
*   Provides a log area to display the process and any errors.

## Prerequisites

*   **Python 3**: Version 3.6 or newer is recommended.
*   No external libraries are required; the script uses only Python's standard library.

## Folder Structure (Default)

The script will create these folders in the same directory where it's run, if they don't already exist:

*   `.\TTF_Source\`
    *   Place the **single** `.ttf` file you want to duplicate here.
    *   Alternatively, you can browse to any `.ttf` file on your system using the GUI. If this folder is used and contains multiple `.ttf` files, the script will pick the first one it finds.
*   `.\Original_Fonts_Game_Names\`
    *   Place files in this folder whose **filenames** (including their extensions) you want to use for the duplicated TTF files. The content of these files does not matter, only their names. For example, if you have `game_hud.ttf` and `menu_text.gfx` here, two copies of the source TTF will be made with these exact names.
*   `.\Output_Folder_Fonts\`
    *   This is where the duplicated and renamed TTF files will be saved.

You can override these default paths using the "Browse" buttons in the application.

## How to Use

1.  **Prepare your files:**
    *   Ensure the `.ttf` file you want to duplicate is accessible (either in the `TTF_Source` folder or elsewhere you can browse to).
    *   Populate the `Original_Fonts_Game_Names` folder (or another folder of your choice) with files whose names you want to use for the output. For example, if you want copies named `font1.ttf`, `font2.ttf`, and `special_font.ttf`, create empty files (or any files) with these names in the naming source folder.

2.  **Run the script:**
    *   Execute the script: `python TTF File Duplicator.py`

3.  **Use the GUI:**
    *   **TTF Source (File or Folder):**
        *   Enter the path to your source `.ttf` file directly, or the path to a folder containing your source `.ttf` file.
        *   Alternatively, click "Browse File..." to open a file dialog and select your `.ttf` file.
    *   **Naming Source Folder:**
        *   Enter the path to the folder containing files whose names will be used for the duplicates.
        *   Alternatively, click "Browse Folder..." to select it.
    *   **Destination Folder:**
        *   Enter the path where the duplicated and renamed `.ttf` files should be saved.
        *   Alternatively, click "Browse Folder..." to select it.
    *   **Run Duplication Process:** Click this button to start the process.
    *   **Log:** Observe the log area for progress, confirmation, and any error messages.

## Example Workflow

1.  You have a font file named `DIN.Next.LT.Arabic.ttf`.
2.  You place `DIN.Next.LT.Arabic.ttf` into the `.\TTF_Source\` folder (or you intend to browse directly to it).
3.  In the `.\Original_Fonts_Game_Names\` folder, you create three empty files:
    *   `Ubuntu-Bold.ufont`
    *   `Ubuntu-BoldItalic.ufont`
    *   `Ubuntu-Italic.ufont`
    *   `Ubuntu-Light.ufont`
    *   `Ubuntu-LightItalic.ufont`
    *   `Ubuntu-Medium.ufont`
    *   `Ubuntu-MediumItalic.ufont`
    *   `Ubuntu-Regular.ufont`
4.  You run the `TTF File Duplicator.py` script.
5.  In the GUI:
    *   "TTF Source": You set it to `.\TTF_Source` (or browse to `MyUniversalFont.ttf`).
    *   "Naming Source Folder": You set it to `.\Original_Fonts_Game_Names`.
    *   "Destination Folder": You set it to `.\Output_Folder_Fonts`.
6.  You click "Run Duplication Process".
7.  The `.\Output_Folder_Fonts\` will now contain:
    *   `Ubuntu-Bold.ufont`` (a copy of `DIN.Next.LT.Arabic.ttf`)
    *   `Ubuntu-BoldItalic.ufont`` (a copy of `DIN.Next.LT.Arabic.ttf`)
    *   `Ubuntu-Italic.ufont`` (a copy of `DIN.Next.LT.Arabic.ttf`)
    *   `Ubuntu-Light.ufont`` (a copy of `DIN.Next.LT.Arabic.ttf`)
    *   `Ubuntu-LightItalic.ufont`` (a copy of `DIN.Next.LT.Arabic.ttf`)
    *   `Ubuntu-Medium.ufont`` (a copy of `DIN.Next.LT.Arabic.ttf`)
    *   `Ubuntu-MediumItalic.ufont`` (a copy of `DIN.Next.LT.Arabic.ttf`)
    *   `Ubuntu-Regular.ufont`` (a copy of `DIN.Next.LT.Arabic.ttf`)

## Important Notes

*   The script copies the source TTF file and renames the copy. The original source TTF file is never modified.
*   If a file with the target name already exists in the destination folder, it will be **overwritten** without warning (other than what's in the log).
*   The script iterates through *files* in the "Naming Source Folder". Subdirectories within the naming source folder are ignored.
*   The new filename in the destination folder will be *exactly* the same as the filename from the "Naming Source Folder", including its extension. If a file in the naming source is `example.ufont`, the duplicated TTF will be named `example.ufont` in the destination folder (though its content will be that of a TTF font).

---
By MrGamesKingPro
```
