import os
import re

from environ import Env


def get_env(file_path):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(file_path)))

    env = Env()
    env.read_env(os.path.join(base_dir, ".env"))

    return env


def get_env_names():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_names = []
    with open(f"{base_dir}/.env", encoding="utf8") as variables:
        for line in variables:
            line = line.strip()
            line = re.search(".+?=", line)
            if line:
                env_var = line[line.start()]
                if "PROD_" not in env_var:
                    env_var = env_var.replace("=", "")
                    env_names.append(env_var)

    return env_names
