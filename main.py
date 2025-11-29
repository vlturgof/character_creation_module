from random import randint
from graphic_arts.start_game_banner import run_screensaver


DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 3)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__}, {self.BRIEF_DESC_CHAR_CLASS}'

    def attack(self):
        damage = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон, равный {damage}'

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} урона'

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'«{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}»')


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = ('Воитель — дерзкий воин ближнего боя. Сильный, '
                             'выносливый и отважный.')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = ('Маг — находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом.')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = ('Лекарь — могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов.')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30


def choice_char_class(char_name):
    game_classes = {
        'warrior': Warrior,
        'mage': Mage,
        'healer': Healer,
        }

    approve_choice = None

    while approve_choice != 'y':
        selected_class = input('Введите название класса Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes.get(selected_class)(char_name)
        print(char_class)
        approve_choice = input('Для подтверждения введите "y"')

    return char_class


def start_training(character):
    commands = {
        'attack': character.attack(),
        'defence': character.defence(),
        'special': character.special(),
    }
    print('Потренируйся управлять своими навыками.'
          'Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.'
          'Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while True:
        if cmd != 'skip':
            cmd = input('Введите команду: ')
            print(commands.get(cmd))
    return 'Тренировка окончена!'


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          f'Сейчас твоя выносливость — {DEFAULT_STAMINA}, атака — '
          f'{DEFAULT_ATTACK} и защита — {DEFAULT_DEFENCE}.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    player: str = choice_char_class(char_name)
    print(start_training(player))
