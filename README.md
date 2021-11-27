Simple-quiz-game

Description: A guess the capital city of a randomly selected country.

The list of countries can be found here:

[https://countriesnow.space/api/v0.1/countries/capital](https://countriesnow.space/api/v0.1/countries/capital)

## Installation

### Prerequisites

#### 1. Install Python

Install python-3.7.2 and python-pip. Follow the steps from the below reference document based on your Operating System. 

Reference: [https://docs.pythoguide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Setup virtual environment
```bash
# Install virtual environment
sudo pip install virtualenv

# Make a directory
mkdir envs

# Create virtual environment
virtualenv ./envs/

# Activate virtual environment
source envs/bin/activate
```

#### 3. Clone git repository
```bash
git clone "https://github.com/Zhencc/simple_quiz.git"
```

#### 4. Install requirements
```bash
cd simple_quiz/
pip install -r requirements.txt
```

#### 5. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
```
Open http://127.0.0.1:8000/ or http://localhost:8000 in the browser. Then you are good to go.

## Usage

Enter your answer into the text box and then the click check answer button to see if you got it right.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
