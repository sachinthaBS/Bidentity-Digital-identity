import json
import os

from web3 import Web3
from dotenv import load_dotenv
from web3.types import TxReceipt
from flask import Flask, request
from flask_restx import Resource, Api, fields, Namespace

load_dotenv()

app = Flask(__name__)
api = Api(app, version='1.0', title='ID system', description='Digital ID System')
ns = api.namespace('ID', 'Main ID system')

CONTRACT_NAME = 'uIdentity'
chain_id = int(os.getenv('CHAIN_ID'))
my_address = os.getenv('MY_ADDRESS')
my_private_key = os.getenv('MY_PRIVATE_KEY')
contract_address = open('./ContractAddress', 'r').read()
abi = json.loads(open(f'./build/{CONTRACT_NAME}.sol/abi.json', 'r').read())


def create_transaction(w3, contract, function_name, params=None, gasPrice=None) -> TxReceipt:
    if params is None:
        params = []
    nonce = w3.eth.getTransactionCount(my_address)
    tx = getattr(contract.functions, function_name)(*params).buildTransaction(
        {
            "gasPrice": gasPrice if gasPrice else w3.eth.gas_price,
            "chainId": chain_id,
            "from": my_address,
            "nonce": nonce,
        }
    )
    signed_txn = w3.eth.account.sign_transaction(tx, private_key=my_private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(*tx_receipt['logs'], sep='\n')
    return tx_receipt


    if __name__ == '__main__':
        app.run(debug=False)