import random

def main():
    tag1 = ["#nft" ,"#net" ,"#nftart" ,"#nfts" ,"#crypto" ,"#cryptocurrency" ,"#cryptoart" ,"#cryptonews" ,"#cryptocurrencies" ,"#cryptoartist","#investments "]

    tag1_list = random.sample(tag1, 2)

    tag2 = ["#nftmarketplace" ,"#netflixpremium" ,"#nftgallery" ,"#nftsstories" ,"#cryptoworld" ,"#cryptoinvestor" ,"#cryptomarket" ,"#cryptomining" ,"#cryptocurrencynews",
            "#cryptomemes" ,"#cryptotrader" ,"#cryptolife" ,"#cryptos" ,"#cryptoexchange" ,"#cryptopunks" ,"#cryptoinvesting" ,"#cryptocoin" ,"#cryptocurrencytrading" ,
            "#cryptozoology" ,"#cryptomoney" ,"#cryptowallet" ,"#cryptoartwork" ,"#cryptotraders" ,"#cryptomonnaie" ,"#cryptosignals" ,"#cryptotrade" ,"#cryptocommunity" ,
            "#nftcrypto" ,"#cryptoinvestment", "#cryptography" ,"#cryptoindia" ,"#cryptocurrencymarket" ,"#cryptolifestyle" ,"#cryptoeducation" ,"#blockchaintechnology",
            "#blockchainnews" ,"#artinvestment"]

    tag2_list = random.sample(tag2,6)

    tag3 = ["#nftopensea" ,"#opeanseanft" ,"#opeanseanftart" ,"#cryptocurrencycommunity" ,"#cryptocoins" ,"#cryptoexplorer" ,"#cryptocurrencymining" ,"#cryptoartists" ,
            "#cryptocurrencys" ,"#cryptocurency" ,"#cryptoartcollector" ,"#cryptocurrencyeducation" ,"#cryptomonedas" ,"#cryptohumor" ,"#cryptocurrency_news" ,
            "#cryptocurrencyinvestments" ,"#cryptoinvestors" ,"#cryptorevolution" ,"#cryptonft" ,"#tradingcrypto" ,"#cryptonewsdaily" ,"#cryptogames" ,
            "#cryptocurrencyinviestments" ,"#cryptominer" ,"#cryptoexpert" ,"#cryptolover", "#cryptotips","#cryptobusiness" ,"#cryptocurrencyrevolution" ,
            "#cryptocollectibles" ,"#cryptopsy" ,"#cryptomonnaies" ,"#cryptocurrencyinvestment" ,"#cryptocomnft" ,"#cryptomarkets","#cryptoanalysis" ,
            "#cryptokeys" ,"#cryptocurrecy" ,"#cryptocurrencyisthefuture" ,"#cryptocurrencymemes" ,"#cryptoinvest" ,"#cryptomaniaks" ,
            "#chainblock" ,"#blockchainsupplychain" ,"#chainpulleyblock" ,"#blockchainart" ,"#blockchainrevolution" ,"#blockchaintech" ,"#blockchaincommunity" ,
            "#blockchainmining" ,"#blockchaindevelopers" ,"#blockchaingaming" ,"#blockchaingames" ,"#blockchaindevelopment" ,"#blockchaingame" ,"#blockchainlife" ,
            "#blockchainsolutions" ,"#blockchainevents","#blockchainartists","#blockchain_technology" ,
            "#blockchainworld" ,"#blockchaintechnologies","#blockchaintechnologies" ,"#blockchainjobs" ,"#nftblockchain",]

    tag3_list = random.sample(tag3, 7)

    all_tags = tag1_list + tag2_list + tag3_list

    print(*all_tags)

for _ in range(15):
    main() 
    print("xxxxxxxxxx")