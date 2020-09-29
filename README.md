#Project 7: Granpy Bot documentation

##Description
This repository contains the code for the GranpyBot web application.

GranPy bot is a flask application that allows you to ask questions about a place in a chat with a 
"bot" that will use google and wikipedia API to answer them. 

##Installation

- To install the application clone this repository:
```bash
git clone https://github.com/adrien914/P7_Adrien_Simon.git
```
    
- Install virtualenv if it's not already:
```bash
pip3 install virtualenv
```

- Create a virtual environment:
```bash
virtualenv venv
```

- Activate this environment:
```bash
source venv/bin/activate
```

- Install the requirements:
```bash
pip3 install -r requirements.txt
```

- Create a .env file and add your google maps api key in it:
```bash
echo API_KEY=************** > .env
```
- Start the program:
```bash
python3 app.py
```