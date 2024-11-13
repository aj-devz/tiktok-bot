from selenium import webdriver  # Assuming this is from selenium package
from os import system, name
import chromedriver_binary  # This ensures chromedriver is on PATH
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller

# Check if the current version of chromedriver exists; if not, download it automatically
chromedriver_autoinstaller.install()

def clear_terminal():
    if name == 'nt':
        _ = system('cls')
        system('title PROGRAM_NAME')  # Adjusted to ensure compatibility with Windows
    else:
        _ = system('clear')

clear_terminal()

print(pyfiglet.figlet_format("PROGRAM_NAME", font="slant"))
print("1. Option 1.\n2. Option 2.\n3. Option 3.\n4. Option 4.\n5. Credits.\n")

try:
    mode = int(input("Mode: "))
except ValueError:
    print("Invalid input. Please enter a number between 1 and 5.")
    exit()

if mode in [1, 2, 3, 4]:
    url = input("URL: ")

    start = time()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1024, 650)
    driver.get(url)

    metric1 = 0
    metric2 = 0
    metric3 = 0

    def beautify(arg):
        return format(arg, ',d').replace(',', '.')

    def update_title1():
        global metric1
        while True:
            time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
            if name == 'nt':  # Update terminal title (only for Windows)
                system(f'title PROGRAM_NAME ^| Metric 1: {beautify(metric1)} ^| Elapsed Time: {time_elapsed}')
            sleep(1)  # Avoid high CPU usage

    def update_title2():
        global metric2
        while True:
            time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
            if
