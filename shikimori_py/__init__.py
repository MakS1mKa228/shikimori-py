from requests import Response, get as _r_get
from .types import *
from .oauth import OAuth



class ShikiMori():

    def __init__(
            self, 
            authorization_code: str
        ) -> None:
        self._oauth = OAuth(authorization_code)
        self._access_token = self._oauth.get_token()

    def get(self, endpoint, query) -> list[AnimeItem | MangaItem | RanobeItem]:

        self._endpoint = endpoint
        self._query = [f"?{key}={value}" for key, value in query.items()]
        self._url = f"https://shikimori.one/api/{endpoint}{''.join(self._query)}"

        resp: Response = _r_get(self._url, headers = {
            "User-Agent": "shikimori-py",
            "Authorization": f"Bearer {self._access_token}"
        })  
        if resp.status_code == 401: 
            self._access_token = self._oauth.refresh()
            return self.get(type, query)
        
        match self._endpoint:
            case "animes":
                return [AnimeItem(**item) for item in resp.json()]
            case "mangas":
                return [MangaItem(**item) for item in resp.json()]
            case "ranobe":
                return [RanobeItem(**item) for item in resp.json()]
            case _:
                return "Error! Cannot find this endpoint"
__all__ = ["ShikiMori"]
