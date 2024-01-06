import os # :3

webhook_link = "https://discord.com/api/webhooks/1193209031263797258/HuGKB1508tiOhOUfcUjjVBhUa2j76S4RYHyepCmvlJo2-xA4cklXtciFB2Sub7ZNKAuJ" # replace this with your webhook link!

while True:
    try:
        import requests, uuid, threading, time

        break
    except Exception as e:
        modules_to_install = ["requests", "uuid"]

        for module_name in modules_to_install: # idk why im doing this.
            if module_name in str(e): # i need psychological help.
                os.system("pip install "+ module_name) # help. please.

headers = { 'authority': 'api.discord.gx.games', 'accept': '*/*', 'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/json', 'origin': 'https://www.opera.com', 'referer': 'https://www.opera.com/', 'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'user-agent': "" }
# headers in one line... oh my god please lord forgive mme 😭😭😭😭
url = "https://api.discord.gx.games/v1/direct-fulfillment"

def request_to_nitro() -> None:
    while True:
        try:
            json = {"partnerUserId": str(uuid.uuid4())}

            with requests.post(url, json=json, headers=headers, timeout=5) as response:
                if response.status_code == 200: # only 200 returns json!
                    free_nitro_token = response.json()["token"] # oh wow, that stinks!

                    if free_nitro_token:
                        content = "<https://discord.com/billing/partner-promotions/1180231712274387115/"+free_nitro_token+">"

                        print(f"[+] Generated working promo link! Sending to webhook.")
                        requests.post(webhook_link, json={"content": content})
                else:
                    print("[-] Oh wow! Didn't got 200 status code: " + response.status_code)
        except:
            # well idgaf about handling with errors, as long as this doesn't get 429, its fine.
            pass


def threads_function() -> None:
    try:
        number_of_threads : int = int(input("> amount of threads: ")) # wanted to do this colorful but fuck this
        threads_list = []

        for _ in range(number_of_threads):
            thread = threading.Thread(target=request_to_nitro)
            threads_list.append(thread)

        for thread in threads_list:
            thread.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            for thread in threads_list:
                thread.join()

    except Exception as e:
        if "invalid literal for int()" in str(e):
            input("Invalid symbols are in threads number. Press enter to exit programm.") # why im even doing this...
        
            exit(0)

if __name__ == "__main__":
    threads_function()
