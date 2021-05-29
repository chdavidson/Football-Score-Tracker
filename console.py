import pdb
from models import player
from models.player import Player
from models.team import Team
from models.stadium import Stadium
import repositories.player_repo as player_repo
import repositories.team_repo as team_repo
import repositories.stadium_repo as stadium_repo

forthbank = Stadium('Forthbank Performance Sports Centre', 'Stirling', 3808)
stadium_repo.save(forthbank)
stirling_albion = Team('Stirling Albion FC', 1945, forthbank)
team_repo.save(stirling_albion)
andrew_ryan = Player('Ryan', 'Andrew', 7, 4, stirling_albion)
player_repo.save(andrew_ryan)
blair_currie = Player('Blair', 'Currie', 1, 1, stirling_albion)
player_repo.save(blair_currie)

anfield = Stadium('Anfield', 'Liverpool', 53000)
stadium_repo.save(anfield)
liverpool = Team('Liverpool FC', 1892, anfield)
team_repo.save(liverpool)
alisson_becker = Player('Alisson', 'Becker', 1, 1, liverpool)
player_repo.save(alisson_becker)
virgil_van_dijk = Player('Virgil', 'Van Dijk', 3, 2, liverpool)
player_repo.save(virgil_van_dijk)

