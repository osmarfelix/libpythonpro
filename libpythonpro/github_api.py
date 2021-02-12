import requests


def buscar_avatar(usuario):
    """
    Buscar um avatar de um usuário no gitHub
    :param usuario: str com o nome do usuario no github
    :return: str com o link do avatar
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('osmarfelix'))
