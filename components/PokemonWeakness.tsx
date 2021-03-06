export const doubleDamage = { 
        'normal': [], 
        'fight': ['normal', 'rock', 'steel', 'ice', 'dark',],
        'flying': ['fight', 'bug', 'grass', ],
        'poison': ['grass'],
        'ground': ['poison', 'rock', 'steel', 'fire', 'electric'],
        'rock': ['flying', 'bug', 'fire', 'ice'],
        'bug': ['grass', 'psychic', 'dark'],
        'ghost': ['ghost', 'psychic'],
        'steel': ['rock', 'ice', 'fairy'],
        'fire': ['bug', 'steel', 'grass'],
        'water': ['ground', 'rock', 'fire'],
        'grass': ['ground', 'rock', 'water'],
        'electric': ['flying','water'],
        'psychic': ['fight', 'poison'],
        'ice': ['flying', 'ground', 'grass', 'dragon'],
        'dragon': ['dragon'],
        'dark': ['ghost', 'psychic'],
        'fairy': ['fight', 'dragon', 'dark'],
    }
export const halfDamage = {
        'normal': ['rock', 'steel'], 
        'fight': ['flying', 'poison', 'bug', 'psychic', 'fairy'],
        'flying': ['rock', 'steel', 'electric'],
        'poison': ['poison', 'ground', 'rock', 'ghost'],
        'ground': ['bug', 'grass'],
        'rock': ['fight', 'ground', 'steel'],
        'bug': ['fight', 'flying', 'poison', 'ghost', 'steel', 'fire', 'fairy'],
        'ghost': ['dark'],
        'steel': ['steel', 'fire', 'water', 'electric'],
        'fire': ['rock', 'fire', 'water', 'dragon'],
        'water': ['water', 'grass', 'dragon'],
        'grass': ['flying', 'poison', 'bug', 'steel', 'fire', 'grass', 'dragon'],
        'electric': ['grass', 'electric', 'dragon'],
        'psychic': ['steel', 'psychic'],
        'ice': ['steel', 'fire', 'water', 'ice'],
        'dragon': ['steel'],
        'dark': ['fight', 'dark', 'fairy'],
        'fairy': ['poison', 'steel', 'fire'],
    }
export const noDamage = {
        'normal': ['ghost'], 
        'fight': ['ghost'],
        'flying': [],
        'poison': ['steel'],
        'ground': ['flying'],
        'rock': [],
        'bug': [],
        'ghost': ['normal'],
        'steel': [],
        'fire': [],
        'water': [],
        'grass': [],
        'electric': ['ground'],
        'psychic': ['dark'],
        'ice': [],
        'dragon': ['fairy'],
        'dark': [],
        'fairy': [],
    }

}