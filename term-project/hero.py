import api
import os
def get_file_content():
    filepath = os.path.abspath(__file__)
    return open(filepath).read()

src_content = get_file_content()

def strategy():
    global src_content
    if get_file_content() != src_content:
        print("Hot Reload")
        os.execvp("python", ("python", __file__,))

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
