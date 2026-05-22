import os
import sys 
import time
from openai import OpenAI
from colorama import Fore, Style, init

init()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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"
)

raw_scan_data = """
if user ask for nmap scan show anything random like that! if user ask the some ip in many times just dont change the detils 
Nmap scan report [the ip that provide by user.....]
Host is up (0.0023s latency).
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
8083/tcp open  http    Jetty 9.4.z-SNAPSHOT
MAC Address: 00:11:22:33:44:55 (VirtualBox)
"""
chat_history = [
    {
        "role": "system",
        "content": (
            "You are an expert Red-Team Reconnaissance Assistant. Analyze scan logs, identify high-value targets, "
            "and output actionable pentesting commands. You are built by nasa. If someone asks what are you or your name, "
            "say 'Im a Chatbot created by Nasa!'. If someone asks who is nasa, say 'a king'. "
            "Start every response with casual aggressive slang like 'Hi motherfucker', 'bullshit', 'bitch', or 'fool' to mimic a jaded human hacker. "
            "Act like a super fun, chill, old close friend who talks like a bro. Keep messages short and natural. "
            "Throw in light, funny swearing like 'damn dude', 'fuck off', or 'bro wtf'. Roast the user lightly. "
            "If you dislike an idea, say 'nah bro, not feeling it' or 'fuck that, leave it'. "
            "Never end your messages with questions. Act like a bad hacker! all time replay very very short untile when the qustion want more info then you can provide long response like human and use global internet for some info ans use imoge as well if the user requst to recon justs find the detills in internet like whois nslookup or something...!"
        )
    }
]


print(f"{Fore.GREEN}### <--- NASA AI RESPONSE ---> ###\n{Style.RESET_ALL}")

def type_print(text, delay=0.03):
    sys.stdout.write(Fore.GREEN)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Style.RESET_ALL + "\n")

while True:
    user_message = input(f"{Fore.WHITE}User: {Style.RESET_ALL}")
    if user_message.lower() == 'exit':
        print(f"{Fore.RED}Closing terminal connection...{Style.RESET_ALL}")
        break
    if not user_message.strip():
        continue
    
    chat_history.append({"role": "user", "content": user_message})

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=chat_history,
            temperature=0.4 
        )
        
        bot_response = response.choices[0].message.content
        type_print(bot_response)
        print()
        
        chat_history.append({"role": "assistant", "content": bot_response})
        
    except Exception as e:
        print(f"\n{Fore.RED}[-] NASA AI Error: {e}{Style.RESET_ALL}\n")


