
class Character(object):
    '''Gracz'''
    def blast(self, enemy):
        print("Twoje strzały dosięgły przeciwnika:")
        enemy.die()

class Creatures(object):
    def die(self):
        print("Zostałem trafiony - umieram")

player = Character()

monster = Creatures()

player.blast(monster)