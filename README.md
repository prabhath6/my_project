## Sample Module Repository For Python3

This simple project is an example repo for Python3 projects.

### Structure of the project

```
my_project
├── README.md
├── main.py
├── my_project
│   ├── __init__.py
│   ├── module_one.py
│   └── module_two.py
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_module_two.py
```

### Setting up

Clone the repo and then create a vitual environment. Install Packages using requirements.txt file.
```
# assuming virtualenv is activated and is of python3
pip install -r requirements.txt
```

### Running the code

Keep the business logic within *my_project/my_project/* and import required functions/classes into *main.py*. *main.py* is used to run the file.

```
python main.py
```

### Running tests

Tests are bult using nose. To run them use *nosetests*.

```
/my_project (master)ᐅ nosetests tests
```

**Note**: This is not for production.(work in progress)

