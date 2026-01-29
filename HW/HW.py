## shape class
from __future__ import annotations

from os import name


class Shape:

    def __init__(self, name:str)-> None:
        self._name: str = name
        self._area: float = 0.0


    def getArea(self) -> float:
        return self._area



    def setArea(self)-> float:
        self._area = area




    def getName(self) -> str:
        self._name = name



    def __str__(self) -> str:
        return self._name




    def__eq__(self,other:Shpae) -> bool:
        if not isinstance(shape):
            return False
        return self._name == other._name



    def main() -> None:
        s1 = Shape("S1")
        s2 = Shape("S2")
        s3 = Shape("S3")

        print(s1)
        print(s2)
        print(s3)

    if __name__=="__main__":
        main()