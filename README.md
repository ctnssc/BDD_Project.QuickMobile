# BDD Testing: QuickMobile.ro
***Quickmobile.ro** este un site web ce comercializeaza (exclusiv prin magazinul online) atat in Romania cat si in Europa, produse electronice de la peste 150 de branduri de IT&C.*

Testarea automata reprezinta o testare dinamica si analitica a unui produs software, care presupune utilizarea unui program pentru executarea procedurilor (test case) sau a întregilor scenarii de testare. Are scopul de a rula teste repetitive sau customizabile pentru o varietate mare de aplicatii cu o interventie umana minima. Avantajele unei astfel de testari sunt: eficienta, precizie, reutilizare si scalabilitate.

In cadrul acestui proiect am utilizat limbajul de programare Python, IDEul (Integrated Development Environment) folosit este PyCharm iar librariile folosite sunt Selenium si Behave. 

  PyCharm este un IDE dezvoltat de JetBrains, compania din spatele IntelliJ IDEA cu scopul de a oferi un IDE simplu, dar puternic, care ar face codarea mult mai ușoară pentru dezvoltatorii ce folosesc ca limbaj de programare Python.
  
  Python este un limbaj de programare dinamic, de nivel înalt, ce pune accent pe expresivitatea și înțelegerea ușoară a codului. Limbajul facilitează mai multe paradigme de programare, în special paradigma imperativa (C) și pe cea orientată pe obiecte (Java). 
  
  Libraria Selenium este o suita de tooluri si librarii open-source folosita pentru browser atuomation. Selenium permite userilor sa testeze functionalitatile siteurilor web pe diverse browsere.
  
  Metodologia folosita in acest proiect este BDD (Behavior-Driven Development), motiv pentru care am utilizat libraria Behave. BDD este un proces de dezvoltare software derivata din TDD care se bazeaza pe o atentie mai mare asupra scenariilor de testare.  Desi activitatile din suita BDD sunt similare cu cele din suita TDD, ele au un avantaj prin faptul ca adauga peste codul de testare automata fisierele descriptive ale scenariilor de business care sunt scrise intr-un limbaj pe care sa il inteleaga si utilizatorii ce nu au cunostinte tehnice. Acestea se numesc feature files si sunt primele fisiere care se creeaza in procesul de BDD, iar tot ce va fi creat ulterior va fi pentru a valida testele descrise in acest feature file.
  
  Gherkin este un limbaj descriptiv folosit in procesul de BDD pentru a putea implementa scenariile de business intr-un limbaj natural, scris intr-o engleza simpla astfel incat sa poata sa fie inteles de catre toate persoanele implicate. 
  
  Design patternul folosit este POM (Page Object Model), design folosit in general de metodologia BDD. Acesta a fost implementat pentru gruparea tuturor elementelor dintr-o pagina web intr-un singur fisiser python, astfel fiecare pagina web va avea ca si corespondent un singur fisier de python care va contine toate elementele dintr-o pagina web si respectiv toate actunile care se pot face pe acea pagina web.



# Structura Proiect:
In pregatirea proiectului am creat fisierul de ***requirements*** unde se regasesc numeroare librarii/pachete/pluginuri utile in crearea codului. Fisierele ***browser*** si ***environment*** au fost create pentru instantierea driverului browserului folosit in scopul testarii, respectiv definirea actiunilor ce vor fi facute inainte si dupa fiecare test executat.
Urmatorul pas a fost crearea folderului ***features***, folder ce contine atat cele trei fisiere de tipul ***.feature*** (specific BDD) ce reprezinta functionalitatile testate in cadrul proiectului scrise sub forma de scenarii in limbajul Gherkin, ***login.feature , logout.feature, infoupdate.feature*** cat si doua folderele, ***pages*** unde am construit logica din spatele testelor si folderul ***steps*** unde am creat pasii pentru executarea testelor conform scenarilor scrise.

Au fost definite 3 fisiere de tipul feature, ***infoupdate.featrure, login.feature, logout.feature*** fisiere in care se regasesc featurile tesate (login - 4 teste, logout -1 test si infoupdate - 1 test) si scenarii corespunzatoare testelor. Avand in vedere ca in cazul testarii feature-ului de login avem mai multe teste, am folosit tag-uri pentru fiecare test in parte pentru a avea posibilitatea de a rula un singur test. (***@invalid_credentials, @invalid_email, @invalid_password, @valid_credentials***).

In folderul ***pages*** am creat fisierul ***base_page*** pentru a nu fi nevoiti sa rescriem aceleasi functii/linii de cod in mai multe locuri astfel aparand cod redundant in aplicatie, si am definit toate actiunile de care avem nevoie in procesul de testare. In ***login_page*** si ***info_page*** am definit toate datele, caile si actiunile ce sunt necesare pentru a putea defini pasii de testare pentru login/logout, respectiv pentru actualizarea informatiilor personale din cadrul sectiunii contul meu, infromatii cont. Ambele fisiere mostenesc clasa ***BasePage*** ( creata in fisierul ***base_page*** ) iar prin intermediul parametrului ***self*** putem apela metodele deja definite. Pentru a respecta in tocmai principiile design patternului POM am ales sa integrez datele si pathurile obiectelor testate in fisierele in care se regaseau, chiar daca din punct de vedere al claritatii codului ar fi fost mai potrivita definirea acestora intr-un fisier separat cu clasele aferente.

In cadrul folderului ***steps*** am creat doua fisiere de tipul step definition file, ***infoupdate_steps*** si ***login_steps***, ce ajuta la implementarea tehnica  a scenariilor descrise in feature file. Cu ajutorul parametrului ***context*** putem accesa metode si instantia obiecte definite in folderul ***pages***.

Dupa executarea cu succes a tuturor testelor am generat cate un raport pentru fiecare feature in parte: ***infoupdate.report.html, login.report.html, logout.report.html***. Modul de generare al acestora se face in terminal cu ajutorul comenzii: ***behave **/features/login.feature -f behave_html_formatter:HTMLFormatter -o login.report.html*** si poate fi accesat din browser datorita parametrului ***"-o"***.
