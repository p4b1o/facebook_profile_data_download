from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Dane logowania i nazwa użytkownika
facebook_login = "adres@e-mail.com"
facebook_password = "SuperTajneHaslo"
profile_username = "zuck"  # Nazwa użytkownika do podmiany w linkach
output_file = "dane.txt"

# Linki do odwiedzenia
links = [
    f"https://www.facebook.com/{profile_username}",
    f"https://www.facebook.com/{profile_username}/about",
    f"https://www.facebook.com/{profile_username}/about?section=work",
    f"https://www.facebook.com/{profile_username}/about?section=education",
    f"https://www.facebook.com/{profile_username}/about?section=living",
    f"https://www.facebook.com/{profile_username}/about?section=contact-info",
    f"https://www.facebook.com/{profile_username}/about?section=basic-info",
    f"https://www.facebook.com/{profile_username}/about?section=relationship",
    f"https://www.facebook.com/{profile_username}/about?section=family",
    f"https://www.facebook.com/{profile_username}/about?section=bio",
    f"https://www.facebook.com/{profile_username}/about?section=year-overviews",
    f"https://www.facebook.com/{profile_username}/friends",
    f"https://www.facebook.com/{profile_username}/following",
    f"https://www.facebook.com/{profile_username}/photos",
    f"https://www.facebook.com/{profile_username}/photos_albums",
    f"https://www.facebook.com/{profile_username}/videos",
    f"https://www.facebook.com/{profile_username}/reels_tab",
    f"https://www.facebook.com/{profile_username}/places_visited",
    f"https://www.facebook.com/{profile_username}/map",
    f"https://www.facebook.com/{profile_username}/places_recent",
    f"https://www.facebook.com/{profile_username}/sports",
    f"https://www.facebook.com/{profile_username}/music",
    f"https://www.facebook.com/{profile_username}/movies",
    f"https://www.facebook.com/{profile_username}/tv",
    f"https://www.facebook.com/{profile_username}/books",
    f"https://www.facebook.com/{profile_username}/games",
    f"https://www.facebook.com/{profile_username}/likes",
    f"https://www.facebook.com/{profile_username}/events",
    f"https://www.facebook.com/{profile_username}/did_you_know",
    f"https://www.facebook.com/{profile_username}/reviews",
    f"https://www.facebook.com/{profile_username}/reviews_given",
    f"https://www.facebook.com/{profile_username}/reviews_written",
    f"https://www.facebook.com/{profile_username}/place_reviews_written",
    f"https://www.facebook.com/{profile_username}/notes"
]

# Inicjalizacja przeglądarki
driver = webdriver.Chrome()  # Upewnij się, że masz chromedriver w PATH
driver.get("https://www.facebook.com")
wait = WebDriverWait(driver, 10)

# Logowanie na Facebooka
wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(facebook_login)
driver.find_element(By.NAME, "pass").send_keys(facebook_password, Keys.RETURN)

# Poczekaj na zalogowanie
time.sleep(60)

# Otwórz plik do zapisu danych
with open(output_file, "w", encoding="utf-8") as file:
    for link in links:
        try:
            driver.get(link)
            time.sleep(3)  # Poczekaj na załadowanie strony
            
            # Przewijanie strony w dół
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)  # Poczekaj na załadowanie nowej zawartości
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            
            content = driver.find_element(By.TAG_NAME, "body").text
            file.write(f"### Zawartość strony: {link} ###\n")
            file.write(content + "\n\n")
        except Exception as e:
            print(f"Błąd podczas odwiedzania {link}: {e}")

# Zakończenie pracy
driver.quit()
print(f"Dane zapisane w pliku {output_file}")
