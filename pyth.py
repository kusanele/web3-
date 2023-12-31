from web3 import Web3

# Connect to a local Ethereum node or Infura
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/XX'))

def get_latest_block_number():
    """Get the latest block number on the Ethereum mainnet."""
    return web3.eth.blockNumber

def get_block_details(block_number):
    """Get details about a specific block."""
    return web3.eth.getBlock(block_number)

def main():
    try:
        # Check if connected to Ethereum node
        if web3.isConnected():
            print(f"Connected to Ethereum node at {web3.providers[0].endpoint_uri}")

            # Get the latest block number
            latest_block_number = get_latest_block_number()
            print(f"Latest Block Number: {latest_block_number}")

            # Get details about a specific block (e.g., latest block)
            block_number = latest_block_number
            block_details = get_block_details(block_number)
            print(f"\nDetails for Block #{block_number}:\n{block_details}")
        else:
            print("Unable to connect to Ethereum node.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
