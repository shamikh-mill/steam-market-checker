import urllib, json, re, smtplib, time

url = [
    "http://steamcommunity.com/market/listings/730/USP-S%20%7C%20Caiman%20%28Minimal%20Wear%29",
    "http://steamcommunity.com/market/listings/730/P90%20%7C%20Trigon%20%28Field-Tested%29"
]
preferred_price = [
    3.6,
    2.3
]
item = []
while True:
    print "CHECKING PRICES"
    for i in xrange(len(url)):
        try:
            json_url = url[i].replace("http://steamcommunity.com/market/listings/730/", "http://steamcommunity.com/market/priceoverview/?country=DE&currency=1&appid=730&market_hash_name=" )

            response = urllib.urlopen(json_url)
            data = json.load(response)
        except:
            print "Oh no! We can't grab data D:"
        try:
            price = re.sub("[^0-9.]", "", data["lowest_price"])
        except:
            print "Couldn't numerify data :C\ndata"            
                
        if preferred_price >= price:
            item.append(i)
     
    if len(item) > 0:
        try:
            to = 'your-email@gmail.com'
            gmail_user = 'your-other0email@gmail.com'
            gmail_pwd = 'your-other-emails-pswd'
            smtpserver = smtplib.SMTP("smtp.gmail.com",587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo
            smtpserver.login(gmail_user, gmail_pwd)
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:You have items that have reached your preferred price!!! \n'
            msg = header + "\n"
            for i in xrange(len(item)):
                msg += "Link: " + url[item[i]] + "\nYour preferred price: $" + str(preferred_price[item[i]]) + "\n\n"
                print msg
            smtpserver.sendmail(gmail_user, to, msg)
            smtpserver.close()
        except:
            print "Uh oh, couldn't send email :/"
            
    time.sleep(120)
        

