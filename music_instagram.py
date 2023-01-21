import random

def main():
    tag1 = ["#music" ,"#musica" ,"#musician" ,"#musically" ,"#newmusic" ,"#musicproducer" ,"#instamusic" ,"#musicians" ,"#musicislife" ,"#musiclover" ,
            "#musiclife","#guitar" ,"#guitarist" ,"#guitarra" ,"#guitarplayer" ,"#guitars" ,"#guitarsolo","#guitarsdaily" ,"#electricguitar" ,"#guitarsofinstagram" ,
            "#guitarrista" ,"#guitaristsofinstagram" ,"#rock","#rockmusic" ,"#rockclimbing" ,"#jazzrock" ,"#hardrock" ,"#jazz" ,"#jazzmusic" ,"#djent"]

    tag1_list = random.sample(tag1, 2)

    tag2 = ["djent", "#musicman" ,"#musiceducation" ,"#musicforlife" ,"#musicislove" ,"#musicmaker" ,"#musicart" ,"#musicproducerlife" ,"#musicnews" ,"#musicaddict" ,
            "#musicflow" ,"#musican" ,"#musicgram" ,"#musiclive" ,"#musicblogger" ,"#musicacristiana" ,"#musicheals" ,"#musically🎶", "#musiccomposer" ,"#chillmusic" ,
            "#musicbank" ,"#musicworld" ,"#feelthemusic" ,"#musicalinstrument" ,"#musicvideoshoot" ,"#musicality","#musicista" ,"#mymusic" ,"#instrumentalmusic" ,
            "#musiclifestyle" ,"#musicquotes" ,"#makingmusic" ,"#musiciansdaily" ,"#musicallyvideo" ,"#instamusician" ,"#nomusicnolife" ,"#guitarlove" ,"#guitarworld" 
            ,"#guitarsarebetter" ,"#guitarpedals" ,"#guitarlessons" ,"#guitarras" ,"#guitarplayers" ,"#guitarstagram" ,"#guitarspotter" ,"#guitareffects" ,"#guitarrist",
            "#guitardaily" ,"#guitarpick" ,"#guitarriff" ,"#guitarplaying","#espguitars" ,"#guitarvideo" ,"#guitarman" ,"#guitarsolos" ,"#guitarpicks" ,"#guitariste" ,
            "#guitarlovers" ,"#guitarpractice" ,"#sologuitar" ,"#guitargasm" ,"#rockguitar" ,"#leadguitar" ,"#playguitar" ,"#guitargram" ,"#electricguitars" ,"#guitarart" 
            ,"#guitarnerd","#mathrock"]

    tag2_list = random.sample(tag2, 6)

    tag3 = ["#musicmotivation" ,"#musicdesign" ,"#musicbloggers" ,"#musicalartist" ,"#musicbeats" ,"#musichealsthesoul" ,"#musicispower" ,"#musicarock" ,"#musicisart" ,
            "#musiciens" ,"#musicexecutives" ,"#musiccityusa" ,"#musicmood" ,"#musicvideoeditor" ,"#musicwasmyfirstlove" ,"#musicedit",
            "#musicquote" ,"#musicclip" ,"#musiceducationmatters" ,"#musicinstruments" ,"#musically_rus" ,"#musicstyle" ,"#musicnote" ,
            "#musicproject"  ,"#musicculture", "#musicastudios","#musicosbrasileiros" ,"#musictherapist" ,"#guitarpickups" ,"#guitarshow" ,"#guitarplay" ,
            "#guitarcollector" ,"#guitarchords" ,"#guitarista" ,"#guitarelectric" ,"#guitarrasolo","#guitarimprovisation"  ,"#guitaristlife" ,"#guitarristasargentinos" ,
            "#guitaracoustic" ,"#guitartime" ,"#guitarplayersunite" ,"#guitarposts" ,"#guitaraddict" ,"#guitara" ,"#offsetguitars" ,"#instaguitarist" ,
            "#rockmath" ,"#mathgirlsrock" ,"#rocketmath" ,"#rockingmath" ,"#mathsrock"  ,"#mathirock" ,"#matheorock" ,"#mathnasiumeaglerock" ,"#mathcentersrock" ,
            "#mathrocks" ,"#shinymathrocks" ,"#mathrockmemes" ,"#mathrockriff" ,"#mathrockmusic" ,"#mathrocksmysocks" ,"#japanesemathrock" ,"#mathrockbands" ,
            "#emomathrock"]

    tag3_list = random.sample(tag3, 7)

    all_tags = tag1_list + tag2_list + tag3_list

    print(*all_tags)

for _ in range(15):
    main() 
    print("xxxxxxxxxx")