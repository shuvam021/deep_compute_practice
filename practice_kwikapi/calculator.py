# pylint: disable=all

from dataclasses import asdict, dataclass


@dataclass
class DataSerializer:
    x: int
    y: int

    def url_params(self) -> str:
        params = asdict(self)
        return "&".join(f"{k}={v}" for k, v in params.items())


class Calculator:
    def add(self, x: int, y: int) -> int:
        return x + y

    def sub(self, x: int) -> int:
        return x - 1


class TestService:
    def str_val(self) -> str:
        return "Hello"

    def str_val2(self) -> str:
        return "World"


calc_requests = {
    "add()": f"anything/add?{DataSerializer(x=1, y=2).url_params()}",
    "sub()": "anything/sub?x=2",
    "str_val()": "anything/str_val",
    "str_val2()": "anything/str_val2",
}
