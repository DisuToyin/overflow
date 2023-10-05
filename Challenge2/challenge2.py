import requests

api_key_token="FZEF4I36DBDVXF674MVHEWX3CEDMZ96N3U"
action="eth_getTransactionReceipt"
module="proxy"



def validate_transaction_hash(transaction_hash):
    # Remove "0x" prefix if present
    if transaction_hash.startswith("0x"):
        transaction_hash = transaction_hash[2:]

    # Check if the remaining string is a valid hexadecimal number
    try:
        int(transaction_hash, 16)
        return len(transaction_hash) == 64  # Ethereum transaction hashes are 64 hexadecimal characters
    except ValueError:
        return False


def print_transfers(txhash):
    # Check if the transaction hash is valid
    if not validate_transaction_hash(txhash):
        print("Invalid transaction hash.")
        return
    

    api_url= f"https://api.etherscan.io/api?module={module}&action={action}&txhash={txhash}&apikey={api_key_token}"


    try:
        response = requests.get(api_url)
        data = response.json()

        # print(data)

        if data["result"] != None:
            logs =  data.get("result").get("logs")
            if logs:
                
                transfers = []
                for log in logs:
                    if 'topics' in log and len(log['topics']) >= 3 and 'data' in log:
                        from_address = log['topics'][1] #The "from" address is typically stored in the second topic
                        to_address = log['topics'][2] #The "to" address is typically stored in the third topic
                        amount = int(log['data'], 16)
                        transfers.append({
                            "from": from_address,
                            "to": to_address,
                            "amount": amount
                        })
                    else:
                        print("Incomplete or missing data in log entry:", log["address"])
                
                return transfers

        else:
            print("No transfer logs found for this transaction.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")



txhash="0x3fbb21da357fdd74a12319ee423b4f30829030ba53b1d8d9e005c0da138e2263"
print(print_transfers(txhash))