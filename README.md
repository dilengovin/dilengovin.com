# dilengovin.com
Personal portfolio website for Dilen Govin. Built using Flask and HTML/CSS while being hosted on Heroku

# Installation
Follow this to run the website locally on your machine, must have [python](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/) installed
1. Clone this repository
```bash
gh repo clone dilengovin/dilengovin.com
```
2. Start your own virtual environment (venv), optionally can be done with [VSCode](https://code.visualstudio.com/docs/python/tutorial-flask)
```bash
python -m venv venv
source venv/bin/activate
```
(For Windows)
```bash
python -m venv venv
YOUR_PROJECT_DIRECTORY/.venv/Scripts/Activate.ps1
```
3. Install all modules from requirements.txt, this will give Flask, Gunicorn, etc..
```bash
pip install -r requirements.txt
```
4. Run the app locally
```bash
python -m flask run
```
