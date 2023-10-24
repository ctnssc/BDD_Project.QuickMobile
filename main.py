#Terminal: pip install selenium
#Terminal: pip install behave (Pentru fisierele de tip feature)
#Settings - Plugins - Cucumber (Pentru recunoasterea limbajului gherkin)
#Settings - Plugins - Ini (Pentru fisierele de tip ini)
#Terminal: pip install behave-html-formatter (pentru raportul final)



'''
Pentru rularea testelor:
Din TERMINAL:  behave sau behave **/features/login.feature ( pentru un proiect mai
complex specificam direct calea fisierului freature.)

Pentru generarea rapoartelor:
Din TERMINAL:
behave **/features/login.feature -f behave_html_formatter:HTMLFormatter -o login.report.html
behave **/features/logout.feature -f behave_html_formatter:HTMLFormatter -o logout.report.html
behave **/features/infoupdate.feature -f behave_html_formatter:HTMLFormatter -o infoupdate.report.html



'''



