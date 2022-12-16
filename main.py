# web3 kütüphanesini dahil edin
from web3 import Web3

# Ethereum ağına bağlanmak için gerekli olan Infura anahtarını alın
infura_key = "your-infura-key"

# Ethereum ağına bağlanmak için web3.py kütüphanesini kullanın
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/{infura_key}"))

# Transfer yapmak istediğiniz cüzdanın adresini belirtin
wallet_address = "your-wallet-address"
private_key = "your-private-key"
# Cüzdanın bakiyesini okuyun
balance = w3.eth.getBalance(wallet_address)
print(f"Transferden once cüzdan bakiyesi : {balance}")
# Transfer yapmak istediğiniz miktarı belirtin (örneğin, 1 Ether)
amount = w3.toWei(1, "ether")

# Cüzdana transfer yapmak için gerekli olan işlem detaylarını belirtin
txn_details = {
    "to": wallet_address,
    "value": amount,
    "gas": 2000000,
    "gasPrice": w3.toWei("20", "gwei"),
}

# İşlemi imzalayarak cüzdana transfer yapın
signed_txn = w3.eth.account.signTransaction(txn_details, private_key)
w3.eth.sendRawTransaction(signed_txn.rawTransaction)

balance_last = w3.eth.getBalance(wallet_address)
print(f"Transferden sonra cüzdan bakiyesi : {balance_last}")
