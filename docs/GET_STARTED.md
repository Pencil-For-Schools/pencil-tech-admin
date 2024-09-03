# Project Directions

## Running the app

**To run locally**:

- Make a copy of the `.env.sample` in the root directory and name it `.env`
- Get the private keys from another engineer if you cannot access [MAKE A LINK]()

Install pipenv if you do not currently have it. This will allow you to install the version of python this project is using.

### Using Pyenv to manage python versioning

You will want to have the correct Python version on your machine.

First, check your python version:
- ```shell
  python --version
  ```
Install Pyenv if not installed
- ```shell
  brew install pyenv
  ```
If using bash:
- ```shell
  echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile
  echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile
  ```
If using Zsh:
- ```shell
  echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc
  echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
  ```
Remember to restart your terminal or run `source ~/.bash_profile` or `source ~/.zshrc` to apply the changes.

Once pyenv is installed, you can install different Python versions using it. For example, to install Python 3.9.13, you can run:
```shell
pyenv install 3.9.13
```
To check for all available Python versions:
```shell
pyenv versions
```

## Install Dependencies

```shell
pipenv shell
```

```shell
pipenv install
```

- Create a secret key for the .env

```shell
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Run migration

This will create a local db

```shell
python3 manage.py migrate
```

## Create 2 local super users

```shell
python3 manage.py createsuperuser --email admin1@gmail.com --username admin1
python3 manage.py createsuperuser --email admin2@gmail.com --username admin2
```
enter your password for the NEW SUPER USER twice

## Load Fixtures
```shell
python3 manage.py loaddata admin_settings creator_types video_types creators medium_settings shows socials videos spotlights merch creator_tags video_tags show_tags
```

## Start the server

```shell
python3 manage.py runserver
```

## Login to the admin

To login navigate to: <http://127.0.0.1:8000/admin>

## If there are any code updates

```shell
python3 manage.py migrate
```

## If you get errors
- make sure that you are in the shell environment
