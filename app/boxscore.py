from nba_api.stats.endpoints import scoreboardv2
from datetime import datetime, timedelta

def get_yesterdays_games():
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    games = scoreboardv2.ScoreboardV2(game_date=yesterday_str)

    games_dict = games.get_dict()
    headers = games_dict['resultSets'][1]['headers']
    header_map = {header: index for index, header in enumerate(headers)}
    structured_data = [
        {header: row[header_map[header]] for header in headers}
        for row in games_dict['resultSets'][1]['rowSet']
    ]

    return structured_data