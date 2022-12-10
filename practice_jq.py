# pylint: disable=all
import json
from time import sleep

import jq

JSON_FILE = "./json_file.json"


def test_syntax():
    program = jq.compile("$a + $b + .", args={"a": 100, "b": 20})

    x = program.input(3)
    print(x.first())  # 100 + 20 + 3 = 123

    y = jq.compile(".[]")
    print(y)  # jq.compile('.[]')

    z = y.input([1, 2, 3])
    print(z.all())  # [1, 2, 3]

    z_1 = y.input([1, 2, 3, 4])
    print(z_1.all())  # [1, 2, 3, 4]

    x = jq.compile(".").input("42")
    print(x.text())  # "42"
    print(x.all())  # ['42']

    print(jq.compile("").input("x").text())
    print(jq.compile("").input("1").text())
    # print(jq.compile("").all())  # invalid syntax
    print(jq.compile("").input("1").all())
    print(jq.compile("").input("1").first())

    x = jq.compile("[.[]+3]").input([1, 2, 3])  # add each element with 3
    #  .    ->  include anything
    # []+3  ->  add 3 to each element of input list
    print(x.all())

    # print(
    #     jq.compile("[.[]+3]").input(["1", 2, 3]).all()
    # )  # invalid systax due to string input
    # print(jq.compile("[.[]+3]").input(1).all())  # invalid systax due to string input


class Demo:
    @staticmethod
    def read_file():
        """
        this function return filtered data using jq commands
        """
        with open(JSON_FILE) as f:
            input_data = json.load(f)
            for data in input_data:
                print(jq.compile("{(.username): .titles}").input(data).all())

    @staticmethod
    def serialize():
        with open(JSON_FILE) as f:
            for data in json.load(f):
                print(
                    jq.compile("{username: (.username), name:(.name)}")
                    .input(data)
                    .all()
                )


if __name__ == "__main__":
    test_syntax()
    # Demo.read_file()
    # print(f"{'='* 60}")
    # Demo.serialize()
