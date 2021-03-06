# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class EosActionLinkAuth(p.MessageType):

    def __init__(
        self,
        account: int = None,
        code: int = None,
        type: int = None,
        requirement: int = None,
    ) -> None:
        self.account = account
        self.code = code
        self.type = type
        self.requirement = requirement

    @classmethod
    def get_fields(cls):
        return {
            1: ('account', p.UVarintType, 0),
            2: ('code', p.UVarintType, 0),
            3: ('type', p.UVarintType, 0),
            4: ('requirement', p.UVarintType, 0),
        }
