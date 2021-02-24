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
