from typing import Dict, List
from dataclasses import dataclass
from requests import Session, Request, Response

from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


@dataclass
class BaseClientConfig:
    base_url: str


def set_session_retry(session: Session, total: int = 3, backoff_factor: int = 2):
    retry = Retry(total=total, backoff_factor=backoff_factor)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)


class BaseClient:
    def __init__(self, config: BaseClientConfig):
        self.config = config

        # create session and set retry
        self.s = Session()
        set_session_retry(self.s)

    def make_request(self, prep_req: Request) -> Response:
        # prepend base url, prep_req.url contains only endpoint
        prep_req.url = self.config.base_url + prep_req.url
        req = prep_req.prepare()

        resp = self.s.send(req)

        return resp

    def close(self):
        self.s.close()
