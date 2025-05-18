import tomllib


def read_config(filename: str) -> dict:
    with open(filename, "rb") as file:
        config_dict = tomllib.load(file)
    return config_dict
