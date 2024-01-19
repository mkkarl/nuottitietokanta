# Tietokantataulut

| Käyttäjät | Users | | |
|---|---|---|---|
| id | id | | |
| käyttäjänimi | username | | |
| salasana_hash | password_hash | | |

|Nuottikokoelma|???| | |
|---|---|---|---|
| id | id | | |
| nimi | name | | |
| tyyppi | type | | kirja, irtolehtikokoelma, sähköinen kokoelma |

|Nuotti|???| | |
|---|---|---|---|
| id | id | | |
| kokoelma_id | | | |
| nimi | name | | |
| säveltäjä | | | |
| sanoittaja | | | |
| sovitus | | | |
| tekijä | | | |
| esittäjä | | | |

| kokoelma_omistaja | | | |
|---|---|---|---|
| käyttäjä_id | user_id  | | |
| kokoelma_id | | | |

Kokoelmalla, esim. nuottikirjalla, voi olla useampi sama omistaja, jos kirjoja on useampi kopio.

| Nuottipyyntö | | | |
|---|---|---|---|
| pyytäjä_id | | | |
| omistaja_id | | | |
| laina | | boolean | true: lainapyyntö, false: kopiopyyntö |
| pyyntöaika | | | |
| nuottikokoelma_id | | | tyhjä, jos pyydetään yksittäistä nuottia |
| nuotti_id | | | tyhjä, jos pyydetään kokoelmaa |

| | | | |
|---|---|---|---|
| | | | |