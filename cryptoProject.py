from web3 import Web3
from eth_account import Account

RPC_URL = "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

CONTRACT_ADDRESS = "0xYourContractAddress"

ABI = [
    {
        "inputs": [],
        "name": "executeAction",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

web3 = Web3(Web3.HTTPProvider(RPC_URL))

account = Account.from_key(PRIVATE_KEY)

contract = web3.eth.contract(
    address=CONTRACT_ADDRESS,
    abi=ABI
)

nonce = web3.eth.get_transaction_count(
    account.address
)

tx = contract.functions.executeAction().build_transaction({
    "from": account.address,
    "nonce": nonce,
    "gas": 200000,
    "gasPrice": web3.eth.gas_price
})

signed_tx = web3.eth.account.sign_transaction(
    tx,
    PRIVATE_KEY
)

tx_hash = web3.eth.send_raw_transaction(
    signed_tx.rawTransaction
)

print(
    "Transaction Hash:",
    web3.to_hex(tx_hash)
)
