# Selfie Cam

This is a simple Selfie App written in Python using the Tkinter GUI library and OpenCV for camera access. The app allows users to capture selfies using their computer's camera and stores them along with user information in an Excel file.

## Project Details
### pythonProject10
The **'pythonProject10'** directory contains code specifically tailored for mobile phone applications. Developers seeking to integrate the selfie camera feature into their mobile apps can utilize this project as a reference. The codebase is optimized for mobile environments, ensuring efficient usage of resources and compatibility with varying screen sizes and device specifications.

### pythonProject9
For developers aiming to implement the selfie camera feature across both mobile phones and laptops, the **'pythonProject9'** directory provides suitable code. This project is designed to be versatile, enabling the same functionality to be seamlessly integrated into applications on multiple devices. By utilizing this codebase, developers can ensure consistent user experiences across different platforms.

## Features

* Capture selfies using your camera.
* Login functionality to access the selfie capture feature.
* User authentication with username and password.
* Selfies are saved with a filename containing the username and timestamp.
* Selfie data is stored in an Excel file for later reference.

## Prerequisite

* Python **'3.x'**
* OpenCV (**'cv2'**)
* Tkinter (**'tkinter'**)
* Pillow (**'PIL'**)
* Pandas (**'pandas'**)

## Installation

* Clone or download the repository to your local machine.
* Install the required Python packages if you haven't already.
* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install opencv-python-headless
pip install tkinter 
pip install pillow 
pip install pandas
```


## Usage

1. Choose the appropriate project directory based on your development needs:
  * If your focus is solely on mobile phone applications, navigate to the **'pythonProject10'** directory.
  * If you intend to develop applications for both mobile phones and laptops, refer to the **'pythonProject9'** directory.
2. Open the project folder in your favorite Python IDE (e.g., PyCharm).
3. Run the selfie_app.py script.
4. The app's main window will open. You'll need to log in with a predefined username and password to access the selfie capture functionality. By default, the username is "user" and the password is "password". You can customize the authentication logic in the login() method of the SelfieApp class.
5. Once logged in, you can capture a selfie by clicking the "Capture Selfie" button. The selfie will be saved in the app's directory with a filename containing your username and timestamp.
6. The selfie data, including username, selfie filename, and timestamp, will be stored in an Excel file named "selfies.xlsx" in the app's directory.

6. To quit the app, click the "Quit" button.

**Note:**

* This app is intended for educational purposes and demonstrates a basic implementation of a selfie capture and storage application.
* The authentication logic is minimal and should be replaced with more secure methods in a production environment.
* Make sure to adjust the camera settings and image dimensions to suit your preferences.
* Please make sure to update tests as appropriate.

## Contribution

Contributions to this repository are welcome. If you identify issues, improvements, or additional features that could enhance the selfie camera access codes, feel free to submit pull requests. Please ensure that any contributions adhere to the established coding standards and documentation guidelines.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License
