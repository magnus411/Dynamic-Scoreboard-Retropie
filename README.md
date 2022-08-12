

# Dynamic-Scoreboard - Retropie

Arkadespill har en sjarm mange savner og alternativer som Retropi har blitt svært populert.

Etter en del oppmerksomhet rundt Retropie vår av kundene, tenkte jeg det hadde vært artig med en ukentlig/månedlig konkuranse i diverse arkade spill.

# Konsept
Jeg startet med Donky Kong 3. 



Kundene spiller et game med Donky Kong 3. Etter spillet skanner de en QR-kode på et ark ved Retropien. QR-Koden fører de til en nettside der highscore'en deres vises og de får mulighet til å inpute et navn.

Vi har en stor skjerm i lokalet med scoreboard-nettsiden i fullscreen. 
Etter brukeren har skrevet inn navnet sitt og trykket på "Send" på registrerings-siden, oppdateres scoreboardet seg automatisk i forhold til score value, med brukeren sin highscore.

# Repo

 - # V2 - RestAPI - Scoreboard NextJs
    ### (Ikke helt oppdatert enda)
    ### NextJS - Python - Flask_Restful - Firebase
    Flask app:

    - Flask-appen er et REST API som sender ut nyeste highscore verdi
    - Flask-appen ser etter endringer i en highscore.dat fil. Etter en endring er registrert, blir hex-tabellen loaded og highscoren til brukeren blir plukket ut og konvertert til UTF-8. Denne verdien blir så oppdatert som nyeste verdi

    Next-JS:
    - NextJS bruker API-et fra Flask-appen og drar inn nyeste highscore verdi og viser den på registerings siden.
    - Etter registering blir Firebase databasen oppdatert med nyeste verdi
    - Scoreboard siden blir dynamisk oppdatert med SWR

- # V1 - Old
    
    ### Python - Flask - SocketIo
    Score.py:
    - Score.py ser etter endringer i highscore.dat filen. Etter en endring er registert blir den nyeste verdien skrevet til en .csv fil.
    
    Flask app:
    - Når brukeren går inn på registerings siden via QR-Koden, blir den nyeste scoren pullet fra .csv filen
    - Etter brukeren har skevet inn navnet og trykket på Send, blir navnet og scoren lagret i en ny csv og en Reload() funsjon blir aktivert
    - Reload() funsjonen trigger en SocketIo emit til Scoreboard siden.
    - Emiten blir tatt i mot og aktiverer en funsjon som reloader Scoreboard-siden
    - Reloaden gjør at Scoreboard-siden drar inn .csv filen med oppdatert navn og score
    Ikke særlig effektivt, men fungerte. Dette var grunnlaget for å lage V2 
    
# Ops

Husk å endre path for highscore.dat.

# Run

python app.py - Kjører Flask serveren

npm run dev - start development server

npm run build - bygger production build

npm run start kjører den ferdigbygde production builden


# Sorry for bad commenting!



