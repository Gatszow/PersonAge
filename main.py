import datetime


time_now = datetime.datatime.now()
print(time_now.strftime())  # w nawiasach: %H - godziny w systemie 24 godzinnym
                            # %I - godziny w systemie 12 godzinnym; %p - AM/PM
                            # %M - minuty;    %d - dzień
                            # %m - miesiąc (liczba); %b - miesiąc słownie (skrócona wersja)
                            # %B - miesiąc słownie (pełna wersja); %Y - pełny rok
                            # Aby spolszczyć trzeba ustawić język programu
