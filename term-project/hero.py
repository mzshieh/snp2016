import api


def strategy():
    state = api.getState()
    myPos = api.getMyPosition()
    mySpeed = api.getMySpeed()
    enemyPos = api.getEnemyPosition()
    enemySpeed = api.getEnemySpeed()
    arenaR = api.getArenaRadius()
    gsensor = api.getGsensor()

    if state!='':
        # Win or lose
        print(state)

    return [-100, -100]


api.play('ws://snp2016.nctu.me:8080/ws', 'yourname', strategy)
