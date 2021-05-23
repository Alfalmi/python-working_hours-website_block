import time
from datetime import datetime as dt

# list of websites to block
website_list = ["www.facebook.com", 
                "facebook.com", 
                "mail.google.com",
                "www.youtube.com",
                "www.twitter.com"]

# define day working hours
from_hour = 9
to_hour = 17

# make a copy of your hosts, as a backup
host_path_windows = r"C:\Windows\System32\drivers\etc\hosts" # hosts file windows route 
host_path_unix = "etc\hosts"                                 # hosts file unix route

# host_dir = "hosts"
host_dir = host_path_windows

redirect = "127.0.0.1" # redirect site



# Main Loop
while True:
    if dt(dt.now().year,
          dt.now().month,
          dt.now().day, from_hour) < dt.now() < dt(dt.now().year,
                                                   dt.now().month,
                                                   dt.now().day, to_hour):
        print("Working hours...")
        with open(host_dir, 'r+') as file:   # open host file
            content = file.read()
            for website in website_list:  # for list of websites
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    # delete websites in fun hours
    else:  
        with open(host_dir, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours", dt.now(), dt(dt.now().year,
          dt.now().month,
          dt.now().day, from_hour))
    time.sleep(1)  #seconds
