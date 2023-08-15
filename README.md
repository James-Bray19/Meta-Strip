# MetaStrip - Image Metadata Removal Tool

MetaStrip is a simple Python application built using the Tkinter library that allows users to remove metadata from image files and manage the processed images. Metadata, such as EXIF information, can contain sensitive information that users might want to remove before sharing images.

## Features

- **Drag-and-Drop**: Users can drag and drop image files onto the application's window to have their metadata removed.
- **Browse Files**: Alternatively, users can use the "Browse Files" button to select an image file from their computer.
- **Metadata Removal**: The application removes metadata from the dropped or selected image and creates a copy with no metadata.
- **Image History**: The original and stripped images are saved in separate folders ("originals" and "stripped") for users to reference later.
- **Output Display**: The application provides a text display area to show information about the metadata removal process and any errors that may occur.

## Instructions

1. Drag and drop an image file onto the designated area in the application window.
2. Alternatively, click the "Browse Files" button to open a file dialog and select an image.
3. The application will create a copy of the image with the metadata removed and store it in the "stripped" folder.
4. The original image is saved in the "originals" folder for reference.
5. Use the "See Originals" and "See Stripped" buttons to open the respective folders in the default file explorer.
6. To clear the image history, click the "Clear Image History" button.

## Dependencies

- Tkinter: A standard Python library for creating graphical user interfaces.
- tkinterdnd2: A library for adding drag-and-drop functionality to Tkinter applications.
- Pillow (PIL): A library for opening, manipulating, and saving image files.
- os: A standard Python library for interacting with the operating system.
- filedialog: A module from the Tkinter library for creating file dialog windows.

## Usage

1. Make sure you have Python installed on your system.
2. Install the required dependencies using the following command:
   ```
   pip install Pillow tkinterdnd2
   ```
3. Run the `meta_strip.py` script to start the application.
4. Follow the instructions provided in the application's GUI to remove metadata from image files.
