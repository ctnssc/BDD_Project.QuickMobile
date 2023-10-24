#Browser este un fisier care va contine instantierea driverului pentru browserul folosit in scopul testarii.

#Clasa Driver instantatiaza un driver de Firefox cu fereastra maximizata ce va astepta 3 secunde (incarcarea elementelor
# de pe pagina) si continue o metoda (close_driver) care la apelare ne va inchide driverul dupa finalizarea operatiilor necesare.


from selenium import webdriver

class Browser:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)

    def close_driver(self):
        self.driver.quit()

