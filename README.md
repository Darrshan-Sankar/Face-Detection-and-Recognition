# Face Detection and Face Recognition

Welcome to the Face Detection and Face Recognition project! This project provides you with the ability to detect faces in images or video streams and recognize faces using Python. Below, you'll find detailed instructions on how to set up the environment, run the scripts for face detection and facial recognition, and also how to set up the database folder.

## Table of Contents
1. [Description](#description)
2. [Prerequisites](#prerequisites)
3. [Setting up the Environment](#setting-up-the-environment)
4. [Setting up the Database Folder](#setting-up-the-database-folder)
5. [Running the Scripts](#running-the-scripts)
6. [Usage](#usage)
7. [License](#license)

## Description

This project utilizes OpenCV and face recognition libraries in Python to accomplish face detection and facial recognition tasks. Whether you're interested in identifying faces in images or video streams, or you want to recognize specific faces, this project provides you with the tools to do so efficiently.

## Prerequisites

Before you can start using the face detection and recognition scripts, make sure you have the following prerequisites installed on your system:

1. **Python**: Python is the programming language used for this project. If you don't have Python installed on your system, you can download and install it from [here](https://www.python.org/downloads/).

2. **Visual Studio C++ Build Tools**: These tools are necessary for compiling certain dependencies required by the libraries used in this project. Follow the steps below to download and install Visual Studio along with the required workload for "Desktop Development with C++":

    - **Step 1: Download Visual Studio**
        - Navigate to [Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/) website.
        - Click on the "Download Visual Studio" button.
        - Follow the on-screen instructions to download the Visual Studio installer.
        - Once the installer is downloaded, run it.

    - **Step 2: Download and install the workload: "Desktop Development with C++"**
        - Open the Visual Studio Installer.
        - Select "Visual Studio C++ Build Tools" from the list of available products.
        - Click on "Install" to download and install the workload.
        - Follow the on-screen instructions to complete the installation.

    - **Step 3: Customize Installation (Optional)**
        - If you want to customize the installation or select additional components, you can do so by clicking on the "Individual components" tab.
        - Here, you can browse and select additional components based on your requirements.

    - **Step 4: Install**
        - After selecting the desired workload and components, click on the "Install" button to begin the installation process.
        - Follow the on-screen instructions to complete the installation.

3. **CMake**: CMake is a cross-platform build system that is used to control the software compilation process. Download and install CMake from [here](https://cmake.org/download/).

## Setting up the Environment

To ensure a smooth running of the scripts, it's recommended to set up a Python virtual environment. Follow these steps to create the environment:

1. **Create a Python Environment**:
    - Open your terminal or command prompt and navigate to your project directory.
    - Run the following command to create a virtual environment named `myenv`:
        ```bash
        python -m venv myenv
        ```

2. **Activate the Environment**:
    - Depending on your operating system, use the appropriate command to activate the virtual environment:
        - On Windows:
            ```bash
            myenv\Scripts\activate
            ```
        - On macOS/Linux:
            ```bash
            source myenv/bin/activate
            ```

3. **Install Necessary Packages**:
    - Once the virtual environment is activated, install the required packages using pip:
        ```bash
        pip install opencv-python
        pip install face-recognition
        ```

## Setting up the Database Folder

To set up the database folder for storing person's photos, so that this can be loaded and used by our face_rec.py script, follow these steps:

1. **Create a Folder**:
    - Create a folder named `persons_data` in your project directory. This folder will store the photos of the persons for facial recognition.

2. **Add Person's Photos**:
    - Inside the `persons_data` folder, add the photos of the persons you want to recognize. 
    - Name each photo file with the person's name. For example, if you have a photo of John Doe, name the file `John_Doe.jpg`.

## Running the Scripts

Now that you've set up your environment and installed the necessary packages, you can run the face detection and facial recognition scripts.

1. **Face Detection**:
    - Run the script `face_detection.py` to detect faces in images or video streams:
        ```bash
        python face_detection.py
        ```

2. **Facial Recognition**:
    - Execute the script `face_rec.py` to recognize faces in images or video streams:
        ```bash
        python face_rec.py
        ```

## Usage

- `face_detection.py`: Use this script to detect faces in images or video streams.
- `face_rec.py`: Utilize this script to recognize faces in images or video streams.

## License

This project is licensed under the MIT License. You can find more details in the [LICENSE](LICENSE) file included in the repository.

That's it! You're now ready to detect and recognize faces using the provided scripts. If you have any questions or encounter any issues, feel free to reach out to the project maintainers. Happy face detecting and recognizing!
