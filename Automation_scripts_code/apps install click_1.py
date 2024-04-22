import uiautomator2 as ui2
import subprocess
import time

receiver_device_serial = "0123456789ABCDEF"
receiver_device = ui2.connect(receiver_device_serial)

def execute_adb(command):
    subprocess.call(command, shell=True)

def open_google_play():
    execute_adb("adb shell am start -n com.android.vending/com.google.android.finsky.activities.MainActivity")
    time.sleep(6)

def install_app(package_name):
    execute_adb(f"adb shell am start -a android.intent.action.VIEW -d 'market://details?id={package_name}' > clr")
    print(f"Installing {package_name}")
    time.sleep(5)
    receiver_device(description="Install").click()
    time.sleep(2)

apps_to_install = [
    "com.imangi.templerun",
    "com.imangi.templerun2",
    "com.kiloo.subwaysurf",
    "com.phonegap.rxpal",
    "com.ludia.jw2",
    "net.one97.paytm",
    "heartratemonitor.heartrate.pulse.pulseapp",
    
    "com.and.riseofthekings",
    "com.krafton.roadtovalorempires",
    "com.fingersoft.hillclimb",
    "com.oldduckgames.mental.math.multiplication.trivia",
    "com.ubercab",
    "com.fsn.nykaa",
    "com.nekki.shadowfight3",
    "com.easygames.race",
    "com.my.warface.online.fps.pvp.action.shooter",
    "com.gamedevltd.wwh",
    "com.nekki.shadowfightarena",
    "com.jio.jioplay.tv",
    "com.snapwork.hdfc",
    "com.goibibo",
    "com.mast.status.video.edit",
    "com.blitzteam.battleprime",
    "com.spotify.music",
    "com.kabam.marvelbattle",
    "com.dts.freefiremax",
    "in.AajTak.headlines",
    "com.rapido.passenger",
    "com.radio.pocketfm",
    "com.activision.callofduty.shooter",
    "com.urbanclap.urbanclap",
    "com.google.android.apps.fitness",
    "com.unacademyapp",
    "com.whatsapp.w4b",
    "com.eterno.shortvideos",
    "fc.admin.fcexpressadmin",
    "com.ludia.jurassicworld",
    "com.skype.raider",
    "com.twitter.android",
    "com.axlebolt.standoff2",
    "in.redbus.android",
    "com.apollo.patientapp",
    "in.amazon.mShop.android.shopping",
    "com.gamedevltd.modernstrike",
    "com.snapdeal.main",
    "com.hkfuliao.chamet",
    "com.github.uiautomator",
    "com.rvappstudios.kids.coloring.book.color.painting",
    "com.NetmedsMarketplace.Netmeds",
    "com.netflix.mediaclient",
    "com.imangi.templerun",
    "com.zeptoconsumerapp",
    "com.axis.mobile",
    "com.amazon.mp3",
    "com.imangi.templerun2",
    "com.agoda.mobile.consumer",
    "com.nnacres.app",
    "com.csam.icici.bank.imobile",
    "com.igg.android.lordsmobile",
    "com.locon.housing",
    "com.pubg.imobile",
    "com.bsbportal.music",
    "com.kiloo.subwaysurf",
    "com.mxtech.videoplayer.ad",
    "com.gameloft.android.ANMP.GloftA8HM",
    "com.whatsapp",
    "org.benchmark.demo",
    "com.duolingo",       
    "com.application.zomato",
    "com.madfingergames.legends",
    "com.phonepe.app",
    "flar2.devcheck",
    "com.codemasters.F1Mobile",
    "com.futuremark.pcmark.android.benchmark",
    "com.google.android.apps.youtube.kids",
    "in.startv.hotstar",
    "com.Splitwise.SplitwiseMobile",
    "com.instagram.lite",
    "com.zeptolab.ctr.ads",
    "com.ak.ta.dainikbhaskar.activity",
    "com.meesho.supply",
    "com.myntra.android",
    "in.mohalla.sharechat",
    "naukriApp.appModules.login",
    "com.dc.gok.google",
    "com.nekki.shadowfight",
    "bbc.mobile.news.ww",
    "nic.goi.aarogyasetu",
    "org.telegram.messenger",
    "in.swiggy.android",
    "com.whereismytrain.android",
    "com.biglime.cookingmadness",
    "com.byjus.thelearningapp.premium",
    "com.github.uiautomator.test",
    "com.ea.game.nfs14_row",
    "com.miraclegames.farlight84",
    "com.instagram.android"

    # Add more apps here
]

open_google_play()

for app in apps_to_install:
    install_app(app)

# Add more app installations as needed
