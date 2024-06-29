# FileFusion

## Overview
FileFusion is a tool designed to help you combine the text content from multiple files into a single file. It provides a user-friendly interface and allows you to easily select files, view the selected files, and generate a combined output file with organized headings.

## Features
- **File Selection**: Select multiple files to combine their content.
- **Visual Display**: View the list of selected files in the application.
- **Organized Output**: The combined file includes headings for each file, indicating the source of the text.

## How to Use

### 1. Open the Application:
   - Launch the FileFusion application.

### 2. Select Files:
   - Click the "Select Files" button to open a file dialog.
   - Choose the files you want to combine and click "Open".
   - The selected files will be displayed in the text area.

### 3. Combine Files:
   - Click the "Run" button to combine the text from the selected files.
   - The combined content will be saved to a file named `all_text_combined.txt` in the same directory as the application.

### 4. View Output:
   - The output file `all_text_combined.txt` will contain the text from each selected file with headings indicating the file names.

## Future Improvements
I'm planning to make improvements and add more features, such as additional customization options and enhanced file handling capabilities.

## Installation

### Prerequisites
- Python 3.x
- Tkinter

### Running the Tool
1. **Clone the repository**:
   ```sh
   git clone https://github.com/Sprackles/File-Fusion.git
2. **Navigate to the project directory**:
   ```sh
   cd FileFusion
3. **Run the script**:
   ```sh
   python file-fusion.py

### Compiling to an Executable
   To compile the script into a single executable file using Pyinstaller:
1. **Install pyinstaller**:
   ```sh
   pip install pyinstaller
2. **Compile the script**:
   ```sh
   pyinstaller --onefile --noconsole file-fusion.py
