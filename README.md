# Język skryptowy lab1

### Pierwszy program

Rozpocznijmy od stworzenia krótkiego programu który wyświetla „Hello world!”. W Pythonie, użyjemy polecenia print do
wyświetlenia tekstu. Poniżej przedstawiono gotowy skrypt.
```Python
print('Hello world!')
```
Dla porównania poniżej przedstawiono program napisany w języku Java:
```Java
public class HelloWorld {

  public static void main(String[] args) {
    System.out.println("Hello, World");
  }
}
```
Jak widać program napisany w Javie wykonuje dokładnie tą samą czynność a jest dużo bardziej „skomplikowany”. Zatem
programowanie w Pythonie jest prostsze.
Proste operacje
Python ma zdolność do wykonywania obliczeń. Wprowadź obliczenia bezpośrednio do konsoli Pythona a ona zwróci odpowiedź.
```Python
>>> 2 + 2
4
>>> 5 - 2 + 4
7
>>> (-7 + 2) * (-4)
20
>>> 6/0
Traceback (most recent call last):
File "<pyshell#0>", line 1, in <module>
6/0
ZeroDivisionError: integer division or modulo by zero
```
> W Pythonie ostatnia linia komunikatu o błędzie informuje o rodzaju błędu:exclamation:

### Operatory
| Operator numeryczny | opis             |
|---------------------|------------------|
| x + y               | suma x oraz y    |
| x - y               | różnica x oraz y |
| x * y               | iloczyn x oraz y |
| x / y               | iloraz x oraz y  |
| x // y              | (zaokrąglony w dół) iloraz x oraz y  |
| x % y               | reszta z dzielenia x / y  |
| abs(x)              | wartość bezwzględna x  |
| divmod(x, y)        | para (x // y, x % y)  |
| pow(x, y)           | x do potęgi y  |
| x ** y              | x do potęgi y  |
| x += y              | x = x + 1        |
| x -= y              | x = x - 1        |
| x *= y              | x = x * 1        |
| x /= y              | x = x / 1        |

| Operator porównania | opis             |
|---------------------|------------------|
| x != y               | rózne    |
| x == y               | równe |
| x > y                | większe |
| x < y                | mniejsze  |
| x >= y               | większe lub równe  |
| x <= y               | mniejsze lub równe  |

Wiele innych języków ma specjalne operatory, takie jak "++" jako skrót dla "x += 1". Python ich nie ma.
### Operacje na łańcuchach znaków (stringach)
Przy „tworzeniu” skryptu wypisującego na ekran komunikat Hello world! tekst umieszczany był w pojedynczych apostrofach (’text’)
ten sam efekt otrzymamy również gdy napis zostanie zamknięty w cudzysłów (”text”). Gdy napis wymagał będzie użycia apostrofu
(np. He’s) wystarczy przed apostrofem postawić znak `\`. Wypróbuj przedstawione konstrukcje.
> Backslash może być również użyty przy tabulatorach, przejściu do następnej linii, dowolnych znakach Unicode i różnych innych rzeczy, których nie można w rzeczywisty sposób wydrukować.

Do konkatenacji służy operator `+` podczas łączenia łańcuchów znaków nie ma znaczenia czy zostały one utworzone w pojedynczym czy podwójnym cudzysłowie. Łańcuchy znaków można również pomnożyć przez liczbę całkowitą np. `”spam”*4` sprawdź jaki będzie wynik takiego działania. Przydatny może być również operator indeksowania który przedstawiono w poniższym skrypcie. Wykonaj go w środowisku Pythona i sprawdź rezultat.
```Python
a = "Welcome to Python's world!"
print(a[0])
print(a[0:7])
```
### Wprowadzanie danych
Przydatną funkcją jest możliwość wprowadzania danych przez użytkownika do tego służy instrukcja `input` i ma ona postać:
```Python
input("stosowny komunikat").
```
### Konwertowanie typów
Jest to zamiana zmiennej z jednego typu na zmienną innego typu np. `float(2)` zamieni liczbę całkowita na zmiennoprzecinkową.
### Zmienne
Zmienne odgrywają bardzo ważną rolę w większości języków programowania, a Python nie jest wyjątkiem. zmienna umożliwia
zapisanie wartości przez przypisanie jej do nazwy, którą można wykorzystać do odnoszenia się do wartości później w programie. Aby
przypisać zmienną, użyj jednego znaku równości.
```Python
>>> x = 7
>>> print(x)
7
>>> print(x + 3)
10
>>> print(x)
7
```
Zmienna może być ponownie przypisana tyle razy, ile chcesz, aby
zmienić ich wartość.
```Python
>>> x = 123
>>> print(x)
123
>>> x = "To jest napis"
>>> print(x + "!")
To jest napis!
```
>W Pythonie zmienne nie mają określonych typów, więc można przypisać łańcuch znaków do zmiennej, a później przypisać liczbę całkowitą do tej samej zmiennej

Obowiązują pewne ograniczenia dotyczące znaków, które mogą być używane w nazwach zmiennych Pythona. Dozwolone są tylko
litery, cyfry i podkreślenia. Ponadto nie mogą zaczynać się od liczb. Nieprzestrzeganie tych zasad powoduje błędy.
```Python
to_poprawna_nazwa_zmiennej = 7
123abc = 7
SyntaxError: invalid syntax
```
>Python to język programowania z uwzględnieniem wielkości liter. Tak więc, Lastname i lastname to dwie różne nazwy zmiennych w Pythonie.
Próba odniesienia do zmiennej, która nie została przypisana powoduje błąd. możesz użyć instrukcji del, aby usunąć zmienną, co oznacza, że odwołanie od nazwy do wartości zostanie usunięte, a próba użycia zmiennej spowoduje błąd. Usunięte zmienne mogą być ponownie przypisane do późniejszego stanu, tak jak zwykle.
```Python
>>> foo = "napis"
>>> foo
'napis'
>>> bar
NameError: name 'bar' is not defined
>>> del foo
>>> foo
NameError: name 'foo' is not defined
```
>Zmienne foo i bar są nazywane zmiennymi metasyntaktycznymi, co oznacza, że są one używane jako nazwy zastępcze w przykładowym kodzie, aby coś zademonstrować. Spam i eggs są kanonicznymi zmiennymi metasyntaktycznymi używanymi w Pythonie. Nawiązują one do słynnego skeczu Latającego Cyrku Monty Pythona
