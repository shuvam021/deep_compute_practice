# pylint:disable=all
import json

from kwikapi import API, BaseRequestHandler, MockRequest

from kwikapi_practice.calculator import Calculator, TestService, calc_requests


def get_request(app: API, val: str) -> dict:
    moc_res = MockRequest(url=val)
    response = BaseRequestHandler(app).handle_request(moc_res)
    return json.loads(response)


def main():
    app = API(default_version="v1")
    app.register(Calculator(), "v1")
    app.register(TestService(), "v1")

    requests = {**calc_requests}
    response = {k: get_request(app, v) for k, v in requests.items()}
    print(json.dumps(response, indent=4))

    return


if __name__ == "__main__":
    main()
