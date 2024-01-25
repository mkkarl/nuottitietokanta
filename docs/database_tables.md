# Tietokantataulut

| Käyttäjät | Users | | |
|---|---|---|---|
| id | id | | |
| käyttäjänimi | username | | |
| salasana_hash | password_hash | | |

|Nuottikokoelma| Sheet_collection | | |
|---|---|---|---|
| id | id | | |
| nimi | name | | |
| tyyppi | type | | kirja, irtolehtikokoelma, sähköinen kokoelma |

|Nuotti|Sheet| | |
|---|---|---|---|
| id | id | | |
| kokoelma_id | collection_id | | |
| nimi | name | | |
| säveltäjä | composer | | |
| sanoittaja | writer | | |
| sovitus | arranger | | |
| tekijä | creator | | |
| esittäjä | artist | | |

| kokoelma_omistaja | collection_owner | | |
|---|---|---|---|
| käyttäjä_id | user_id  | | |
| kokoelma_id | collection_id | | |

Kokoelmalla, esim. nuottikirjalla, voi olla useampi sama omistaja, jos kirjoja on useampi kopio.

| Nuottipyyntö | | | |
|---|---|---|---|
| pyytäjä_id | inquirer_id | | |
| omistaja_id | owner_id | | |
| laina | loan | boolean | true: lainapyyntö, false: kopiopyyntö |
| pyyntöaika | inquiry_time | | |
| nuottikokoelma_id | collection_id | | tyhjä, jos pyydetään yksittäistä nuottia |
| nuotti_id | sheet_id | | tyhjä, jos pyydetään kokoelmaa |

| | | | |
|---|---|---|---|
| | | | |