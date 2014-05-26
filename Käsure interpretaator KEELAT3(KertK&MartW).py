#Programmi koostajad: Kert Kahu ja Mart Weber rühm 17, rühma nimi AT3.
#Programm valminud AKT aine raames Kevad 2014
#Programm võimaldab masinkeelele sarnast keelt kasutajal kirja panna ja seda hilisemalt ka interpreteerida
#Keele nimeks on AT3
#https://wiki.python.org/moin/CmdModule on moodul, mida kasutame.
#Funktsioonide koostamine käib käsuga "def do_Funktsiooninimi()", kus Funktsiooninimi on see, mida käsuna hiljem programmis kasutame.
#vastavad vajalikud funktsioonid ja toimimine on realiseeritud CmdModul'iga.

#Programmi tekstid on realiseeritud eesti keelsetena ja samuti edasi seda ka kood.
#NB! Välditud on funktsioonide ja nende väljakutsumisel täpitähti, et vältida kompileerumisest tulenevaid probleeme teistes arvutites.

#Programmi kodeering
# -*- coding: utf-8 -*-

#Soovitav on programmi kasutamiseks kasutada Python versiooni 3 ja uuemaid.
#Vanemate Pythoni versioonidega programm peaks töötama, kuid me ei taga Pythoni interpretaatorist tulenvate vigade korral programmi korrektset töötamist.

#Vajalikud moodulid, mida programm kasutab
from __future__ import print_function #vaja selleks, et ka vanemate pythoni programmi versioonidega print() korrektselt toimiks
import cmd #võimaldab kirjutada käsureal põhinevaid programme
import math #matemaatiliste arvutuste tegemiseks
import os #failide otsimiseks ja salvestamiseks 
import random #juhuliku arvu genereerimiseks
import re #võimaldab kasutada regulaaravaldisi
import sys #süsteemipõhine informatsioon

#programmi algus
#Esmalt defineerime kõikide funktsioonide kasutamise õpetuse, mida programmis koodi kirjutamiseks saab kasutada.

#Moodustame ABI meetodi jaoks sõnastiku, programmi võimalikud käsud ja nende kasutamine.
#Sõnastik ABI defineerimine. Proovime tekstid liigendada sobivalt, et käivitatud programmis oleks need ka loetavad. 
ABI = {}
ABI[''] = """
Järgnevalt kirjeldatud programm hõlmab
endas alljärgnevaid käske. Interpreteerimiseks
ja programmi elementaarseks kasutamiseks on
loodud keeles AT3 võimalus rakendada vastavaid
käske. Nende käskude kohta lisainformatsiooni
saamiseks tuleb kirjutada: ABI ULD
Vastav käsk räägib täpsemalt lahti
programmi võimalused koodi kirjutamiseks.

Elementaarsed käsud, mis on programmis realiseeritud:

LAHKU: Sulgeb käivitatud pythoni käsurea
interpretaatori keele AT3 jaoks.

KATALOOG: Näitab antud kataloogis olevaid
käivitamiseks võimalikke programme.
KATALOOG käsk otsib programme samast kaustast,
kus ta ise käivitatud on.
Ei saa muuta, et mujalt otsida.

SILUMINE: Käsu kasutamisel kuvatakse programmi
täitmisel rea numbreid ja muutujate väärtustamist.
Saab aimu, kuidas interpretaator programmi täidab.
Lihtsam otsida programmist vigu.

ABI: väljatab vastavad võimalused käskude kohta,
mida programm võimaldab kasutada.
Kasulik ja lausa soovitav
lugeda esmakordselt programmi kasutamisel.

KUVA: Väljastab kõik programmis olevad read.
Koodi kirjutamisel kirjapandud ridade kuvamiseks
kasutada samuti KUVA käsku.

UUS: Võimaldab luua uusi programme.
Programmide ülekirjutamise vältimiseks
kontrolli, et sama nimega faili, mida
tekitada soovite veel loodud ei oleks.

KAIVITA: Käivitab laetud programmi.
Kontrollitakse programmi süntaksit ning
vigade avastamisel vastavalt reageeritakse.
Sõltuvalt, kas ollakse silumise
või mitte silumisrežiimis,
kuvatakse ka vigasid erinevalt.

MUUDA: Muudab olemasoleva programmi nime.
Failide ümbernimetamiseks kasutada. Laiend ei muutu
faili ümbernimetamisel. Jääb ikka .at3.

SILUMINEEI: Lülitab välja programmi täitmisel silumise.
Ei näidata detailselt programmi täitmist.
Vaikimisi silumine väljas.

LAE: Laeb programmimällu varem kirjutatud programmi.
Võimaldab uuesti kasutada loodud programme ning
neid kasutada vastavalt soovile.

EEMALDA: Eemaldab laetud programmi programmimälust
ning lisaks kustutatakse ka faili sisu.
Fail jääb iseenesest kettale alles.
Saab kirjutada täiesti uue koodi faili,
ilma uut faili tekitamata. Tagasi võtta enam eemaldatud
faili sisu ei anna. Ole täpne käsu kasutamisel!

KUSTUTA: Kustutab laetud programmi failisüsteemist.
Tagasi võtta ei anna enam kustutatud faili.
Ole täpne käsu kasutamisel!

Programmeerimiseks mõeldud käskude kirja panemisel
kasutada alati esimese parameetrina rea numbrit.
Näiteks 1.
Rea numbrite järgi käib ka programmi täitmine.
Väiksem number enne ja siis järjest
kasvalt programmi kulg.
Lisainformatsiooni saamiseks mingi käsu
kohta trüki vastava käsu
nimi koos funktsiooniga ABI.
Kuvatakse informatsioon, kui
selline käsk eksisteerib. Muidu veateade.
Näiteks ABI LAHKU või ABI KATALOOG

"""

ABI['ULD']="""
Kõik programmi read, mida koodina kirja pannakse,
peavad algama rea numbriga. Iga rida programmis
peab olema eraldi real.
Ridasid täidetakse programmis vastavalt sellele,
mis on rea indeks. Programmi täitmine
hakkab reast, mille indeks kõige väiksem.
,,,.
Kasutada võib ka negatiivseid numbreid
nagu näiteks -1 jne. Erandina kasutatakse
teistsugust programmi täitmise loogikat,
kui kasutatakse käske: MINE, ALAM,
JÄRGMINE ning TAGASTA.
Täpsemalt loe juba vastava käsu infost.


Programmi rea kustutamiseks sisesta lihtsalt
vastava programmi rea number
ilma täiendavate parameetriteta
ning vajuta klaviatuuril ENTER klahvi,
vastava rea numbriga rida kustutakse programmist.
NB! Ära ilma asjata kustuta. Tagasi võtta ei saa.

Muutujad, mis defineeritakse programmi koodi
kirjutamisel peavad algama tähega
või alakriipsuga ja võivad sisaldada endas:
numbreid, tähti või alakriipse. Sõne muutujad
võiksid alata alakriipsuga koodi parema
lugemise tagamiseks (pole range nõue),
numbrilised muutujad alakriipsuga
alustamist ei vaja.

Programmi käsuloend
sisaldab endas järgnevaid käske:

ANDMED: Defineerib programmis kasutatavad
andmed.

FN: Defineerib funktsiooni, mida saab
hiljem kasutada/väljakutsuda.

MASSIIV: Defineerib massiivi.
Võimalik ka kahedimensioonalse
masiivi defineerimine.

LOPP: Tähendab programmi mingi lõigu lõppu,
alamprogrammi täitmine lõpetatakse LOPP käsuga.
Iga programm ja alamprogramm peab lõppema
LOPP käsuga.

FOR: Defineerib tsükli vastavalt
algus ja lõpp tingimusele.

ALAM: Suunatkse programmi täitmine ümber
alamprogrammile ja jäätakse meelde viimati
täidetud rea number.

MINE: Suunatakse täitama teist protsessi/koodrida.
Minnakse suunatud reale. Kasutatakse tingimuse juures.

TINGIMUS: Täidetakse, vastavalt kirja
pandud tingimusele

SISEND: Loetakse sisestatud andmed käsurealt.
Programmi andmete lugemiseks klaviatuurilt.

VAARTUSTA: Muutuja väärtustamine.

JARGMINE: Võetakse muutuja järgnev väärtus tsükli täitmisel.
Suurendatakse tsükli loendurit.

HUPPA: Programmi täitmine suunatakse vastavalt
sisestatud rea numbrile.

VALJASTA: Väljastatakse kasutajale soovitud informatsioon.

LOE: Loeb programmimällu käsuga ANDMED defineeritud andmed.

KOMMENTAAR: Saab vajadusel kirjutada programmi
paremaks mõistmiseks infot, mida programmi
täitmisel ei arvestata. Kuvatakse ainult programmi
teksti lugemisel, mitte täitmisel.

TAGASTA: Suunatakse programmi täitmine viimati
täidetud põhiprogrammi reale.

PEATA: Lõpetab programmi täitmise.

SALVESTA: Salvestab olemasoleva programmi.
Salvestakse samasse kataloogi, kus  programm käib.

LAE: Laeb programmimällu varem kirjutatud programmi.
Peab asuma samas kataloogis AT3 interpretaatoriga.

KAIVITA: Käivitab laetud programmi või
käivitab ka hektel kirjutamisel oleva programmi.

MUUDA: Muudab olemasoleva programmi nime.

EEMALDA: Eemaldab laetud programmi programmimälust.

KUSTUTA: Kustutab laetud programmi failisüsteemist.

SILUMINEEI: Lülitab välja programmi täitmisel silumise.

Lisainformatsiooni saamiseks, mingi kindla käsu kohta
kirjuta ABI ning vastava käsu nimi.
Näiteks: ABI ANDMED või ABI MUUDA.

Programmi funktsiooniloend,
sisaldab endas järgnevaid käske:

ABSOLUUT(X): Absoluutväärtus.
ARCUSTANGENS(X): Arkustangens
SONE(X): Konverteerib X sõneks.
KOOSINUS(X): Koosinus.
EKSPONENT(X): Eksponent
TAISARV(X): Konverteerib X-i täisarvuks.
LOGARITM(X): Naturaallogaritm.
JUHUSLIK(X): Juhuslik number.
SIINUS(X): Siinus
RUUTJUUR(X): Ruutjuur
TUHIK(X): Tühik
TANGENS(X): Tagens
KONVERTEERI(_X): konverteerib _X täisarvuks
ASCII koodi põhjal

Vaikimisi on kõik trigonomeetirlised funktsioonid
ootamas sisendina kraadides väärtust.
Antu programmi versioonis neid muuta ei saa.
Samuti on tagastava väärtus vastava funktsiooni
kasutamisel kraadides.
"""

#Käskude lahtikirjutamine ABI meetodi jaoks
#Kirjutame põhjalikult, kuidas mingit käsku kasutada ja milleks see mõeldud on.

 
ABI['ABI']="""
Abi saamiseks ABI käsu kohta.
Annab ülevaate, mida ABI käsuga programmis
teha on võimalik ja mis informatsiooni
pärida annab.
Kasutamine: ABI ABI
"""


ABI['LAHKU']="""
Sulgeb avatud programmeerimiskeele "AT3 keel"
programmi. Veendu alati,et salvestad enne
oma programmi, kui kasutad sulgemise käsku.
Salvestamiseks kasuta käsku: SALVESTA.
Kasutamine: LAHKU
"""

ABI['KATALOOG']="""
Käsk: KATALOOG. Näitab olemasolevast kataloogist
programme, mida on võimalik
avada. Kuvab kõiki faile, mis lõppevad faili
laiendiga .at3.
Kasutamine: KATALOOG
"""

ABI['PEATA']="""
Lõpetab olemasoleva programmi täitmise.
Kasutada käsku, kui mingi tingimuse
jõustumisel näiteks soovitakse programmi
töö lõpetada. Ülejäänud programmi töö peatatakse.
Kasutamine: rea number PEATA
"""

ABI['KUSTUTA']="""
KUSTUTA: Kustutab laetud programmi failisüsteemist.
Antud käsk kustutab varasemalt salvestatud
programmi. Programmi kood kui ka fail
kustutatakse täielikult arvuti kõvakettalt.
Lae progamm enne mällu ja siis kustuta.
Kasutamine: KUSTUTA
"""

ABI['EEMALDA']="""
EEMALDA: Eemaldab laetud programmi programmimälust.
Kustutab programmi koodi. Fail vastava
nimega jääb endiselt arvuti kettale,
kuid tühja failina.
Lae progamm enne mällu ja siis eemalda.
Kasutamine: EEMALDA
"""

ABI['KAIVITA']="""
KAIVITA: Käivitab laetud programmi.
Programmi interpreteerimiseks kasuta antud käsku.
Samuti varem kirjutatud koodijuppide interpretaatorile
kontrollimiseks andmiseks kasutada seda käsku.
Programm peab olema mälus. Kasuta LAE käsku.
Kasutamine: KAIVITA
"""

ABI['SALVESTA']="""
SALVESTA: Salvestab olemasoleva programmi.
Kasuta salvestamise käsku, et hiljem oma
kirjutatud programmikoodi avada ja kasutatada.
Salvesta oma koodi pidevalt, et vältida
programmide kadumaminemist.
Kasutamine: SALVESTA
"""

ABI['MUUDA']="""
MUUDA: Muudab olemasoleva programmi nime.
Kasuta seda käsku, kui soovid varem tehtud
programmi nime muuta.
Koopia tegemiseks antud failist
kasuta samuti antud käsku.
Kasutamine: MUUDA katse2
NB! katse2 on varasema faili uus nimi
"""

ABI['LAE']="""
LAE: Laeb programmimällu varem kirjutatud programmi.
Samuti seda käsku kasutades
ilma parameetrita viimati
lahti olnud programm.
Selle käsu kasutamisel suletakse antud hetkel
lahti olnud programm ilma salvestamata.
Kasuta lahti olevate programmide
salvestamiseks SALVESTA käsku.
Avatava programmi laadimisel on oluline
õige faili nimi, nii
nagu see on salvestatud arvuti kettal.
Faili mitteleidmisel kuvatakse veateade.
Kasutamine: LAE proov
proov on faili nimi. Kasuta ilma laiendita
"""

ABI['TAGASTA']="""
TAGASTA: Suunatakse programmi täitmine viimati
täidetud põhiprogrammi reale. Programmi täitmine
suunatakse seega reale, kus viimati kasutati
käsku ALAM ehk alamprogrammi põhiprogrammi sees.
Kasutamine: rea number TAGASTA
"""

ABI['KOMMETAAR']="""
KOMMENTAAR: Saab vajadusel kirjutada programmi
paremaks mõistmiseks infot,
mida programmi täitmisel ei arvestata.
Kasutamine: rea number KOMMETAAR see on kommetaar
"""

ABI['LOE']="""
LOE: Loeb programmimällu andmed. Andmed loetakse
vastavalt sellele, kuidas nad on kirja
pandud ANDMED käsuga programmi kirjutamisel.
ALATI peab rea number olema andmetel väiksem,
kui järgneval LOE käsul,
sest vastasel korral pole need käsule LOE nähtavad.
Kasutamine: rea number LOE MUUTUJA[arv]
"""

ABI['VALJASTA']="""
VALJASTA: Väljastatakse kasutajale soovitud informatsioon.
Programmi täitmise ajal 
mitmete muutujate või sõnede
väljatamiseks kasutatakse semikoolonit ;
Automaatselt pannakse iga muutuja järele tühik.
Kui VALJASTA käsu lõpus pole semikoolonit,
siis trükitakse ühele reale.
Kasutamine: rea number VALJASTA "Muutuja muutuja1 väärtus on"; X
"""

ABI['HUPPA']="""
HUPPA: Programmi täitmine suunatakse 
sisestatud rea numbrile.
Kasutamine: rea number HUPPA muutuja1 MINE rea number,
rea number, rea number
"""

ABI['SILUMINEEI']="""
SILUMINEEI: Lülitab välja programmi täitmisel silumise.
Kasutamine: SILUMINEEI
"""

ABI['SILUMINE']="""
SILUMINE: Lülitab sisse silumise programmi täitmisel.
Näidatakse rea numbreid ja vastavate
muutujate väärtustamisi programmi käivitamisel.
Kasutamine: SILUMINE
"""

ABI['ANDMED']="""
ANDMED: Defineerib programmi andmed.
Komaga eraldatud andmed omistatakse LOE
käsuga muutujatele.
Väärtused, mille omistamine muutujatele
toimub, võivad olla:
täisarvud, ujukomaarvud või jutumärkide vahel
olevad sõned. ANDMED käsk peab programmis
olema enne LOE käsku.
Kasutamine: rea number ANDMED 1, 2, 3, 4, 5, 8, 10
"""

ABI['FN']="""
FN: Defineerib funktsiooni, mida saab hiljem
kasutada/väljakutsuda.
Funksiooni saab välja kutsuda erinevate
muutujate väärtustega.
Kasutamine: rea number FN ABSOLUUT(X)= X + X
"""

ABI['MASSIIV']="""
MASSIIV: Defineerib massiivi elementide jaoks.
Massiiv võib olla koodiliselt, kas
ühe- või kahedimensionaalne. Massiivi kirja-
panemiseks kasutada kandilisi sulge [ ].
Kandiliste sulgude sees on üks element.
Kahedimensionaalse massivi defineerimiseks
kahed kandilised sulud.
Kasutada erinevaid nimesid massiivide
ja mitte massiivide jaoks.
Sarnased nimed võivad tekitada vigasid
programmi täitmisel.
Mitut massiivi võib defineerida ühe
reaga eraldades komaga erinevad massiivid.
Kasutamine: rea number MASSIIV MASSIIV1[5], MASSIIV2[4][5]
"""

ABI['LOPP']="""
LOPP: Tähendab programmi mingi lõigu lõppu,
alamprogrammi täitmine lõpetatakse vastava
käsu leidmisel.
Interpretaator võib programmi käivitades
väljastada veateate, kui pole fikseeritud
programmi lõpp.
Kasutamine: rea number LOPP
"""

ABI['FOR']="""
FOR: Defineerib tsükli vastavalt etteantud indeksile.
Tsükli kasutamiseks on mitmeid erinevaid võimalusi.
Valikuga tsükkel sisaldab endas järgnevat:
FOR muutuja = number KUNI number1 SAMM number2.
Muutuja muutub vastavalt sammule.
Esimene parameeter number on algusväärtus tsüklile.
Teine parameeter number1 kuhuni tsükkel käib.
Kolmas parameeter number2 on see, mis lisatakse
juurde parameetrile number (ideksi suurendaja).
Muutuja suurendamine toimub, kui käsk JÄRGMINE
on jälle programselt läbitud.
Kasutamine: FOR MUUTUJA = 2 KUNI 5
"""

ABI['ALAM']="""
ALAM: Suunatakse programmi täitmine ümber alamprogrammile
ja jäätakse meelde viimati täidetud põhiprogrammi rea number.
TAGASTA käsuga saab suunata siiski programmi
täitmise tagasi enda valitud reale.
Mitmed ALAM/TAGASTA käsud on võimalikud,
neid käsitletakse FIFO meetodina. Ehk viimane sisse,
esimene välja.
Kasutamine: rea number ALAM rea number
"""

ABI['MINE']="""
MINE: Programm suunatakse
vastavalt ette antud reale.
Kasutakse tingimuse järel.
Kasutamine: rea number MINE rea number
"""

ABI['TINGIMUS']="""
TINGIMUS: Täidetakse, kui tingimus kehtib.
Sisaldab kahte parameetrit. Tingimust ja rea numbrit,
kuhu tõese väärtuse korral minnakse.
Tingimuse kirja panemisel eraldatakse
tingimuse pooled kasuga SIIS.
Kasutamine: rea number TINGIMUS MUUTUJA[2] > MUUTUJA2 SIIS rea number
"""

ABI['SISEND']="""
SISEND: Loetakse sisestatud andmed käsurealt.
Loetud andmed omistatakse vastavale muutujale.
Kasutamine: rea number SISEND MUUTUJA
"""

ABI['VAARTUSTA']="""
VÄÄRTUSTA: Muutuja väärtustamine.
Kasutamine: rea number VÄÄRTUSTA MUUTUJA = 5 * MUUTUJA2
Kasutamine: MUUTUJA[2] = RUUTJUUR(MUUTUJA2 + MUUTUJA3) 
"""

ABI['UUS']="""
Uue programmi kirjutamise alustamiseks. Varsemalt lahti
olnud programm suletakse ning ei salvestata.
Salvestamiseks SALVESTA käsk. Käsk nõuab ka uue
faili loomiseks nime.
Kasutamine: UUS proov
"""

ABI['JARGMINE']="""
JARGMINE: Võetakse muutuja järgnev väärtus tsükli täitmisel.
Kasutada tsükli sammu väärtuse suurendamiseks.
Kasutamine: rea number JARGMINE muutuja
"""

ABI['FUNKSIOONILOEND']="""
Vastavate programmis defineeritud funksioonide
käitumine ja kasutamine on
sarnane kõigile üldlevinud programmeerimiskeeltele.
Täpsemalt, kui defineeritud ABI ULD käsus,
saab lugeda funktsiooni googeldades.
Seega selleks kasutada veebiaadressi: www.google.ee
ja otsi vastavat funktsiooni.
"""

#Klass interpretaatori realiseerimiseks keelele AT3
class KEELAT3(cmd.Cmd):
        #self, mis tähendab klassi ennast ja meetodi väljakutsumisel seda parameetrit ei kirjutata
        #järgnevalt realiseerime meetotid vastavate käskude jaoks, mida programmis kasutada saab.
        
        #regulaaravaldis: kahekordsete jutumärkide jaoks 
        
        #Klassi meetodid on:
        #keel_fn: funktsioonide käsitlemiseks
        #keel_massiiv: massiivide käsitlemiseks
        #regulaaravaldis topelt jutumärkide jaoks
        #kasutame meetodit compile(string, '', 'exec')
        
        #regulaaravaldise defineerimine
	regulaaravaldis = re.compile('("*?")"')
	#funktsioon FN
	def keel_fn(self, tail):
                #kasutame meetodit str.find(str, beg=0 end=len(string))
                #kasutame meetodit strip()
                #eraldame jupid
                #võetakse väärtus pärast võrdus märki
		fn_nimi, fn_parameeter1, fn_funktsioon = tail.partition('=')
		#otsitakse sulge
		fn_parameeter = fn_nimi[(fn_nimi.find('(')) + 1:fn_nimi.find(')')]
		fn_nimi = fn_nimi[:fn_nimi.find('(')].strip()
		
		#tekitame ja säilitame funktsiooni lambda
		funktsioon = 'lambda {}: {}'.format(fn_parameeter, fn_funktsioon)
		#eval võimaldab pythoni programmil käivitada programmi ise.
		self.muutujad[fn_nimi] = eval(funktsioon, self.muutujad)

	#funktsioon MASSIIV
	def keel_massiiv(self, tail):

		#eraldan jupid, mis komaga eraldatud
		for vaartus in tail.split(','):
			# eraldan jupid
			nimi = vaartus[:vaartus.find('[')].strip()
			#ühedimensionaalse masiivi jaoks
			massiiv1 = eval(vaartus[(vaartus.find('[') + 1):vaartus.find(']')], self.muutujad) + 1
			# kontrollime, kas edasi kahe dimensionaalne, kui jah teeme vastava massiivi, kui üle ühe kandilisi sulge siis järelikult kahe dimensionaalne.
			if vaartus.count('[') > 1:
                                #kahedimensionaalse masiivi jaoks
				massiiv2 = eval(vaartus[(vaartus.rfind('[') + 1):vaartus.rfind(']')], self.muutujad) + 1
				self.muutujad[nimi] = [[0] * massiiv2 for muutuja1 in range(massiiv1)]
			else:
				self.muutujad[nimi] = [0] * massiiv1

	#funktsioon FOR
	def keel_for(self, tail):
                #tagastan tsükli muutuja, muutuja lõpuväärtuse ja suurendaja väärtuse
		#otsitakse võrdusmärki
		nimi, muutuja1, ulatus = tail.partition('=')
		#tingimusega KUNI pannakse kirja ulatus tüsklil
		algus, muutuja1, lopp = ulatus.partition('KUNI')
		#kontrollin ka leidub argument SAMM, siis vastavalt sammule toimub tsükli korduv täitmine kuni parameetrini KUNI
		if 'SAMM' in lopp:
			lopp, muutuja1, samm = lopp.partition('SAMM')
		#kui SAMM pole defineeritud, siis vaikimisi üks
		else:
			samm = '1'
		#tsükli täitmine ja väärtust tagastamine
		#Tsükkel täidetakse vastavalt defineeritule.
		self.muutujad[nimi.strip()] = eval(algus, self.muutujad)
		return nimi.strip(), eval(lopp, self.muutujad), eval(samm, self.muutujad)


        #funktsioon TINGIMUS		
	def keel_tingimus(self, tail):
		#tagastatakse 0 kui tingimus on vale, kui õige siis MINE rea number
                #defineerime tingimused pythoni jaoks
		
		tail = tail.replace('JA', 'and')
		tail = tail.replace('VOI', 'or')
		tail = tail.replace('=', '==')
		#matemaatilised võrdused
		tail = tail.replace('!==', '!=')
		tail = tail.replace('>==', '>=')
		tail = tail.replace('<==', '<=')
		#TINGIMUS ja MINE
		tingimus, muutuja1, mine = tail.partition('SIIS')
		#lahendame tingimuse
		if eval(tingimus, self.muutujad):
			return int(mine)
		else:
			return 0

	#Funktsioon SISEND	
	def keel_sisend(self, tail):
		#sisend saamine
		tail = tail.strip()
		#otsitakse klaviatuurilt sisestatut
		self.muutujad[tail] = input()
		#mitte stringi korral korral tehakse muutuja väärtustamine
		if not tail.startswith('_'):
			self.muutujad[tail] = int(self.muutujad[tail])
			
	#funktsioon HUPPA
	def keel_huppa(self, tail):
		#eraldame käsu jupid
                #otsitakse käsku HUPPA
		vaartus, edasi, minevad = tail.partition('HUPPA')
		#listi indekseerimine -1 teistele indeksitele, et leida õige hüpe
		edasi_tekst = '[{}][{} - 1]'.format(minevad.strip(), vaartus.strip())
		return eval(edasi_tekst, self.muutujad)
	
	#funktsioon VALJASTA
	def keel_valjasta(self, tail):
		#jupid valjastamiseks sobilike parameetrite jaoks
                #eraldatud on semikooloniga parameeter ja tekst näiteks
		for grupp in tail.split(';'):
			if grupp:
				print(eval(grupp, self.muutujad), end = ' ')
		#kontrollime lõppemist semikooloniga
		if tail.endswith(';'):
                        #väljastatakse semikooloni järel olev väärtus/parameeter
			print(' ', end = '')
		#kui semokoolonit pole, siis lihtsalt tekst või väärtus välja trükkida.
		else:
			print()
			
	#funktsioon kontrollimaks, kas iga rea alguses on number, kontrollitakse püstitatud programmeerimise reeglit, et täitmine käib vastavalt rea numbrile koodi iga rea ees.
	def default(self, line):
		#kui numbrit rea alguses pole, anname veateate
		#kontrollime, ka koodi rida on õige ülesehitusega
                
		try:
			#kontrollime protsessi
			if self.koodinimi:
				reanumber = int(line.split()[0])
				#kontrollime rea lisamist, kustutamist
				try:
					elementaar = line.split(None, 1)[1]
					self.programmikood[reanumber] = line.split(None, 1)[1]
				#oodatakse indekseerimise viga
				except IndexError:
					del self.programmikood[reanumber]
			#teade kui programmi pole alustatud, enne ei saa alustada koodi kirjutamist, kui uus fail tehtud
			else:
				print('\nPROGRAMMI POLE ALUSTATUD. KASUTAGE PALUN KÄSKU "UUS" JA RPOOVIGE UUESTI.\n')
		#kui käsku kasutatud valesti või pole rea alguses numbrit
		except ValueError:
			print('\nVIGA: TEGEMIST ON VALE KÄSUGA. KONTROLLIGE SISESTATUT.\n')


        #do funktsiooni ees tähendab, et saab väljakutsuda vastava funktsiooni nime järgi
	#ei pea eraldai defineerima käskusid ja siduma neid funktsioonidega
        
	#funktsioon LAHKU
	def do_LAHKU(self, line):
                #kui käsku kasutati väljastame true
                #suletakse programm, kõik eelenev, mis salvestamata kaob
		return True

	#funktsioon KATALOOG
	def do_KATALOOG(self, line):

		#kuvame võimalikud programmid, mida saab interpreteerida
                #otsitakse siis faile laiendiga .at3
		programmid = [failinimi for failinimi in os.listdir() if failinimi.lower().endswith('.at3')]
		#Väljastame need, mis leiti antud kataloogist ja sobivad laiendiga
		if programmid:
			print()
			for programm in programmid:
                                #Kuna kasutame igal pool suuri tähti (väike nõue programmi jaoks), siis ka väljatrükkimisel programmi nimi suurte tähtedega.
				print(programm[:-4].upper())
			print()
		else:
			print('\nÜHTEGI PROGRAMMI EI LEITUD.\n')

			
	#funktsioon SILUMINE		
	def do_SILUMINE(self, line):
                #Saab sisselülitada silumise programmi täitmisel
		self.silumine = True
		#kuvatakse programmi täitmise kulgu
		self.silumismuutujad = [sona.strip() for sona in line.split(',')]
		
        #funktsioon ABI
	def do_ABI(self, line):
                #vastavalt kasutaja abi funktsiooni päringule, väljastame päringu sisu
		if line.strip() in ABI:
                        #väljastatakse parameetri otsing
			print(ABI[line.strip()])
		#Kui sellist päringut pole, siis veateade
		else:
			print('\nANTUD PÄRINGU KOHTA VASTET EI LEITUD, KONTROLLI PÄRINGUT.\n')

	#funktsioon KUVA			
	def do_KUVA(self, line):
		#väljastatakse programmi read vastavalt ridade numbritele
		reanumbrid = sorted(self.programmikood.keys())
		#Väljastamine
		print()
		#vastavalt indeksile rea alguses trükkimine
		for reanumber in reanumbrid:
			print(reanumber, self.programmikood[reanumber])
		print()

	#funktsioon UUS		
	def do_UUS(self, line):
		#tehakse uus fail programmi kirjutamiseks samasse kataloogi, kus põhiprogramm
                #kontrollikse programmi nime parameetri olemasolemist
		if line.strip():
                        #tehakse uus fail, kuhu saab koodi kirjutama hakata. Sõnastik luuakse, mida saab hiljem salvestada
			self.programmikood = {}
			self.koodinimi = line.strip()
		else:
                        #Kui nimi puudu parameetri järel, siis viga
			print('\nVIGA:SISESTAGE PROGRAMMI NIMI FAILI KOOSTAMISEKS.\n')

	#funktsioon SILUMINEEI	
	def do_SILUMINEEI(self, line):
                #silumise režiim välja
                #programmi täitmist ei kuvata detailselt
		self.silumine = False

	#funktsioon varasemalt kirjutatud või saadud faili avamiseks
	def do_LAE(self, line):
        #varasemalt kirjutatud programmi laadimine
                
		try:
                        
                        #moodustakse sõnastik laetud programmist
			uuskood = {}
			#otsitakse laiendiga .at3 failist siis ridasid
			for koodirida in open(line.strip() + '.at3'):
				reanumber, tühik, programmikood = koodirida.partition(' ')
				uuskood[int(reanumber)] = programmikood.strip()
			self.programmikood = uuskood
			self.koodinimi = line.strip()
		except IOError:
                        #kui programmi ei ole, mida laadida tahetakse
			print('\nVIGA: PROGRAMMI LAADIMISEKS EI LEITUD {}.\n'.format(line.strip()))

	#funktsioon MUUDA			
	def do_MUUDA(self, line):
		#muuda olemasolevat programmi
		if line.strip() and self.koodinimi:
			self.koodinimi = line.strip()
		elif self.koodinimi:
                        #Uue nime sisetamine muudetavale programmile
			print('\nSISESTAGE PALUN UUS NIMI OLEMASOLEVALE PROGRAMMILE.\n')
		else:
                        #ei saa progammi ümber nimetada
			print('\nVIGA: POLE PROGRAMMI ÜMBERNIMETAMISEKS.\n')
			
	#funktsioon KAIVITA		
	def do_KAIVITA(self, line):
		
		#Käivitab ja interpreteerib programmimälus oleva koodi
                #hoiame muutujaid hilisemaks
		peamised_muutujad = self.muutujad.keys()
		#valmistame ette käsurea
		reanumbrid = sorted(self.programmikood.keys())
		viit = 0 #programmi rida täitmise jaoks. Vastavalt käiakse kõik read läbi viidale, mis võrdub ridada arvuga
		alamad = []
		tsüklid = {}
		andmed = []
		try:
			#tsükkel vastavalt koodiridadele
			while viit < len(reanumbrid):
				#kood tõlgitakse ümber pythonile mõistetavaks
				reanumber = reanumbrid[viit]
				käsurida, tail = self.ymbertolkimine(self.programmikood[reanumber])
				#kontrolli silumist, kui sees, siis detailne programmi läbimine
				if self.silumine:
					print(reanumber, end = ' ')
					for muutujake in self.silumismuutujad:
						if muutujake in self.muutujad:
							print(muutujake, '=', self.muutujad[muutujake], end = ' ')
					print()
				#otsitakse ridadest sobivust antud parameetritega, kui leiti, siis käitutakse vastavalt defineeritud käsule
				#käske täidetakse vastavalt sellele, kuidas programmi funktsioonides nende olemus kirja pandud
				if käsurida == 'ADNMED':
					andmed.extend(eval('[{}]'.format(tail)))
					
				elif käsurida == 'FN':
					self.keel_fn(tail)
					
				elif käsurida == 'MASSIIV':
					self.keel_massiiv(tail)
					
				elif käsurida == 'LOPP':
					break
				
				elif käsurida == 'FOR':
					nimi, piir, samm = self.keel_for(tail)
					tsüklid[nimi] = [piir, samm, viit]
					
				elif käsurida == 'ALAM':
					alamad.append(viit)
					viit = reanumbrid.index(int(tail)) - 1
					
				elif käsurida == 'MINE':
					viit = reanumbrid.index(int(tail)) - 1
					
				elif käsurida == 'TINGIMUS':
					mine = self.keel_tingimus(tail)
					if mine:
						viit = reanumbrid.index(mine) - 1
						
				elif käsurida == 'SISEND':
					self.keel_sisend(tail)
					
				elif käsurida == 'VAARTUSTA':
					exec(tail, self.muutujad)
					
				elif käsurida == 'JARGMINE':
					nimi = tail.strip()
					self.muutujad[nimi] += tsüklid[nimi][1]
					if tsüklid[nimi][1] > 0:
						loop = self.muutujad[nimi] <= tsüklid[nimi][0]
					else:
						loop = self.muutujad[nimi] >= tsüklid[nimi][0]
					if loop:
						viit = tsüklid[nimi][2]
					else:
						del tsüklid[nimi]
						
				elif käsurida == 'HUPPA':
					viit = reanumbrid.index(self.keel_huppa(tail)) - 1
					
				elif käsurida == 'VALJASTA':
					self.keel_valjasta(tail)
					
				elif käsurida == 'LOE':
					exec('{} = {}'.format(tail, andmed.pop(0)), self.muutujad)
					
				elif käsurida == 'KOMMENTAAR':
					pass
				
				elif käsurida == 'TAGASTA':
					viit = alamad.pop()
					
				elif käsurida == 'PEATA':
					break
				
				elif '=' in tail or '=' in käsurida:
					exec(self.programmikood[reanumber], self.muutujad)
					
				else:
					print('\nVIGA REAL: {}: VALE KÄSK: {}\n'.format(reanumber, käsurida))
					break
				
				viit += 1
				
		except Exception as err:
			if self.silumine:
				#täis veateade, kui on viga silumisrežiimi ajal
				sõnum = '\nINTERPRETAATORI VIGA REAL: {}/{}\n{}\n'
				print(sõnum.format(reanumber, sys.exc_info()[2].tb_lineno, err.args[0].upper()))
			else:
				#Antakse veatede vastava rea numbriga, kui ei ole silumisrežiimi
				print('\nINTERPRETAATORI VIGA REAL: {}\n'.format(reanumber))
		#puhasta programmi muutujad
		for muutujake in self.muutujad:
			if muutujake not in peamised_muutujad:
				del self.muutujad[muutujake]
		#väljastamine
		print()

	#Funktsioon SALVESTA
	def do_SALVESTA(self, line):

		#salvestamise meetod
		if self.koodinimi:
			#kirjutab koodiread faili
			reanumbrid = sorted(self.programmikood.keys())
			salvestamiseks = open(self.koodinimi + '.at3', 'w')
			#koodirida lisamine faili
			for reanumber in reanumbrid:
				reatekst = '{} {}\n'.format(reanumber, self.programmikood[reanumber])
				salvestamiseks.write(reatekst)
			print('\nPROGRAMM SALVESTATUD {}\n'.format(self.koodinimi.upper()))
		else:
                        #kui pole programmi salvestamiseks
			print('\nPOLE PROGRAMMI SALVESTAMISEKS\n')

	#Funktsioon EEMDALDAMINE		
	def do_EEMALDAMINE(self, line):
        #programmi sisu eemaldamine
		if self.koodinimi:
                        #kodu faili sisu eemaldatakse
			self.programmikood = {}
		else:
			print('\nVIGA: POLE PROGRAMMI EEAMALDAMISEKS\n')

	#funktsioon KUSTUTA		
	def do_KUSTUTA(self, line):

		#progammi kustutamine
		if self.koodinimi:
			try:
                                #kustutatakse fail laiendega .at3
				kustuta = self.koodinimi
				self.koodinimi = ''
				self.programmikood = {}
				os.remove('{}.at3'.format(kustuta))
				
			except OSError:
                                #kui antud programmil pole õigus teha muudatusi kettal
				print('\nVIGA: FAILI EI SAA KUSTUTADA, KONTROLLI ÕIGUSI\n')
		else:
			print('\nVIGA: PUUDUB FAIL KUSTUTAMISEKS\n')


	#Funktsioon ymbertolkimine		
	def ymbertolkimine(self, line):

		#programmi koodi ümbertõlkmine
                #programmi käsu saamine
		reakäsurida = line.split()[0].upper()
		try:
			#tükeldame programm
			alus = line.split(None, 1)[1]
			alus = self.regulaaravaldis.split(alus)
			#KÕIK SUURTÄHTEDEKS; Hoiame igal poole ühtalast programmi süntaksi
			reasaba = ''
			for tykk in alus:
				if tykk.startswith('"'):
					reasaba += tykk
				else:
					reasaba += tykk.upper()
		except IndexError:
			#tühik käskudele, kus puuduvad parameetrid
			reasaba = ''
		return reakäsurida, reasaba


        
        
        #Funktsioon preloop, mis käivitab loodud programmi
	def preloop(self):
                #paneme kirja esmalt kuvata kasutajale ja defineerime funktsiooniloendites kirja pandud funktsioonid
		self.programmikood = {}
		self.koodinimi = ''
		self.silumine = []
		#kuvatakse koguaeg rea alguses
		self.prompt = 'Keel AT3 >> '
		#meetodid, mille vastavad pythoni sisseehitatud funktsioonid, meie programmis defineeritud funktsiooniloendi funktsioonidega.
		self.muutujad = {'__builtins__': {}, 'ABSOLUUT': abs, 'ARCUSTANGENS': math.atan, 'SONE': chr, 'KOOSINUS': math.cos, 'EKSPONENT': math.exp, 'TAISARV': int, 'LOGARITM': math.log, 'KONVERTEERI': ord, 'JUHUSLIK': JUHUSLIK, 'SIINUS': math.sin, 'RUUTJUUR': math.sqrt, 'TUHIK': TUHIK, 'TANGENS': math.tan}




#Funktsioon JUHUSLIK
def JUHUSLIK(n):
        #Genereerime juhusliku ujukoma arvu 0-st kuni n-ni
	return random.random() * n

    
#Funktsioon TUHIK
def TUHIK(n):
        #Tekitame vastava arvu tühikuid
	return ' ' * n

#klassi isendi loomine klassile KEELAT3	
if __name__ == '__main__':
        #loome uue klassi isendi
	keelat3 = KEELAT3()
	#tevistus tekst programmi käivitamisel
	keelat3.cmdloop('Tere tulemast kasutama uut keelt AT3, mis võimaldab Teil \nhõlpsalt kirjutada madaltaseme keele programme. \nMugavat kasutamist! \nAutorid Kert Kahu ja Mart Weber\nTutvumiseks kasuta ABI käsku\n\nNB!Käsud peavad olema suurtähtedega kirjutatud\nPANE CAPS LOCK SISSE!\n')

