
# Web3py Giriş
Web3.py, Ethereum blockchain'ine erişmek için kullanılan bir Python kütüphanesidir. Bu kütüphane, Ethereum blockchain'inde bulunan verileri okuma ve yazma gibi işlemleri kolaylaştırmayı amaçlar. Web3.py, Ethereum'un ``JSON-RPC`` arabirimini kullanarak Ethereum ağına bağlanarak bu işlemleri gerçekleştirir.


## Web3py ile neler yapılabilir ?
Web3.py kütüphanesi sayesinde, Ethereum blockchain'inde bulunan verileri okuyabilir ve bu verileri değiştirebilirsiniz. Örneğin, bir Ethereum cüzdanının bakiyesini okuyabilir ve bu cüzdanın adresine Ether gönderebilirsiniz. Ayrıca, Ethereum smart contract'lerini de oluşturabilir ve yönetebilirsiniz. Bu sayede, Ethereum blockchain'ini kullanarak çeşitli uygulamalar geliştirebilirsiniz.

## JSON-RPC
JSON-RPC, bir web servis arabirimini tanımlayan bir protokoldür. Bu protokol, bir web servisine istek yaptığınızda cevap olarak JSON (JavaScript Object Notation) veri biçiminde bir yanıt döndürür. Bu sayede, web servisinin döndürdüğü verileri kolayca işleyebilir ve kullanabilirsiniz. JSON-RPC, açık bir standart olduğu için çeşitli programlama dillerinde kullanılabilir. Örneğin, Ethereum blockchain'i de JSON-RPC arabirimini kullanarak erişilebilir.

## Infura nedir ?
Infura, Ethereum ve diğer blockchain ağlarına erişmek için kullanılan bir hizmettir. Bu hizmet, Ethereum ve diğer blockchain ağlarına bağlanmak için gerekli olan sunucu ve depolama alanını sağlar. Böylece, Infura sayesinde Ethereum ve diğer blockchain ağlarına bağlanarak bu ağlarda bulunan verileri okuyabilir ve yazabilirsiniz. Infura, özellikle Ethereum blockchain'ine erişmek isteyen büyük ölçekli uygulamalar için kullanışlı bir hizmettir.
Ayrıca Infura'nın birçok benzeri bulunmaktadır. Örneğin, Alchemy, Blockdaemon ve QuikNode gibi hizmetler Ethereum ve diğer blockchain ağlarına erişmek için kullanılabilir. Bu hizmetlerin hepsi, Infura gibi Ethereum ve diğer blockchain ağlarına bağlanmak için gerekli olan sunucu ve depolama alanını sağlar. Bu sayede, bu hizmetler sayesinde de Ethereum ve diğer blockchain ağlarına bağlanarak bu ağlarda bulunan verileri okuyabilir ve yazabilirsiniz. Hangi hizmeti kullanacağınızı seçerken, size en uygun olan hizmeti seçebilirsiniz.

## Ethereum ağında transfer (örnek)

Ethereum ağında web3.py kullanarak transfer yapmak oldukça basittir. Öncelikle, web3.py kütüphanesini kurmanız ve projenize dahil etmeniz gerekmektedir. Daha sonra, Ethereum ağına bağlanmak için gerekli olan bir Infura anahtarı almanız gerekmektedir. Bu anahtarı kullanarak web3.py kütüphanesi ile Ethereum ağına bağlanabilirsiniz.

Bağlandıktan sonra, transfer yapmak istediğiniz cüzdanın adresini ve bu cüzdanın bakiyesini okuyabilirsiniz. Ardından, transfer yapmak istediğiniz miktarı belirleyerek bu miktarı cüzdanınıza gönderebilirsiniz. Bu işlemi gerçekleştirmek için aşağıdaki kod parçacığını kullanabilirsiniz:

```Python
# web3 kütüphanesini dahil edin
from web3 import Web3

# Ethereum ağına bağlanmak için gerekli olan Infura anahtarını alın
infura_key = "your-infura-key"

# Ethereum ağına bağlanmak için web3.py kütüphanesini kullanın
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/{infura_key}"))

# Transfer yapmak istediğiniz cüzdanın adresini belirtin
wallet_address = "your-wallet-address"

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
```
Yukarıdaki kod parçacığını çalıştırdıktan sonra, transfer işleminiz gerçekleşecek ve cüzdanınıza belirlediğiniz miktar Ether gönderilecektir. Daha sonra, cüzdanınızın bakiyesini tekrar kontrol ederek yeni cüzdan bakiyesini gösterecektir.
