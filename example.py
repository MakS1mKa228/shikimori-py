from pprint import pprint
from shikimori_py import ShikiMori


def main():
    shiki = ShikiMori(authorization_code = "OAUTH_CODE")

    pprint(shiki.get(
        type = "mangas", 
        query = {"search": "no game no life"}
    )[0]) 

    # MangaItem(id=48397, name='No Game No Life', russian='Нет игры — нет жизни', image=Image(original='/system/mangas/original/48397.jpg?1636188617', preview='/system/mangas/preview/48397.jpg?1636188617', x96='/system/mangas/x96/48397.jpg?1636188617', x48='/system/mangas/x48/48397.jpg?1636188617'), url='/mangas/z48397-no-game-no-life', kind='manga', score='7.99', status='ongoing', aired_on=datetime.date(2013, 1, 26), released_on=None, volumes=0, chapters=0)

    pprint(shiki.get(
        type = "ranobe", 
        query = {"search": "no game no life"})
    [0])

    # RanobeItem(id=48399, name='No Game No Life', russian='Нет игры — нет жизни', image=Image(original='/system/mangas/original/48399.jpg?1636189576', preview='/system/mangas/preview/48399.jpg?1636189576', x96='/system/mangas/x96/48399.jpg?1636189576', x48='/system/mangas/x48/48399.jpg?1636189576'), url='/mangas/z48399-no-game-no-life', kind='light_novel', score='8.51', status='ongoing', aired_on=datetime.date(2012, 4, 25), released_on=None, volumes=0, chapters=0)


if __name__ == "__main__": main()