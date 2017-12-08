Til workshoppen den 23. januar 2018, skal du arbejde med programmeringssproget Python.
For at du kan komme godt fra start på dagen, bedes du læse denne guide igennem og installere
det software, du skal bruge på dagen.

På dagen er der sat 30 minutter af til installfest. Her installerer og konfigurerer vi Python og Atom i fælleskab.
Installfest er i tidsrummer 9:00 -> 9:30.

**BEMÆRK!** Hvis du *ikke* er lokaladministrator på din maskine, skal du have installeret programmerne hjemmefra. Primærk fokus skal lægges på Python og Atom. Atom udvidelser kan drille, såfremt man ikke er lokaladministrator - disse kan derfor udelades.

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

**bibtex2csv.py**
Scriptet er udviklet med det formål, at omsætte metadata udtrukket fra Web of Science (WoS) fra bibtex formatet til csv, som kan importeres direkte i et regneark. Med scriptet kan du udplukke de specifikke felter fra den fra WoS eksporterede bibtexfil.
```
*kode:*
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

  entries = []
  entry = {}

  for line in stdin:
      if match('^@', line.strip()):
          if entry != {}:
              entries.append(entry)
              entry = {}
      elif match('url', line.strip()):
          #value, = findall('\{(\S+)\}', line)
          value, = findall("\\s+", line)
          entry["url"] = value
      elif search('=', line.strip()):
          key, value = [v.strip(" {},\n") for v in line.split("=", 1)]
          entry[key] = value

  for entry in entries:
      doi = entry["DOI"]
      title = entry["Title"]
      oa = entry["OA"]
  print("{}\t{}\t{}".format(doi, title, oa))
```
*anvendelse:*
Howto convert & add fields to extract: Convert single BibTex file (.bib) with the command ./bibtex2csv.py < [.bib file] > [output file] Convert multiple BibTex files (.bib) with the command cat *.bib | ./bibtex2csv > [output file]

Add extra fields to extract by adding fields to the below code in main program. for entry in entries: doi = entry["DOI"] title = entry["Title"] oa = entry["OA"] -> new_variable = entry["name_from_bibtex_file"]

Add \t{} to line for as many new fields as you add -> print("{}\t{}\t{}".format(doi, title, oa))

