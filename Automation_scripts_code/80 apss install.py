
import subprocess
import time
def execute_adb(command):
    subprocess.call(command, shell=True)

def adbUp():
    #Storage
    # 91%used - 2.88GB free
    #1. Templerun
 
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.imangi.templerun' > clr ")
    print("Templerun")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #2. Templerun
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.imangi.templerun2' > clr ")
    print("Templerun 2")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #3. subwaysurf
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.kiloo.subwaysurf' > clr ")
    print("subwaysurf")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #4. hillclimb
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.fingersoft.hillclimb' > clr ")
    print("Hillclimb")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #5. CALL OF DUTY
    #execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.activision.callofduty.shooter' ")
    #time.sleep(5)
    #execute_adb("adb shell input tap 500 600")
    #execute_adb("adb shell input tap 500 610")
    #time.sleep(2)
    #6. angrybirdsfriends
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.rovio.angrybirdsfriends' > clr ")
    print("angrybirdsfriends")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #7. candycrushsaga
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.king.candycrushsaga' > clr ")
    print("candycrushsaga")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #8. racingmoto
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.droidhen.game.racingmoto' > clr ")
    print("racingmoto")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #9 ball poll
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.miniclip.eightballpool' ")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #10 com.ludo.king
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.ludo.king' > clr ")
    print("ludoking")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(4)
    #11.freefiremax
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.dts.freefiremax' > clr ")
    print("freefiremax")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #12. cookingmadness
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.biglime.cookingmadness' > clr")
    print("cookingmadness")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #13. game.nfs14_row
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.ea.game.nfs14_row' >clr")
    print("NFS14 row")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #14. package:com.byjus.thelearningapp.premium
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.byjus.thelearningapp.premium' > clr ")
    print("thelearningapp premium")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #15. com.easygames.race
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.easygames.race' > clr ")
    print("easygames race")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #16. com.mast.status.video.edit
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.mast.status.video.edit' > clr ")
    print("mast status video edit")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
   
    #17. flipkart
    # execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.flipkart.android' > clr ")
    # print("Flipkart")
    # time.sleep(5)
    # xecute_adb("adb shell input tap 500 600")
    # time.sleep(2)
    #18. Amazon
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=in.amazon.mShop.android.shopping' >clr ")
    print("Amazon")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    # 19 Meesho
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.meesho.supply' > clr ")
    print("meesho")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(4)
    #20. com.myntra.android
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.myntra.android' > clr ")
    print("myntra")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #21. com.microsoft.bing
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.microsoft.bing' > clr ")
    print("bing")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #22. amazon music
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.amazon.mp3' ")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #23. instagram
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.instagram.android' >clr ")
    print("instagram")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #24. instagram.lite
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.instagram.lite' > clr ")
    print("instagram lite")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #25. com.hkfuliao.chamet
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.hkfuliao.chamet'> clr ")
    print("chamet")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #26. whatsApp
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.whatsapp'> clr ")
    print("WhatsApp")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    #27. com.snapdeal.main
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.snapdeal.main' > clr ")
    print("snapdeal")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #28. fc.admin.fcexpressadmin 
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=fc.admin.fcexpressadmin' > clr ")
    print("fc admin")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #29. com.fsn.nykaa
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.fsn.nykaa' > clr ")
    print("nykaa")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #30.  com.olx.southasia
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.olx.southasia'> clr ")
    print("OLX")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #31. com.ebay.mobile
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.ebay.mobile'> clr ")
    print("com.ebay.mobile")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #32. bigbasket
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.bigbasket.mobileapp' >clr ")
    print("Bigbasket")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #33. zeptolab
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.zeptolab.ctr.ads' > clr ")
    print("zeptolab")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #33. dunzo
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.dunzo.user' > clr ")
    print("dunzo")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #34. lenskart
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.lenskart.app' > clr ")
    print("lenskart")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #34. fastcleaner
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.cleaner.fastcleaner.booster.security.clean' ")
    time.sleep(5)
    execute_adb("adb shell input tap 500 590")
    time.sleep(4)
    #35. hdfc
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.snapwork.hdfc' > clr ")
    print("hdfc")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #36. axis mobile
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.axis.mobile'> clr ")
    print("axis mobile")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #37. icici.bank.imobile
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.csam.icici.bank.imobile' > clr")
    print("icici bank imobile")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #38. phonepe
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.phonepe.app' > clr ")
    print("phonepe")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #39. net.one97.paytm
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=net.one97.paytm' >clr ")
    print("Paytm")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #40. com.mobikwik_new
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.mobikwik_new' > clr ")
    print("mobikwik")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #41. com.myairtelapp
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.myairtelapp' > clr ")
    print("Airtel")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #42. com.Splitwise.SplitwiseMobile
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.Splitwise.SplitwiseMobile' > clr ")
    print("SplitwiseMobile")
    time.sleep(5)
    execute_adb("adb shell input tap 500 590")
    time.sleep(4)
    #43. in.mohalla.video&hl
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=in.mohalla.video&hl' > clr")
    print("Moj")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #44. sharechat
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=in.mohalla.sharechat' > clr ")
    print("Sharechat")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #45. josh
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.eterno.shortvideos' > clr ")
    print("Josh")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #46. twitter.android
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.twitter.android' > clr ")
    print("twitter")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #47. skype.raider
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.skype.raider' > clr ")
    print("skype")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #48. telegram
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=org.telegram.messenger' > clr ")
    print("telegram")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #49. com.whatsapp.w4b
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.whatsapp.w4b' > clr ")
    print("WA Business")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #50. com.application.zomato
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.application.zomato' > clr ")
    print("zomato")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #51. swiggy
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=in.swiggy.android' > clr ")
    print("swiggy")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #52. fitness
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.google.android.apps.fitness' > clr ")
    print("fitness")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)	
    #53. aarogyasetu
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=nic.goi.aarogyasetu' > clr ")
    print("aarogyasetu")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #54. heartratemonitor
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=heartratemonitor.heartrate.pulse.pulseapp' > clr ")
    print("heartratemonitor")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #55. com.bsbportal.music
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.bsbportal.music' > clr ")
    print("bsbportal music")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #56. spotify.music
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.spotify.music' >clr ")
    print("spotify music")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #57. com.radio.pocketfm
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.radio.pocketfm' > clr ")
    print("pocketfm")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #58. duolingo
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.duolingo' > clr ")
    print("duolingo")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #59. org.coursera.android
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=org.coursera.android' > clr ")
    print("coursera")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #60. unacademyapp
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.unacademyapp' > clr ")
    print("unacademyapp")
    time.sleep(5)
    execute_adb("adb shell input tap 500 590")
    time.sleep(4)
    #61. adda247
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.adda247.app' > clr ")
    print("adda247")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #62. Mast
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.mast.status.video.edit' > clr ")
    print("mast")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #63. com.playit.videoplayer
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.playit.videoplayer' > clr ")
    print("playit")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #64. com.mxtech.videoplayer.ad
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.mxtech.videoplayer.ad' > clr ")
    print("mxplayer")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #65. com.whereismytrain.android
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.whereismytrain.android' > clr ")
    print("whereismytrain")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #66. IRCTC
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=cris.org.in.prs.ima'> clr ")
    print("IRCTC Rail")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #67. com.ixigo.train.ixitrain
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.ixigo.train.ixitrain' > clr ")
    print("ixigotrain")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #68. goibibo
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.goibibo' > clr")
    print("goibibo")
    time.sleep(5)
    execute_adb("adb shell input tap 500 590")
    time.sleep(4)
    #69. com.agoda.mobile.consumer
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.agoda.mobile.consumer' > clr ")
    print("agoda mobile")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #70. makemytrip
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.makemytrip' > clr ")
    print("makemytrip")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #71. OLA
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.olacabs.customer' > clr ")
    print("OLA")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #72. ubercab
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.ubercab' > clr ")
    print("ubercab")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #73. Rapido
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.rapido.passenger' > clr ")
    print("Rapido")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #74. com.google.android.apps.nbu.paisa.user
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.google.android.apps.nbu.paisa.user' > clr ")
    print("Gpay")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #75. redbus
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=in.redbus.android' > clr")
    print("Redbus")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #76. youtube.kids
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.google.android.apps.youtube.kids' > clr ")
    print("youtube.kids")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #77. coloring.book.color.painting
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.rvappstudios.kids.coloring.book.color.painting' > clr ")
    print("coloring")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #78. mental.math.multiplication.trivia
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.oldduckgames.mental.math.multiplication.trivia' > clr ")
    print("mental math")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)	
    #79. com.apollo.patientapp
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.apollo.patientapp' > clr ")
    print("apollo")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #80. NetmedsMarketplace
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.NetmedsMarketplace.Netmeds' > clr ")
    print("NetmedsMarketplace")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #81. bbc.mobile.news.ww
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=bbc.mobile.news.ww' > clr ")
    print("BBC News")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #82. AajTak.headlines
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=in.AajTak.headlines' > clr ")
    print("Aaj Tak")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #83. com.ak.ta.dainikbhaskar.activity
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.ak.ta.dainikbhaskar.activity' > clr ")
    print("Dainikbhashar")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #84. com.instagram.lite
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.instagram.lite' > clr ")
    print("instagram lite")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #85. housing
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.locon.housing' > clr ")
    print("housing")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #86. nnacres.app
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.nnacres.app' > clr")
    print("nnacres")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #87. com.urbanclap.urbanclap
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.urbanclap.urbanclap' > clr ")
    print("urbanclap")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #88. naukriApp
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=naukriApp.appModules.login' > clr ")
    print("naukriApp")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #89. com.microsoft.bing
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.microsoft.bing' > clr ")
    print("microsoft bing")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #90 jioplay.tv
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.jio.jioplay.tv' > clr ")
    print("jioplay tv")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #91. hotstar
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=in.startv.hotstar' > clr ")
    print("hotstar")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #92. netflix.mediaclient
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.netflix.mediaclient' > clr ")
    print("Netflix")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #93. com.amazon.avod.thirdpartyclient
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.amazon.avod.thirdpartyclient' > clr ")
    print("Prime Video")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #94. myjio
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.jio.myjio' > clr ")
    print("myjio")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #95. jiochat
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.jiochat.jiochatapp' > clr ")
    print("jiochat")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #96. jio.cloud.drive
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=jio.cloud.drive' > clr")
    print("jio cloud drive")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #97. org.spaceapp.clean
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=org.spaceapp.clean' > clr ")
    print("spaceapp clean")
    time.sleep(5)
    execute_adb("adb shell input tap 500 610")
    time.sleep(2)
    #98. sonyliv
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.sonyliv' > clr ")
    print("sonyliv")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #99. ZEE5
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.graymatrix.did' > clr ")
    print("ZEE5")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #100 adobe.reader
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=om.adobe.reader' > clr ")
    print("adobe reader")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
    #101. PharmEasy
    execute_adb("adb shell am start -a android.intent.action.VIEW -d 'market://details?id=com.phonegap.rxpal' > clr ")
    print("PharmEasy")
    time.sleep(5)
    execute_adb("adb shell input tap 500 600")
    time.sleep(2)
adbUp()




