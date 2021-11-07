# notex-cogs
Just personal cogs for the Glacier Modding server that are related to the Hitman video game

## crc32
Calculates a CRC32 hash from a given string which the Hitman game uses for localisation hashes

## hashdb
Looks up ResourceID hashes using the API provided by https://hitmandb.notex.app

## id
Generates a random contract ID that can be used in custom contract JSON files

## md5
Generates a MD5 hash from a given string and replaces the first two characters with zeroes while also cutting the hash off after 16 characters to match what the game uses

Example:
`5E12FFEC093C3B75B57245DC9B9A2AC8` becomes `0012FFEC093C3B75`