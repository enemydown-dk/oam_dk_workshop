Til workshoppen den 23. januar 2018, skal du arbejde med programmeringssproget Python.
For at du kan komme godt fra start på dagen, bedes du læse denne guide igennem og installere
det software, du skal bruge på dagen.

På dagen er der sat 30 minutter af til installfest. Her installerer og konfigurerer vi Python og Atom i fælleskab.
Installfest er i tidsrummer 9:00 -> 9:30.

**BEMÆRK!** Hvis du *ikke* er lokaladministrator på din maskine, skal du have installeret programmerne hjemmefra. Primærk fokus skal lægges på Python og Atom. Atom udvidelser kan drille, såfremt man ikke er lokaladministrator - disse kan derfor udelades.

**BEMÆRK OGSÅ!** Du kan med fordel registrere din API-kode til Science Direct på forhånd. Den kan oprettes her: https://dev.elsevier.com/apikey/manage

<h2>PYTHON</h2>
For at kunne køre kode skrevet i Python, skal du have en såkaldt Python fortolker.
Du skal installere den nyeste version af python, som er version 3.6.3. Den kan hentes her: https://www.python.org/downloads/
Det er vigtigt at du kører nyeste version, da scripts er opdateret til denne udgave.
Følg den installations guide, der kommer med programmet. Du skal lave en standard installation,
men huske at sætte flueben ved: **add python to path**.

<h2>ATOM</h2>
For at skrive python skal du også bruge en text editor, vi anbefaler at bruge Atom det er en
gratis open source editor lavet af folkene bag GitHub. Atom kan hentes i sin nyeste version her: https://atom.io/

<h2>ATOM UDVIDELSER</h2>
Atom har en række udvidelser der gør det nemmere at skrive i python, hvis du i
menulinjen trykker på Atom -> "Install shell commands", kan du gøre det
væsenligt nemmere at installere disse udvidelser.
Efter man har gjort dette, kan du åbne terminal på macOS og Linux, eller kommandoprompten
på Windows (cmd) og indtaste disse kommandoer (copy and paste):

* apm install autocomplete-python
* apm install linter
* apm install linter-pylint
* pip install jedi
* pip install pylint

<h2>SCRIPTS</h2>
Herunder følger koden til de enkelte scripts vi bruger på workshoppen. Du skal ikke være fortrolig med tingene herunder.
Det er inkluderet til den meget nysgerrige deltager og som et sted, hvor du efter workshoppen kan se tilbage på koden. Under de enkelte
scripts er der linket direkte til nyeste version som kan hentes som køreklar Python kode.

<h3>oadoi.py</h3>
Scriptet er udviklet med det formål, at udtrække OA metadata fra ressourcen http://oadoi.org

Download her: https://github.com/enemydown-dk/oam_dk_workshop/blob/master/filer/oadoi.py

**Kode:**
```python
#!/usr/bin/env python3

"""OADOI lookup via DOI from .csv"""

import urllib.request
import urllib.error
import json
import csv

URL = 'https://api.oadoi.org/' #URL til API'et
MAIL = 'lajh@kb.dk' #angiv din e-mail her, påkrævet for at undgå blacklist.
FILE_NAME = 'ind.csv' #angiv filnavn på den fil der indeholder din DOI-liste.
JSON_NAME = 'json.txt' #angiv et filnavn på den fil, hvor du ønsker output.

def pull_data_api(url):
    """Udfører forespørgslen i API og returnerer evt. fejlkoder til terminal"""
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        write_json_2_csv(JSON_NAME, data)
        print(data)

    except urllib.error.HTTPError as _:
        print(_.reason)

def open_csv():
    """Åbner filen i variablen FILE_NAME og læser DOI en efter en + kalder pullDataAPI"""
    with open(FILE_NAME, newline='') as _:
        reader = csv.reader(_, delimiter=';')
        next(_)
        for row in reader:
            pull_data_api(URL + row[0] + '?email=' + MAIL)

def write_json_2_csv(json_name, data):
    """Open filen i variablen JSON_NAME i append format, og skriver herefter data"""
    with open(json_name, mode="a") as file:
        file.write(json.dumps(data))

def main():
    """main"""
    open_csv()

if __name__ == '__main__':
    main()
```

**Anvendelse:**
Scriptet accepterer input i form af en kommasepareret tekstfil indeholdende den liste af DOI'er, som vi ønsker at udtrække informationer omkring. Der skal også defineres en output fil. Input og output defineres i scriptets linje 12 og 13. Mail skal defineres ift. eventuel misbrug (undgå blacklisting), dette defineres i linje 11.
En videreudvikling med GUI (grafisk brugerinterface) kan hentes her: https://github.com/enemydown-dk/OaDoiMiner (dette er udenfor dette workshop, men kan inspirere til at arbejde videre).

***Kør scriptet med følgende kommando: python oadoi.py***

<h3>scidoi.py</h3>
Scriptet er udviklet med det formål, at udtrække OA data fra Science Direct med input i form af en kommasepareret DOI-liste.

Download her: https://github.com/enemydown-dk/oam_dk_workshop/blob/master/filer/scidoi.py

**Kode:**
```python
"""
Extracts OA metadata from Science Direct.
"""

import urllib.request
import urllib.error
import json
import csv

APIKEY = '64ca3ad5b69086dca1Ac2a9b9c8166cb' #indtast din APIkey fra Science Direct her (denne er fiktiv).
FILE_NAME = 'in.csv' #navn på inputfil her.
JSON_NAME = 'out.txt' #navn på output fil her.

def pull_data_api(url):
    """Opslag i Science Direct API"""
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        write_json_2_csv(JSON_NAME, data)
        print(data)

    except urllib.error.HTTPError as _:
        print(_.reason)

def open_csv():
    """Læser inputfilen i variablen FILE_NAME"""
    with open(FILE_NAME, newline='') as _:
        reader = csv.reader(_, delimiter=';')
        for row in reader:
            wos_url = "https://api.elsevier.com/content/article/doi/" \
            + row[0] + "?apiKey=" + APIKEY + "&httpAccept=application%2Fjson"
            pull_data_api(wos_url)

def write_json_2_csv(json_name, data):
    """Skriver datastrøm (json) til outputfilen i variablen JSON_NAME"""
    with open(json_name, mode="a") as file:
        file.write(json.dumps(data))

def main():
    """main"""
    open_csv()

if __name__ == '__main__':
    main()
```
**Anvendelse:**
Indsæt din API-kode fra Science Direct, og navngiv input og outputfilerne direkte i scriptet. Disse filer skal være tilstede i samme mappe som scriptet. Den ene fil in.txt (eller hvad du navngiver den til) skal indeholde din kommaseparerede DOI-liste, output.txt skal bare være en tom tekstfil. API-koden til Science Direct kan oprettes her: https://dev.elsevier.com/apikey/manage

***Kør scriptet med følgende kommando: python scidoi.py***

<h3>bibtex2csv.py</h3>
Scriptet er udviklet med det formål, at omsætte metadata udtrukket fra Web of Science (WoS) fra bibtex formatet til csv, som kan importeres direkte i et regneark. Med scriptet kan du udplukke de specifikke felter fra den fra WoS eksporterede bibtexfil. Vi har primært brugt scriptet til at udtrække informationer til brug for identifikation af corresponding author.

Download her: https://github.com/enemydown-dk/oam_dk_workshop/blob/master/filer/bibtex2csv.py

**Kode:**
```python
#!/usr/bin/env python3

"""
Python script that converts BibTeX
entries to CSV.
Input is via standard input.
Output is via standard output.
"""

from re import match
from re import search
from re import findall
from sys import stdin

ENTRIES = []
ENTRY = {}

#De enkelte elementer af den Bibtexstregn vi indlæser, klippes i stykker.
for line in stdin:
    if match('^@', line.strip()):
        if ENTRY != {}:
            ENTRIES.append(ENTRY)
            entry = {}
    elif match('url', line.strip()):
        value, = findall("\\s+", line)
        entry["url"] = value
    elif search('=', line.strip()):
        key, value = [v.strip(" {},\n") for v in line.split("=", 1)]
        entry[key] = value

#Listen ENTREES løbes igennem, alle værdier udskrives. Hvis elementet er tomt
#udskrives N/A (not avalible) på den tomme plads.
for entry in ENTRIES:
    try:
        issn = entry["ISSN"]
    except KeyError:
        issn = 'N/A'
    try:
        doi = entry["DOI"]
    except KeyError:
        doi = 'N/A'
    try:
        title = entry["Title"]
    except KeyError:
        title = 'N/A'
    try:
        oa = entry["OA"]
    except KeyError:
        oa = 'N/A'
    try:
        affiliation = entry["Affiliation"]
    except KeyError:
        affiliation = 'N/A'
    try:
        journal = entry["Journal"]
    except KeyError:
        journal = 'N/A'
    try:
        publisher = entry["Publisher"]
    except KeyError:
        publisher = 'N/A'
    try:
        funding = entry["Funding-acknowledgement"]
    except KeyError:
        funding = 'N/A'
    try:
        fundtext = entry["Funding-text"]
    except KeyError:
        fundtext = 'N/A'

    #Elementerne printes, såfremt vi specificerer stdout skrives til fil - ellers til skærm.
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}" \
    .format(issn, doi, title, oa, affiliation, journal, publisher, funding, fundtext))
```

**Anvendelse og tilføjelse af ekstra felter:**

* Konverter en enkelt BibTex fil (.bib) med kommandoen: python bibtex2csv.py < [.bib filnavn] > [output filnavn].
* Konverter mange BibTex filer (.bib) samtidig med kommandoen: python cat \*.bib | ./bibtex2csv > [output filnavn] (ikke Windows).

Tilføj ekstra felter som du vil have udtrukket fra Bibtex, ved at tilføje felter til programkoden i denne del:
```python
print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}" \
    .format(issn, doi, title, oa, affiliation, journal, publisher, funding, fundtext))
```
Bemærk! At såfremt du tilføjer eller fjerner et felt i linjen: .format(issn, doi, title, oa, affiliation, journal, publisher, funding, fundtext)), skal du også tilføje samme antal \t{} til linjen: print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}" + du skal tilføje en fejlhåndteringsblok eksempelvis:

```python
try:
    fundtext = entry["Funding-text"]
except KeyError:
    fundtext = 'N/A'
```

**Corresponding author og OA information fra WoS**

På DOI kan der fra WoS søges på 500 records ad gangen. Men hvordan laver du en liste med 500 DOI’er om til en søgestreng?
GUI'en accepterer DOI'er separeret med OR som input: 10.1111/1469-8676.12099 OR 10.1007/978-3-662-46081-8_9 OR 10.1016/j.entcs.2015.12.020 OR […]

Der er to metoder til at opbygge denne søgestreng. Du skal erstatte mellemrum efter hver DOI med et [OR] via en af disse metoder:
* Commandline (bash): sed 's/$/OR/' DOI_WoS.txt > new-DOI_WoS.txt (OBS: kræver linux)
* Excel: 1. kolonne med DOI’er; 2. kolonnne med blanktegn_or_blanktegn [ or ] og ctrl+c ind i en ny tekstfil.



<h2>VIDEREBEARBEJDNING AF DATA</h2>
Herunder kommer vi med en række anbefalinger af programmer, som du kan benytte til at arbejde videre med din data. Specielt er der fokus på at oprense data og samle dette i et samlet Excel regneark.

<h3>OPENREFINE</h3>
Vi anbefaler at du benytter programmer OpenRefine (http://openrefine.org/) til at arbejde med oprensning af data. Specielt scriptet oadoi.py er lidt råt i outputformatet, men da OpenRefine kan præsentere den store mængde af json-poster fra scriptet i skønneste orden, er der ikke brugt yderligere ressourcer på dette (det er evt. noget ud selv kan arbejde med).

<h3>EXCEL (LOPSLAG)</h3>
Vi har anvendt Microsoft Excel med funktionen LOPSLAG til at samle vores data i et samlet regneark. Der er andre programmer og andre måder at opbevare data på (database). Vi viser dog alligevel her, hvordan du hurtigt kan kombinere data via en nøgle (DOI).

Du lavet et LOPSLAG ved at skrive følgende i formellinjen i Excel: =LOPSLAG(

Hvis du er nybegynder i Excel, kan det være en fordel at trykke på indsæt funktion. Du skal derefter udfylde følgende elementer i vinduet.
1. Opslagsværdi - dette er den værdi du vil bruge som nøgle i kombineringen af de to regneark (fællesnøglen). Du skal finde værdien i dit primære regneark, dvs. det regneark du vil arbejde med fremadrettet. Vi anbefaler at benytte værdier som DOI som fællesnøglen.

2. Tabelmatrix - dette er det dataområde, du vil gennemsøge for opslagsværdien. Dette er det regneark, som du vil indhente data fra til primærkarket. Det er vigtigt at den værdi du vil søge står i kolonne A.

3. Kolonneindeks_nr - dette er angivelsen af hvilket kolonnenummer i sekundærarket, der indeholder den værdu du er interesseret i at overføre.

4. Lig_med - dette er en angivelse af, om Excel såfremt en værdi ikke findes skal forsøge at finde en tilstødende værdi. Dette skal i vores tilfælde være FALSK, da vi ikke ønsker tilnærmelser af DOI, men kun præcise matches.

Herunder et eksempel, hvor der skabes et match og overføres data fra et regneark til et andet. Vi matcher på DOI, som findes i kolonne 'E' i primær regnearket (DOI skal altid findes i kolonne A i det regneark vi matcher med, ellers virker det ikke). I tabelmatrix definerer vi hele det sekundære ark som vores søgested. Vi er interesseret i at overføre værdien i 4-kolonne, dette angiver vi med tallet '4'. Sidst angiver vi, at vi kun ønsker et præcist match mellem DOI i kolonne E og A, dette gøres ved at angive FALSK i feltet.

![LOPSLAG](/filer/LOPSLAG.png)
