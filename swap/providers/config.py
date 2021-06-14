#!/usr/bin/env python3

import datetime

from swap import __version__

# Bitcoin config
bitcoin: dict = {
    "mainnet": {
        "blockchain": "https://blockchain.info",
        "smartbit": "https://api.smartbit.com.au/v1/blockchain",
        "blockcypher": {
            "url": "https://api.blockcypher.com/v1/btc/main",
            "token": "c6ef693d3c024088810e6fac2a1494ee"
        }
    },
    "testnet": {
        "blockchain": "https://testnet.blockchain.info",
        "smartbit": "https://testnet-api.smartbit.com.au/v1/blockchain",
        "blockcypher": {
            "url": "https://api.blockcypher.com/v1/btc/test3",
            "token": "c6ef693d3c024088810e6fac2a1494ee"
        }
    },
    "path": "m/44'/0'/0'/0/0",
    "BIP44": "m/44'/0'/{account}'/{change}/{address}",
    "unit": "SATOSHI",
    "timeout": 60,
    "locktime": 0,
    "max_amount": True,
    "version": 2,
    "network": "mainnet",
    "sequence": 1000,
    "headers": {
        "user-agent": f"Swap User-Agent {__version__}",
        "content-type": "application/json; charset=utf-8",
        "accept": "application/json"
    }
}

# Bytom config
bytom: dict = {
    "mainnet": {
        "bytom-core": "http://localhost:9888",
        "blockmeta": "https://blockmeta.com/api/v3",
        "blockcenter": "https://bcapi.bystack.com/bytom/v3",
        "mov": "https://ex.movapi.com/bytom/v3"
    },
    "solonet": {
        "bytom-core": "http://localhost:9888",
        "blockmeta": None,
        "blockcenter": None,
        "mov": None
    },
    "testnet": {
        "bytom-core": "http://localhost:9888",
        "blockmeta": None,
        "blockcenter": None,
        "mov": None
    },
    "path": "m/44/153/1/0/1",
    "BIP44": "m/44/153/{account}/{change}/{address}",
    "indexes": ["2c000000", "99000000", "01000000", "00000000", "01000000"],
    "unit": "NEU",
    "timeout": 60,
    "asset": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
    "fee": 10_000_000,
    "estimate_fee": True,
    "confirmations": 1,
    "max_amount": True,
    "network": "mainnet",
    "forbid_chain_tx": False,
    "sequence": 1000,
    "headers": {
        "user-agent": f"Swap User-Agent {__version__}",
        "content-type": "application/json; charset=utf-8",
        "accept": "application/json"
    }
}

# Vapor config
vapor: dict = {
    "mainnet": {
        "vapor-core": "http://localhost:9889",
        "blockmeta": "https://vapor.blockmeta.com/api/v1",
        "blockcenter": "https://bcapi.bystack.com/vapor/v3",
        "mov": "https://ex.movapi.com/vapor/v3"
    },
    "solonet": {
        "vapor-core": "http://localhost:9889",
        "blockmeta": None,
        "blockcenter": None,
        "mov": None
    },
    "testnet": {
        "vapor-core": "http://localhost:9889",
        "blockmeta": None,
        "blockcenter": None,
        "mov": None
    },
    "path": "m/44/153/1/0/1",
    "BIP44": "m/44/153/{account}/{change}/{address}",
    "indexes": ["2c000000", "99000000", "01000000", "00000000", "01000000"],
    "unit": "NEU",
    "timeout": 60,
    "asset": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
    "fee": 10_000_000,
    "estimate_fee": True,
    "confirmations": 1,
    "max_amount": True,
    "network": "mainnet",
    "forbid_chain_tx": False,
    "sequence": 1000,
    "headers": {
        "user-agent": f"Swap User-Agent {__version__}",
        "content-type": "application/json; charset=utf-8",
        "accept": "application/json"
    }
}

# Ethereum config
ethereum: dict = {
    "mainnet": {
        "infura": {
            "http": "https://mainnet.infura.io/v3",
            "websocket": "wss://mainnet.infura.io/ws/v3",
            "token": "4414fea5f7454211956b1627621450b4"
        }
    },
    "ropsten": {
        "infura": {
            "http": "https://ropsten.infura.io/v3",
            "websocket": "wss://ropsten.infura.io/ws/v3",
            "token": "4414fea5f7454211956b1627621450b4"
        }
    },
    "kovan": {
        "infura": {
            "http": "https://kovan.infura.io/v3",
            "websocket": "wss://kovan.infura.io/ws/v3",
            "token": "4414fea5f7454211956b1627621450b4"
        }
    },
    "rinkeby": {
        "infura": {
            "http": "https://rinkeby.infura.io/v3",
            "websocket": "wss://rinkeby.infura.io/ws/v3",
            "token": "4414fea5f7454211956b1627621450b4"
        }
    },
    "testnet": {
        "ganache-cli": {
            "http": "http://localhost:8545",
            "websocket": "wss://localhost:8545",
            "token": None
        }
    },
    "path": "m/44'/60'/0'/0/0",
    "BIP44": "m/44'/60'/{account}'/{change}/{address}",
    "units": {
        "ETH": 1,
        "Gwei": 1_000_000_000,
        "Wei": 1_000_000_000_000_000_000
    },
    "provider": "http",
    "network": "mainnet",
    "unit": "Wei",
    "gas": 3000000,
    "timeout": 60,
    # "time": int(datetime.timestamp(datetime.now())) + (3600 * 1)  # 1 hour
}
