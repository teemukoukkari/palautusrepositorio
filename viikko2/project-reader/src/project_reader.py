from urllib import request
import toml
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            parsed['tool']['poetry']['name'],
            parsed['tool']['poetry']['description'],
            parsed['tool']['poetry']['license'],
            parsed['tool']['poetry']['authors'],
            list(parsed['tool']['poetry']['dependencies']),
            list(parsed['tool']['poetry']['group']['dev']['dependencies'])
        )
