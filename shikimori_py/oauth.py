from requests import Response, post as r_post
import json

class OAuth():

    def __init__(self, authorization_code: str):

        self._authorization_code = authorization_code
        self.path = __file__[:-8]
        self._load_config()
        if self._config["oauth_code"] is None or self._authorization_code != self._config["oauth_code"]:
            self._config.update({
                "oauth_code" : self._authorization_code, 
                "access_token" : None, 
                "refresh_token" : None
            })
            self._update_config()
            self._get_new_token()

    def _load_config(self) -> None:
        with open(f"{self.path}config.json", "r") as file:
            self._config: dict = json.loads(file.buffer.read())
            file.close()
        return
    def _update_config(self) -> None:
        
        with open(f"{self.path}config.json", "w") as file:
            file.write(str(self._config).replace("'", '"').replace("None", "null"))
            file.close()

    def refresh(self) -> str:
        headers = {"User-Agent": "shikimori-py"}
        body = {
            "grant_type":"refresh_token",
            "client_id": self._config["client_id"],
            "client_secret": self._config["client_secret"],
            "refresh_token": self._config["refresh_token"],
        }
        resp: Response = r_post("https://shikimori.one/oauth/token", headers=headers, data=body)
        json = resp.json()
        if  resp.status_code == 200:
            self._config.update({"access_token": json["access_token"], "refresh_token": json["refresh_token"]})
            self._update_config()
            return self._config["access_token"]
        if resp.status_code == 400:
            self._get_new_token()

    def get_token(self) -> str:
        return self._config["access_token"]

    def _get_new_token(self) -> None:
        headers = {"User-Agent": "shikimori-py"}
        body = {
            "grant_type":"authorization_code",
            "client_id": self._config["client_id"],
            "client_secret": self._config["client_secret"],
            "code": self._config["oauth_code"],
            "redirect_uri":"https://shikimori.org/oauth"    
        }
        resp: Response = r_post("https://shikimori.one/oauth/token", headers=headers, data=body)
        json = resp.json()

        if resp.status_code == 200:
            
            self._config.update({"access_token": json["access_token"], "refresh_token": json["refresh_token"]})
            self._update_config()

        if resp.status_code == 400:
            raise Exception(json)
        
