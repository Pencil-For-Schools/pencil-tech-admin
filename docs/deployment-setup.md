# Heroku Setup

1. Set up a `Procfile` file with this. (the text "app" needs to be updated to be the name of your django app, where the `wsgi.py` file lives)

    ```Procfile
    web: gunicorn app.wsgi
    ```

1. Set up `runtime.txt` with version of Python you plan to use.

    ```txt
    python-3.9.13
    ```

1. Install a package to handle `.env` files (We're going to be using [django-environ](https://pypi.org/project/django-environ/))

    - Install the package: `pipenv install django-environ`
    - Create an `.env` file at the root of the directory
    - Update the `settings.py` file to be able to read from the `.env` file. Add this to the top of the file:

        ```python
        import os
        from environ import Env

        # NOTE: This line of code is already inthe settings.py file
        BASE_DIR = Path(__file__).resolve().parent.parent

        env = Env()
        env.read_env(os.path.join(BASE_DIR, ".env"))
        ```

1. Update the `settings.py` file to use env variables for the following variables:
    - `SECRET_KEY`

        ```python
        SECRET_KEY = env("SECRET_KEY")
        ```

    - `DEBUG`

        ```python
        DEBUG = env.bool("DEBUG")
        ```

    - `ALLOWED_HOSTS`

        ```python
        ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
        ```

    - `CORS_ORIGIN_WHITELIST`

        ```python
        # You might have to add this entire variable if you're starting from scratch
        CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST")
        ```

1. Set up `.env` files with new info

    ```env
    SECRET_KEY=''
    DEBUG=true
    ALLOWED_HOSTS='localhost,127.0.0.1'
    CORS_ORIGIN_WHITELIST='http://localhost:3000,http://127.0.0.1:3000'
    ```

    - You can use this command to create a secret key (make sure you're in your virtual environment or this won't work)

        ```terminal
        python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
        ```

1. In order to work with Heroku's infrastructure, we're going to install a few packages to handle things that our computer does locally.

    ```terminal
    pipenv install dj-database-url psycopg2-binary gunicorn whitenoise
    ```

    - Here are links to each package for if you want to look further into them:
        - [`dj-database-url`](https://pypi.org/project/dj-database-url/)
        - [`psycopg2-binary`](https://pypi.org/project/psycopg2-binary/)
        - [`gunicorn`](https://pypi.org/project/gunicorn/)
        - [`whitenoise`](https://pypi.org/project/whitenoise/)
        <!-- - [`pillow`](https://pypi.org/project/pillow/) -->
1. Now that we've installed the packages, let's use them to help us config our app for heroku. Update the following in your `settings.py` file
    - Add this to your `MIDDLEWARE` variable (anywhere after `django.middleware.security.SecurityMiddleware`)

        ```python
        'whitenoise.middleware.WhiteNoiseMiddleware'
        ```

    - Add these lines (you can add them right under `STATIC_URL` for organizational purposes)

        ```python
        STATICFILES_DIRS = [
          os.path.join(BASE_DIR, 'static'),
        ]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
        ```

    - Import `dj_database_url` and replace the `DATABASES` variable

        ```python
        import dj_database_url

        DATABASES = {
          'default': dj_database_url.config(
            default='sqlite:///{path}/db.sqlite3'.format(path=BASE_DIR),
            conn_max_age=600,
            conn_health_checks=True,
          )
        }
        ```

    - Update `TEMPLATES` with values for `'DIRS'`

        ```python
        TEMPLATES = [
          {
            ...

            'DIRS': [BASE_DIR / 'templates'],

            ...
          }
        ]
        ```

1. Create a `static/` directory at the root and add a `.gitkeep` file to the folder so that git won't delete the directory
1. Test that your API works normally with the new set up locally.
    - If you're having issues, try to open a new terminal and run the server there.
1. Create an app within Heroku for this code to be deployed to

    > **You might want to skip ahead and connect things, but whatever you do DO NOT DEPLOY ANYTHING YET!!!**

1. Go to the app's setting in Heroku and add all of the variables we've defined in the `.env` file.

    - `SECRET_KEY`: Create a differet secret key for this app using the command from above
    - `DEBUG`: If this is a deploy for production, I'd set this to `false`. But f this is for a testing environment, or you're still in the development stage, set this to `true`
    - `ALLOWED_HOSTS`: If you scroll down in settings within heoku, you'll find what domain to put there under "Domain". For an example you could set this to `ancient-beach-72402-21b2a1da8e94.herokuapp.com`. If you ever need to add any more domains, make sure to seperate them by commas (`,`) like how we set up the allowed hosts locally in our `.env` file.
        - Make sure to remove the "https://" and any thing after the tld (.com)
    - `CORS_ORIGIN_WHITELIST`: This is where you define what url's can hit this API. So this should include any FE app that will hit this, seperated by comma's (`,`).

1. Now you can add on the Postgress DB addon to the app

    - Go to the "Resources"section within Heroku
    - In the text box right under "Add-ons", start typing "Postgres"
    - Select the "Heroku Postgres" add-on. (This add on is not free, so you will have to add payment to your account in order for this to work)

1. Now that everything's set up config wise, you can now connect your repo to the Heroku app

    - Make sure to commit and push your changes up to GitHub
    - Go to the "Deploy" section within heroku
    - Under "Deployment method" select "GitHub"
    - Search for the repo you want to connect and select it
    - Now for the first deploy, under "Manual deploy" select what beanch you want deployed
    - Click "Deploy branch"
    - If you want to, feel free to also set up Automatic Deployment in this section as well.
    - Wait for app to build and deploy sucessfully (You can check this under "Activity")

1. Your app is now deployed! But you will notice that there are errors that mention that certain tables don't exist like: "ProgrammingError at /users/". Let's fix that!
1. Now that we have the DB set up and ready to go using our Add On, let's set up commands we want to tell heroku to run every time we deploy our app. We want to be able to have the heroku app run the following commands: `python manage.py makemigrations` (to check for changes to the models code wise and make instructions on what changes to the DB need to be made) and `python manage.py migrate` (to apply those changes to the DB)
    - Update the `Procfile` to look like this:

        ```Procfile
        web: gunicorn tutorial.wsgi
        release: python manage.py makemigrations; python manage.py migrate;
        ```

    - Save and commit your changes to your branch and push it up

1. If you have automatic deploy on then the build should automaticlly start, if not, fee free to manyally deploy in the same way we deplotyed the app at first.
1. Now your app should work as expected!!1
