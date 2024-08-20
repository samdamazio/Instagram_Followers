import instaloader
from decouple import config

# Cria uma instância do Instaloader
L = instaloader.Instaloader()

# Efetuar login
username = config("USER", default="", cast=str)
password = config("PASSWORD", default="", cast=str)
L.login(username, password)

# Carregar perfil do usuário
profile = instaloader.Profile.from_username(L.context, username)

# Obter lista de pessoas que sigo e seguidores
following = set(profile.get_followees())
followers = set(profile.get_followers())

# Encontrar quem sigo que não me segue de volta
not_following_back = following - followers

# Exibir os resultados
print("Pessoas que você segue e não te seguem de volta:")
for user in not_following_back:
    print(user.username)
