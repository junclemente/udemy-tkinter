# Python GUI Programming Using Tkinter

This repository contains the desktop applications I am developing using Tkinter and Python3. There are five fully functioning desktop apps that I will be creating following the course listed below. 

Since this repository is for learning about Tkinter, the applications may not have been tested for errors and/or edge cases. This may be corrected in the future to develop a more robust program, but as of right now, assume that the program may break if the instructions aren't followed. 

Another part of this course is converting a Tkinter/Python app into a standalone desktop application. See below for more information about converting one of the apps into a standalone desktop application. 

### Course 
[Master Tkinter By Building 5 Fully Functioning Apps](https://www.udemy.com/master-tkinter-by-building-5-apps/) on [Udemy.com](https://www.udemy.com).
 
#### Technology
* Python v3.7
* Tkinter
* py2app v0.13

## Desktop Applications Projects
### Simple Food Price Calculator

_Description_: This app calculates the cost of the food selected using a radio button. 

_How To Use_: 

1. Download the `food_price.py` file and run the app by typing: 

	```
	$:python3 food_price.py
	``` 

	or whatever method you use to run a Python3 	file. 

2. Select a food item by clicking the adjacent radio button. 
3. Type an integer into the box next to "Cal".
4. Click the "Cal" button.
5. Magic! The box labeled "Price" will show the value of the 'cost' of the food item multiplied by the number entered in "Cal". 

### File Counter
_Description_: This application counts the number of specific words in a text file.

_How To Use_: 

1. Download the file `file_counter.py` and run the app by typing:

	```
	$:python3 file_counter.py
	```
or whatever method you use to run a Python3 file. 

2. Enter ', ' comma seperated words into the top text box. 
3. Select the `.txt` file that will be analyzed by clicking the `Select file` button.
4. Click `Count Words` button. 
5. After some magic, a count of how many times each word entered is found in the uploaded text is displayed in the lower text box.
6. Use `Clear Text` button to clear all text in the application. 


### Python IDE
_Description_: This is a simple IDE that takes an Python script entered in the text box, executes it, and returns the result in an alert message box. 

_How To Use_:

1. Download the file `python_ide.py` and run the app by typing: 

	```
	$:python3 python_ide.py
	```
2. Enter Python code in the text box. 
3. Click the `run` button to execute the script. The results of the program will be shown in a pop-up "Warning" window. 
4. Click `clear` to clear the text box. 

### Simple Calculator
_Description_: In this app, enter two numbers then click a button that corresponds to add, subtract, multiply, or divide. The result will then be printed in the 'Results' box. 

_How To Use_: 

1. Download the file `calculator.py` and run the app by typing:

	```
	$:python3 calculator.py
	```
2. Enter a number in the boxes for 'Input Number 1:' and 'Input Number 2:'.
3. Click a button corresponding to `+`, `-`, `*`, or `/` to perform a mathematical calculation. 
4. Magic! The result will show next to the 'Result:' box. 

### Email Sender
_Description_: This is a simple email app. Enter the 'from' email address and the 'to' email address. Type a message. Then click 'Send'. 

_How To Use_:

1. Download the file `emailer.py` and run the app by typing:

	```
	$:python3 emailer.py
	```

2. Enter the 'from' email address in the box provided. Do the same for the 'to' email address (or addresses, seperated by a comma. 
3. To clear the 'from', 'to', or both entry boxes, click on the appropriate button on the right side. 
4. This is an actual, working email sending app. Currently, it is set up to send email from gmail. To be able to send email from a gmail account, you must enter your email address next to `USERNAME`.
5. For the `PASSWORD`, you cannot just use your own password. You must [follow these instructions](https://support.google.com/mail/?p=InvalidSecondFactor) to host an email session.
6. Once you've entered the required information, including a message, click `send` to send the message. 


## Converting 'Simple Calculator' to a standalone MacOS application

In this course, the instructor also shows us how to use the `py2app` Python library to convert a Tkinter/Python application into a standalone desktop application. 

I ran into a bit of a problem when following the tutorial because the instructor was using `Python v3.6` and `py2app v0.13`. I was using `Python 3.7` and due to some changes between Python v3.6 and v3.7, py2app v0.13 doesn't work out-of-the-box with v3.7. A few changes had to be made to py2app to make it work with the version of Python I was using. Thankfully, someone else on [stackoverflow.com](https://www.stackoverflow.com) had the same problem and others were able to provide a solution. The solution to making py2app v0.13 work with Python 3.7: [An import error when using Py2app](https://stackoverflow.com/questions/51471259/an-import-error-when-using-py2app).

The 'Simple Calculator' app was converted using py2app to a standalone MacOS desktop application. To try it out, download `Cal.app` in the `/dist` folder. Double-click it to open. 