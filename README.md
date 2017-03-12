# Music History API

## Description

This is a REST API designed to be used as a collection of music

## Installation

1. Install Python 3.6.0. See instructions for installation and download here: https://www.python.org/downloads/
2.Create a virtual environment by following the instructions in the How to Run section.
3. Import all required dependencies located in `requirements.txt`.
4. Go into the project's root directory and follow the instructions in the "How to Run" section below.

## Requirements.txt
```
Django==1.10.5
djangorestframework==3.5.3
```

## How to Run

## MAC

Create a virtual environment
```
python -m venv venv
```

Activate the virtual environment
```
source venv/bin/activate
```

Install all dependencies in requirements.text
```
pip install -r requirements.txt
```

To deactivate the virtual environment
```
deactivate
```

## Windows

Install virtual environment and wrapper

```
pip install virtualenvwrapper-win
```

Create a virtual environment
```
mkvirtualenv myproject
```

Activate the virtual environment
```
workon myproject
```

Install all dependencies in requirements.txt
```
pip install -r requirements.txt
```

To deactivate the virtual environment
```
deactivate
```

## How to Run Cont. (After Creating Virtual Environment)
Go into the projects secondary directory
```
cd music_history/
```

Run the migrations script to create the database