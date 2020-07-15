XO+ - verzija sa botom

U ovom projektu predstavljen je novi oblik igrice XO koji umesto standardnog tipa sa 2 igraca i table 3x3, sadrzi 3 igraca(X, O, +) i tablu velicine 5x5.
Predstavili smo 2 slucaja ove igrice:

1) Igrac protiv dva bota
2) Dva igraca protiv bota

U obe verzije igrice je koriscen min-max algoritam. Na primeru XO-a svaki igrac ima mogucnost da pobedi, izgubi i izjednaci. U slucaju da neki od igraca narednim potezom moze da pobedi, igrac koji je na redu ce povuci najbolji potez da izjednaci, u suprotnom prvi igrac pobedjuje. Min-max algoritam pomaze u pronalasku najboljeg poteza gledanjem unazad do pocetka. U svakom koraku pretpostavljamo da je prvi igrac pokusao da maksimizuje sanse za pobedu odnosno da minizuje sanse za protivnikovu pobedu. 




Koriscene biblioteke:

- pygame
- numpy
- matplotlib
- torch

