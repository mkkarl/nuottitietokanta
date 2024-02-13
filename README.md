# Nuottitietokanta

Tämä on Helsingin yliopiston kurssilla [Tietokannat ja web-ohjelmointi](https://hy-tsoha.github.io/materiaali/) toteutettava harjoitustyö.

Käyttäjä voi tallentaa nuottitietokantaan tiedot omistamistaan nuoteista ja nuottikirjoista. Tietokannasta voi etsiä, löytyykö omista tai muiden käyttäjien nuoteista haluttua kappaletta. Käyttäjä voi lähettää lainaus- tai kopiopyynnön nuoteista toiselle käyttäjälle.

## Tavoitteet

- [x] Käyttäjä voi luoda tunnuksen
- [x] Käyttäjä voi kirjautua

- [ ] Käyttäjä voi luoda nuottikokoelman
- [ ] Käyttäjä voi lisätä nuotin nuottikokoelmaan
- [ ] Käyttäjä voi lisätä useamman nuotin nuottikokoelmaan
- [ ] Käyttäjä voi selata nuotteja
- [ ] Käyttäjä voi selata nuottikokoelmia
- [ ] Käyttäjä voi hakea nuotteja
    - [ ] nimi
    - [ ] tekijätiedot
    - [ ] esittäjä
    - [ ] hakutuloksen voi rajata omistajan mukaan

- [ ] Käyttäjä voi pyytää nuottia lainaan
- [ ] Käyttäjä voi pyytää nuotista kopiota
- [ ] Käyttäjä voi pyytää nuottikokoelmaa lainaan

## Tietokantataulut

Tietokantataulut löytyvät [täältä](docs/database_tables.md).

## Käynnistysohjeet omalla tietokoneella

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```

Määritä vielä tietokannan skeema komennolla

```
$ psql < schema.sql
```

Nyt voit käynnistää sovelluksen komennolla

```
$ flask run
```