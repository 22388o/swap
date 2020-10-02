#!/usr/bin/env python3

from btcpy.structs.crypto import PrivateKey
from btcpy.structs.sig import (
    P2pkhSolver, IfElseSolver, HashlockSolver, Branch, RelativeTimelockSolver
)
from btcpy.structs.script import (
    ScriptBuilder, IfElseScript
)
from btcpy.structs.transaction import Sequence
from typing import Optional, Union

from ..config import bitcoin
from .wallet import Wallet
from .htlc import HTLC

# Bitcoin config
config = bitcoin()


class FundSolver:
    """
    Bitcoin Fund solver.

    :param root_xprivate_key: Bitcoin sender root xprivate key.
    :type root_xprivate_key: str
    :param account: Bitcoin derivation account, defaults to 0.
    :type account: int
    :param change: Bitcoin derivation change, defaults to False.
    :type change: bool
    :param address: Bitcoin derivation address, defaults to 0.
    :type address: int
    :param path: Bitcoin derivation path, defaults to None.
    :type path: str
    :returns: FundSolver -- Bitcoin fund solver instance.

    >>> from swap.providers.bitcoin.solver import FundSolver
    >>> from swap.providers.bitcoin.wallet import Wallet
    >>> sender_root_xprivate_key = "tprv8ZgxMBicQKsPeLxEBy2sJ8CqLdc76FUzeaiY5egrW4JdpM4F9b9A3L6AQhsY1TRsqJAfTdH7DdRAt5hRdcdhn5LnMZPiaGRR7Snrmd8CLqR"
    >>> fund_solver = FundSolver(root_xprivate_key=sender_root_xprivate_key)
    <swap.providers.bitcoin.solver.FundSolver object at 0x03FCCA60>
    """

    def __init__(self, root_xprivate_key: str, account: int = 0,
                 change: bool = False, address: int = 0, path: Optional[str] = None):
        if not path:
            path = config["BIP44"].format(
                account=account, change=(1 if change else 0), address=address
            )

        self._root_xprivate_key: str = root_xprivate_key
        self._path: Optional[str] = path

    def solve(self, network: str = config["network"]) -> P2pkhSolver:
        return P2pkhSolver(
            privk=PrivateKey.unhexlify(
                hexa=Wallet(network=network).from_root_xprivate_key(
                    root_xprivate_key=self._root_xprivate_key
                ).from_path(
                    path=self._path
                ).private_key()
            )
        )


class ClaimSolver:
    """
    Bitcoin ClaimSolver class.

    :param root_xprivate_key: Bitcoin sender root xprivate key.
    :type root_xprivate_key: str
    :param secret_key: Secret password/passphrase.
    :type secret_key: str
    :param bytecode: Bitcoin witness HTLC bytecode..
    :type bytecode: str
    :param account: Bitcoin derivation account, defaults to 0.
    :type account: int
    :param change: Bitcoin derivation change, defaults to False.
    :type change: bool
    :param address: Bitcoin derivation address, defaults to 0.
    :type address: int
    :param path: Bitcoin derivation path, defaults to None.
    :type path: str
    :returns:  ClaimSolver -- Bitcoin claim solver instance.

    >>> from swap.providers.bitcoin.solver import ClaimSolver
    >>> recipient_root_xprivate_key = "xprv9s21ZrQH143K4Kpce43z5guPyxLrFoc2i8aQAq835Zzp4Rt7i6nZaMCnVSDyHT6MnmJJGKHMrCUqaYpGojrug1ZN5qQDdShQffmkyv5xyUR"
    >>> bytecode = "63aa20821124b554d13f247b1e5d10b84e44fb1296f18f38bbaa1bea34a12c843e01588876a9140e259e08f2ec9fc99a92b6f66fdfcb3c7914fd6888ac6702e803b27576a91433ecab3d67f0e2bde43e52f41ec1ecbdc73f11f888ac68"
    >>> claim_solver = ClaimSolver(wallet=recipient_root_xprivate_key, secret_key="Hello Meheret!", bytecode=bytecode)
    <swap.providers.bitcoin.solver.ClaimSolver object at 0x03FCCA60>
    """

    def __init__(self, root_xprivate_key: str, secret_key: str, bytecode: str,
                 account: int = 0, change: bool = False, address: int = 0, path: Optional[str] = None):
        if not path:
            path = config["BIP44"].format(
                account=account, change=(1 if change else 0), address=address
            )

        self._root_xprivate_key: str = root_xprivate_key
        self._secret_key: str = secret_key
        self._path: Optional[str] = path
        self._bytecode: str = bytecode

    def solve(self, network: str = config["network"]) -> IfElseSolver:
        return IfElseSolver(
            branch=Branch.IF,
            inner_solver=HashlockSolver(
                preimage=self._secret_key.encode(),
                inner_solver=P2pkhSolver(
                    privk=PrivateKey.unhexlify(
                        hexa=Wallet(network=network).from_root_xprivate_key(
                            root_xprivate_key=self._root_xprivate_key
                        ).from_path(
                            path=self._path
                        ).private_key()
                    )
                )
            )
        )

    def witness(self, network: str = config["network"]) -> Union[IfElseScript, ScriptBuilder]:
        return HTLC(network=network).from_bytecode(
            bytecode=self._bytecode
        ).script


class RefundSolver:
    """
    Bitcoin RefundSolver class.

    :param root_xprivate_key: Bitcoin sender root xprivate key.
    :type root_xprivate_key: str
    :param bytecode: Bitcoin witness HTLC bytecode..
    :type bytecode: str
    :param sequence: Bitcoin witness sequence number(expiration block), defaults to 1000.
    :type sequence: int
    :param account: Bitcoin derivation account, defaults to 0.
    :type account: int
    :param change: Bitcoin derivation change, defaults to False.
    :type change: bool
    :param address: Bitcoin derivation address, defaults to 0.
    :type address: int
    :param path: Bitcoin derivation path, defaults to None.
    :type path: str
    :returns:  RefundSolver -- Bitcoin refund solver instance.

    >>> from swap.providers.bitcoin.solver import RefundSolver
    >>> sender_root_xprivate_key = "xprv9s21ZrQH143K3XihXQBN8Uar2WBtrjSzK2oRDEGQ25pA2kKAADoQXaiiVXht163ZTrdtTXfM4GqNRE9gWQHky25BpvBQuuhNCM3SKwWTPNJ"
    >>> bytecode = "63aa20821124b554d13f247b1e5d10b84e44fb1296f18f38bbaa1bea34a12c843e01588876a9140e259e08f2ec9fc99a92b6f66fdfcb3c7914fd6888ac6702e803b27576a91433ecab3d67f0e2bde43e52f41ec1ecbdc73f11f888ac68"
    >>> refund_solver = RefundSolver(root_xprivate_key=sender_root_xprivate_key, bytecode=bytecode sequence=1000)
    <swap.providers.bitcoin.solver.RefundSolver object at 0x03FCCA60>
    """

    def __init__(self, root_xprivate_key: str, bytecode: str, sequence: int = config["sequence"],
                 account: int = 0, change: bool = False, address: int = 0, path: Optional[str] = None):
        if not path:
            path = config["BIP44"].format(
                account=account, change=(1 if change else 0), address=address
            )

        self._root_xprivate_key: str = root_xprivate_key
        self._path: Optional[str] = path
        self._bytecode: str = bytecode
        self._sequence: int = sequence

    def solve(self, network: str = config["network"]) -> IfElseSolver:
        return IfElseSolver(
            branch=Branch.ELSE,
            inner_solver=RelativeTimelockSolver(
                sequence=Sequence(
                    seq=self._sequence
                ),
                inner_solver=P2pkhSolver(
                    privk=PrivateKey.unhexlify(
                        hexa=Wallet(network=network).from_root_xprivate_key(
                            root_xprivate_key=self._root_xprivate_key
                        ).from_path(
                            path=self._path
                        ).private_key()
                    )
                )
            )
        )

    def witness(self, network: str = config["network"]) -> Union[IfElseScript, ScriptBuilder]:
        return HTLC(network=network).from_bytecode(
            bytecode=self._bytecode
        ).script