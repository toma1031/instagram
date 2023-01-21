import random

def main():
    tag1 = ["#nycart", "#contemporaryart", "#contemporaryartist", "#digitalart", "#artedigital","#nftart", "#nftartist", "#nftartists", "#nftartgallery", "#nftartwork", "#nftcollector", "#nftcommunity", "#nfts", "#cryptoart", "#opensea", "#nftcollectors", "#nftcollectibles", "#nftdrop", "#cryptoartist", "#nftcollection", "#openseanft", "#newstart", "#newart", "#newartist", "#artnews", "#newartwork", "#chicagoartist", "#artmuseum", "#artbasel", "#contemporaryart", "#contemporaryartist", "#contemporaryartwork", "#artgallery", "#galleryart", "#nftartgallery"]

    tag1_list = random.sample(tag1, 2)

    tag2 = ["#nycartist","#nycartists", 
            "#artcontemporary", "#contemporaryfineart","#digitalfanart", "#nftarts", "#nftartcollector", "#nftartcollector", 
            "#openseanftart", "#raredigitalart", "#nftnews", "#nftgallery", "#nftmarketplace", "#nftmagazine", "#nfthesearch",
            "#openseaart", "#cryptoartwork", "#newyorkart", "#newmediaart", "#newcontemporaryart", "#newbornart", "#newyearnewstart", "#neworleansart", "#newyorkartist", 
            "#newartists", "#chicagoart", "#chicagoartists", "#artcontemporary", "#contemporaryfineart", "#contemporaryartcurator", "#contemporaryartists", 
            "#contemporaryartgallery", "#contemporaryartcollectors", "#contemporaryartcollector", "#contemporaryarts", "#newcontemporaryart", "#contemporaryartmuseum", 
            "#artsgallery", "#galleryartist", "#contemporaryartgallery", "#onlineartgallery", "#artgallerys", "#artgallerynyc"
            ]

    tag2_list = random.sample(tag2, 6)

    tag3 = ["#nycartscene", "#contemporaryphotoart", "#contemporaryabstractart", "#digitalabstractart", "#digitalillustrationsart", "#nftartistsoninstagram", 
            "#nftartworks", "#nftartworks", "#nftartworld", "#nftartoftheday", "#nftartis", "#nftartcollection", "#openseanftartist", "#nftartdaily", "#nftartsale", 
            "#nftartistsofinstagram", "#nftartdrop", "#nftartmedia", "#nftarti̇st", "#nftathome", "#artchicago","#artinchicago", "#chicagopublicart", "#contemporaryglassart",
            "#artistgallery", "#galleryofart", "#artdigitalgallery", "#artpeoplegallery","#artegallery", "#artspacegallery", "#modernedengallery",
            "#modernartistsgallery", "#modernismgallery", "#modernartworkgallery", "#moderndesigngallery", "#modernandcontemporaryartgallery",
            "#galleryofmodernart", "#japanesecontemporaryart", "#japanesefanart", "#artjapanese", "#japanesepopart", "#japaneseflowerart", "#japanesefineart", 
            "#japanesemartialart", "#japaneseinspiredart"]

    tag3_list = random.sample(tag3, 7)

    all_tags = tag1_list + tag2_list + tag3_list

    print(*all_tags)

for _ in range(15):
    main() 
    print("xxxxxxxxxx")