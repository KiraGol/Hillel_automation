from __future__ import annotations

from typing import List, Type
from xml.etree import ElementTree


class Movie:
    def __init__(
            self,
            title: str,
            format: str,
            year: int,
            rating: str,
            description: str,
            category: str,
    ):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category

    @classmethod
    def from_xml(cls, path: str) -> Type[list]:
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []

        for movie in collection.iter("movie"):
            title = movie.attrib["title"]
            # print(title)

            for child in movie.findall("*"):
                other = child.text
                # print(other)

            movies.append(title)
            movies.append(other)
            print(movies)


if __name__ == '__main__':
    movies = Movie.from_xml("market.xml")
