# Face Detection and Face Recognition

Welcome to the Face Detection and Face Recognition project! This project provides you with the ability to detect faces in images or video streams and recognize faces using Python. Below, you'll find detailed instructions on how to set up the environment and run the scripts for face detection and facial recognition.

## Table of Contents
1. [Description](#description)
2. [Prerequisites](#prerequisites)
3. [Setting up the Environment](#setting-up-the-environment)
4. [Running the Scripts](#running-the-scripts)
5. [Usage](#usage)
6. [License](#license)

## Description

This project utilizes OpenCV and face recognition libraries in Python to accomplish face detection and facial recognition tasks. Whether you're interested in identifying faces in images or video streams, or you want to recognize specific faces, this project provides you with the tools to do so efficiently.

## Prerequisites

Before you can start using the face detection and recognition scripts, make sure you have the following prerequisites installed on your system:

1. **Python**: Python is the programming language used for this project. If you don't have Python installed on your system, you can download and install it from [here](https://www.python.org/downloads/).

2. **Visual Studio C++ Build Tools**: These tools are necessary for compiling certain dependencies required by the libraries used in this project. You can install Visual Studio C++ Build Tools from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

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
