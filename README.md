# Skrypt do pobierania danych z Facebooka za pomocą Selenium

> **Link do nagrania ze szkolenia**: [https://www.youtube.com/live/VOwJSkBLwOs](https://www.youtube.com/live/VOwJSkBLwOs)

Poniżej znajduje się opis przykładowego skryptu w języku Python, który loguje się na konto Facebook i pobiera zawartość z różnych sekcji profilu (np. lista znajomych, informacje z sekcji „O mnie”, obserwowani, polubienia i inne). 

## 1. Opis działania

1. **Logowanie**  
   - Skrypt uruchamia przeglądarkę Chrome przy pomocy `webdriver.Chrome()`.
   - Następnie przechodzi na stronę logowania Facebooka i wypełnia pola **email** oraz **hasło**.
   - Po wysłaniu formularza i zalogowaniu się na konto, skrypt czeka 60 sekund, żeby użytkownik mógł ewentualnie potwierdzić logowanie lub przejść przez dodatkowe zabezpieczenia (np. dwuskładnikowe uwierzytelnianie).

2. **Przeglądanie stron**  
   - W kodzie zdefiniowana jest lista adresów URL, które odnoszą się do konkretnych sekcji na Facebooku (takich jak „O mnie”, „Zdjęcia”, „Znajomi” itp.).
   - Dla każdej pozycji na liście skrypt otwiera stronę, przewija ją do samego dołu, aby wczytać ukrytą zawartość (np. starsze posty).
   - Następnie pobiera tekst z danej strony i dopisuje go do pliku tekstowego `facebook_profile_data.txt`.

3. **Zapis do pliku**  
   - Dla każdej odwiedzonej strony w pliku wynikowym poprzedza pobrane dane nagłówkiem, np. `### Zawartość strony: https://... ###`.
   - Dzięki temu w wygodny sposób można później przejrzeć zawartość i odróżnić dane z poszczególnych sekcji.

4. **Zakończenie działania**  
   - Na koniec skrypt zamyka przeglądarkę (`driver.quit()`) i wyświetla komunikat, że dane zostały zapisane do wybranego pliku.

## 2. Wymagania i konfiguracja

- **Python 3.x**  
  Skrypt został przetestowany w środowisku Python 3.  
- **Selenium**  
  Niezbędne jest zainstalowanie biblioteki `selenium`.  
  ```bash
  pip install selenium
  ```
- **ChromeDriver**  
  Do obsługi przeglądarki Chrome potrzebny jest plik `chromedriver`, który należy pobrać ze strony [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/).  
  Następnie należy dodać go do zmiennych systemowych (PATH) lub umieścić w tym samym katalogu, co skrypt.

## 3. Użycie

1. **Ustaw dane logowania**  
   Wypełnij zmienne `facebook_login` oraz `facebook_password` odpowiednimi danymi.
   ```python
   facebook_login = "adres@e-mail.com"
   facebook_password = "haslo"
   ```
2. **Wskaż nazwę użytkownika**  
   Zmodyfikuj zmienną `profile_username` w taki sposób, aby odpowiadała interesującemu Cię profilowi.
   ```python
   profile_username = "zuck"
   ```
3. **Uruchom skrypt**  
   Przykładowo w terminalu/wierszu poleceń:
   ```bash
   python nazwa_skryptu.py
   ```
4. **Odbierz dane**  
   Po pomyślnej realizacji skryptu w katalogu skryptu pojawi się plik (domyślnie `facebook_profile_data.txt`), zawierający tekstową zawartość odwiedzonych podstron.

## 4. Struktura kodu

- **Importy**  
  Wykorzystujemy m.in. `selenium.webdriver`, `selenium.webdriver.common.by`, `selenium.webdriver.common.keys`, `time` oraz `WebDriverWait`.
- **Logowanie**  
  Pobieramy elementy formularza przy pomocy metody `EC.presence_of_element_located((By.NAME, "email"))` i wypełniamy je danymi.
- **Przewijanie strony**  
  Skrypt wykorzystuje JavaScript, aby przewinąć stronę do dołu, co umożliwia wczytanie dynamicznie ładowanych elementów.
- **Zapis danych**  
  Odczytujemy zawartość całej strony przez `driver.find_element(By.TAG_NAME, "body").text` i dopisujemy do pliku.

## 5. Możliwe rozszerzenia

- **Analiza danych**  
  Zamiast zapisywać czysty tekst, można go przetwarzać (np. filtrować określone sekcje czy słowa kluczowe).
- **Inne przeglądarki**  
  Zmieniając sterownik (np. `webdriver.Firefox()`), można użyć Firefoksa zamiast Chrome.
- **Obsługa CAPTCHy / dwuskładnikowego uwierzytelniania**  
  W razie potrzeby można wzmocnić skrypt o obsługę komunikatów czy weryfikacji 2FA, wprowadzając np. ręczny input (dla wartości kodu SMS) w trakcie logowania.

---

**Pamiętaj**: To jest przykładowy skrypt demonstracyjny do pokazywania możliwości automatyzacji przeglądarki i analizy profilu. Należy go używać wyłącznie zgodnie z obowiązującymi przepisami i regulaminem platformy.

---

### Autor
Skrypt omawiany jest podczas szkolenia z białego wywiadu, dostępnego pod linkiem na YouTube:  
[https://www.youtube.com/live/VOwJSkBLwOs](https://www.youtube.com/live/VOwJSkBLwOs)
