# Description

I automated the entire Microsoft Rewards system.

*Note: Check **requirements.ipynb** for requirements, setup and working. Head to **problem.txt** file to understand the flow.*

## Setup the **main.py** file: -
* Install the requirements from the **requirements.ipynb** file.
* Clone the repository using this command:
` $ git clone git@github.com:heylightning/mr-script.git `
* Set your default webbrowser to Microsoft Edge.
* Your IDs should be in this format: ` <first-name>.<second-name>@outlook.com `
* Run the **main.py** file using this command:
` $ python main.py `

## Features
* **idConfiguration.py** file is a script designed to facilitate the automation process of making Microsoft IDs from the *data.py* or any other file containing the IDs and their passwords. In my case, I have used *data.py* that I have mentioned in the *.gitignore* file. 
* **lockConfiguration.py** file is a script developed to automate the checking process of Microsoft IDs for lock status. It provides a convenient and efficient way to determine whether a given ID is currently locked or not. This can be especially valuable in scenarios where a large number of IDs need to be monitored for potential lockouts.

## Flow of files: -
1. First, run the **idConfiguration.py** file to create the IDs with respect to the data file.
2. Second, run the **lockConfiguration.py** file to check the lock status of the ID.
3. Lastly, run the **main.py** file to grind the points. (*You can alter the number of points to grind in the source file locally in your environment.*)
4. Again, for proper and controlled flow, execute the **lockConfiguration.py** first to check the status of the ID and then execute the **main.py** file.

### LICENSE

MIT License

Copyright (c) 2023 Pratham Mishra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
