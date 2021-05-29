from models.season import Season
from models.participant import Participant
import pdb
from models import player
from models import stadium
from models import team
from models.player import Player, Position
from models.team import Team
from models.league import League
from models.stadium import Stadium
from models.signing import Signing
from models.fixture import Fixture
from models.association import Football_Association
import repositories.signing_repo as signing_repo
import repositories.player_repo as player_repo
import repositories.team_repo as team_repo
import repositories.stadium_repo as stadium_repo
import repositories.association_repo as association_repo
import repositories.league_repo as league_repo
import repositories.participant_repo as participant_repo
import repositories.season_repo as season_repo
import repositories.fixture_repo as fixture_repo

sfpl = Football_Association('Scottish Professional Football League')
association_repo.save(sfpl)

scot_prem = League('Scottish Premiership', sfpl)
league_repo.save(scot_prem)
scot_league_two = League('Scottish League Two', sfpl)
league_repo.save(scot_league_two)

# for league in league_repo.select_by_association(sfpl):
#     print(league.get_name())

forthbank = Stadium('Forthbank Performance Sports Centre', 'Stirling', 3808)
stadium_repo.save(forthbank)
stirling_albion = Team('Stirling Albion FC', 1945, forthbank)
team_repo.save(stirling_albion)

andrew_ryan = Player('Ryan', 'Andrew', 7, 'FWD')
player_repo.save(andrew_ryan)
sign_ar_stirlingalbion = Signing(andrew_ryan, stirling_albion)
signing_repo.save(sign_ar_stirlingalbion)

blair_currie = Player('Blair', 'Currie', 1, 'GK')
player_repo.save(blair_currie)
sign_bc_stirlingalbion = Signing(blair_currie, stirling_albion)
signing_repo.save(sign_bc_stirlingalbion)

anfield = Stadium('Anfield', 'Liverpool', 53000)
stadium_repo.save(anfield)
liverpool = Team('Liverpool FC', 1892, anfield)
team_repo.save(liverpool)

alisson_becker = Player('Alisson', 'Becker', 1, 'GK')
player_repo.save(alisson_becker)
sign_ab_liverpool = Signing(alisson_becker, liverpool)
signing_repo.save(sign_ab_liverpool)

virgil_van_dijk = Player('Van Dijk', 'Virgil', 4, 'DEF')
player_repo.save(virgil_van_dijk)
sign_vvd_liverpool = Signing(virgil_van_dijk, liverpool, '2018-01-01')
signing_repo.save(sign_vvd_liverpool)

jc_arena = Stadium('Johan Cruyff Area', 'Amsterdam', 55500)
stadium_repo.save(jc_arena)
netherlands = Team("Netherlands National Football Team", 1905, jc_arena)
team_repo.save(netherlands)
sign_vvd_netherlands = Signing(virgil_van_dijk, netherlands)
signing_repo.save(sign_vvd_netherlands)


virgil_van_dijk.set_firstname('Big Virgil')
player_repo.update(virgil_van_dijk) # Outputs 'no results to fetch' to console but it is working..


san_siro = Stadium('San Siro Stadium', 'Milan', 80018)
stadium_repo.save(san_siro)
inter_milan = Team('Internazionale', 1908, san_siro)
team_repo.save(inter_milan)
ac_milan = Team('Associazione Calcio Milan', 1899, san_siro)
team_repo.save(ac_milan)

ochilview = Stadium("Ochilview Park", "Falkirk", 3746)
stadium_repo.save(ochilview)
stenhousemuir = Team("Stenhousemuir F.C.", 1884, ochilview)
team_repo.save(stenhousemuir)

sa_sl2 = Participant(scot_league_two, stirling_albion)
participant_repo.save(sa_sl2)
sm_sl2 = Participant(scot_league_two, stenhousemuir)
participant_repo.save(sm_sl2)

sl2_2021 = Season('2021/22', scot_league_two)
season_repo.save(sl2_2021)

sa_v_sm = Fixture(stirling_albion, stenhousemuir, sl2_2021)
fixture_repo.save(sa_v_sm)