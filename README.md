# Ineractive-Scoreboard - Retropie

Arkadespill har en sjarm mange savner og alternativer som Retropi har blitt svært populert.

Etter en del oppmerksomhet rundt Retropie vår av kundene, tenkte jeg det hadde vært artig med en ukentlig/månedlig konkuranse i diverse arkade spill.

# Konsept
Jeg startet med Donky Kong 3. 



Kundene spiller et game med Donky Kong 3. Etter spillet skanner de en QR-kode på et ark ved Retropien. QR-Koden fører de til en nettside der highscore'en deres vises og de får mulighet til å inpute et navn.

Vi har en stor skjerm i lokalet med scoreboard-nettsiden i fullscreen. 
Etter kunden har skrevet inn navnet sitt og trykket på "Send" på registrerings-siden, oppdateres scoreboardet seg automatisk i forhold til score value, med kunden sin highscore.

# Repo

V2 - Versjon 2 består av en flask-app som 
# 1.
Ser etter endringer i en highscore.dat fil, og ##2. sender ut highscoren s
# 2.

ser etter endringer i en .dat highscorefil fra Retropien. Etter en endring er registrert blir hex-tabellen loaded og highscoren til kunden blir plukket ut og konvertert til UTF-8.
Denne verdien blir så oppdatert som nyeste verdi


#Ops

Husk å endre path for highscore.dat.



V1 - OLD
