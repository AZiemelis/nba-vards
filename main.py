from nba_api.stats.endpoints import scoreboardv2
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


def get_nba_games_data():
    with open('home.html', 'r') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', id='scoreboard')
    tbody = table.find('tbody')

    tbody.clear()


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

    i = 0
    while i < len(structured_data) - 1:
        new_row = soup.new_tag('tr')
        new_row.append(soup.new_tag('td'))
        new_row.append(soup.new_tag('td'))
        new_row.append(soup.new_tag('td'))
        new_row.find_all('td')[0].string = f"{structured_data[i]['TEAM_CITY_NAME']} {structured_data[i]['TEAM_NAME']}"
        new_row.find_all('td')[1].string = f"{structured_data[i]['PTS']}:{structured_data[i + 1]['PTS']}"
        new_row.find_all('td')[2].string = f"{structured_data[i + 1]['TEAM_CITY_NAME']} {structured_data[i + 1]['TEAM_NAME']}"
        tbody.append(new_row)

        i += 2

    with open('home.html', 'w') as file:
        file.write(str(soup))

if __name__ == "__main__":
    get_nba_games_data()
