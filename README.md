# Messenger
Multithreaded client-server app for texting


1. Instrukcja uruchomienia:
     
  1. Projekt składa się z dwóch skrptów w języku Python, tj. server.py oraz client.py.
     Należy uruchomić oba z nich, poprzez wywołanie w linii poleceń komend "python server.py",
     a następnie "python client.py".
  2. Część serwerowa działa w sposób zupełnie automatyczny. W oknie klienta, po każdym uruchomieniu,
     należy najpierw podać nazwę użytkownika, która zostane przypisana w serwerze do danej instancji klienta.
  3. Następnie należy wybrać rozmówcę za pomocą komendy addr z ppkt. 5 instrukcji.
  4. Aplikacja jest gotowa od użytku.
     
  5. Aplikacja kliencka obsługuje kilka szczególnych poleceń, których użycie musi być poprzedzone znakiem "\".
     Są to:

        1. addr - służy do wybrania bądź zmiany aktualnego rozmówcy. Przyjmuje ona parametr będący nazwą użytkownika,
           z którym chcemy porozmawiać. Schemat całego polecenia to "\addr <NAZWA_UZYTKOWNIKA>", np. "\addr Alicja".
        2. curr - służy do wyświetlenia nazwy użytkownika aktualnego rozmówcy,
        3. quit - służy do zamknięcia programu

7. Lista wątków:

    1. Wątek odbierający wiadomości w części klienckiej - nasłuchuje wiadomości przychodzących ze strony serwerowej
    2. Wątek wysyłający wiadomości w części klienckiej -  pobiera dane tekstowe od użytkownika, odpowiada za
       przesyłanie danych do serwera oraz interpretuje polecenia z ppkt. trzeciego.
    3. Zmienna liczba wątków obsługujących komunikację ze stroną kliencką w części serwerowej - każdy z nich odpowiada
       zavkomunikację z jednym, konkretnym klientem zalogowanym do serwera, a także za zarządzanie kolejką wiadomości
       dla tego klienta przeznaczonych.

8. Problemy, których nie udało się, jak dotąd, rozwiązać:
   
    1. Opóźnione wyświetlanie przychodzących wiadomości w oknie klienta - Pomimo zastosowania osobnych wątków do
       wyświetlania oraz pobierania tekstu, nie udało się osiągnąć efektu odbierania wiadomości w czasie rzeczywistym.
       Pojawiają się one z opóźnieniem jednej wiadomości, tj. dopiero po zamknięciu się aktywnego pola pobierania tekstu.
    3. Niepoprawnie działająca obsługa polecenia quit po stronie klienta. Nie doprowadza ono do całkowitego zakończenia
       pracy klienta.
    4. Niewyświetlanie odebranych z serwera wiadomości przez klienta, jeśli nie jest wybrany rozmówca.

9. Potencjalne usprawnienia

    1. W przypadku braku wybranego rozmówcy, automatyczne ustawienie rozmówcy po stronie klienta, po otrzymaniu wiadomości
       od innego klienta.
    2. Dodanie GUI (co mogłoby potencjalnie rozwiązać problem z ppkt. 1 z pkt. 5)
    3. Po stronie serwera, archiwizowanie pewnej liczby wiadomości dla każdego klienta.
