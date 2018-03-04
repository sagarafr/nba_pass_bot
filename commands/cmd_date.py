from commands import Command
import requests
import json
import datetime
from traceback import print_stack


@Command(pass_args=True)
def date(bot, update, args):
    if len(args) != 3:
        print("not good length")
        bot.sendMessage(chat_id=update.message.chat_id, text="Must have the following format: day month year")
        return
    else:
        try:
            datetime.date(int(args[2]), int(args[1]), int(args[0]))
        except:
            bot.sendMessage(chat_id=update.message.chat_id, text="Unable to get the page")
            return

        url = "http://stats.nba.com/stats/scoreboardV2"
        headers = {
            "Host": "stats.nba.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }

        params = {
            "DayOffset": "0",
            "LeagueID": "00",
            "gameDate": "{}/{}/{}".format(int(args[1]), int(args[0]), int(args[2][2:]))
        }

        try:
            response = requests.get(url=url, headers=headers, params=params, timeout=30)
            decoder = json.JSONDecoder()
            json_data = decoder.decode(response.text)

            for e in json_data["resultSets"]:
                if e["name"] == "LineScore":
                    row_set = e["rowSet"]
                    header = e["headers"]
                    info_to_recover = ["TEAM_NAME", "PTS_QTR1", "PTS_QTR2", "PTS_QTR3", "PTS_QTR4",
                                       "PTS_OT1", "PTS_OT2", "PTS_OT3", "PTS_OT4", "PTS_OT5", "PTS_OT6", "PTS_OT7",
                                       "PTS_OT8", "PTS_OT9", "PTS_OT10", "PTS"]
                    index_to_recover = [header.index(info) for info in info_to_recover]
                    game_id_index = header.index("GAME_ID")
                    results = {}

                    for element in row_set:
                        game_id = element[game_id_index]
                        tmp = [element[index_element] for index_element in index_to_recover]
                        if game_id not in results:
                            results[game_id] = []
                        results[game_id].append(tmp)

                    for _, value in results.items():
                        str_result = ""
                        if len(value) == 2:
                            team_one = value[0]
                            team_two = value[1]
                            str_result += "{0} vs {1} : {2} / {3}\n".format(team_one[0], team_two[0],
                                                                            team_one[-1], team_two[-1])
                            pts_team_one = team_one[1:-1]
                            pts_team_two = team_two[1:-1]
                            index_team_one = 1
                            index_team_two = 1
                            if 0 in pts_team_one:
                                index_team_one = pts_team_one.index(0)
                            if 0 in pts_team_two:
                                index_team_two = pts_team_two.index(0)
                            max_index = max(index_team_one, index_team_two)
                            # Add the different point and result
                            format_str = " ".join(["{:>4}" for _ in range(0, max_index + 1)]) + "\n"
                            str_result += format_str.format(*pts_team_one[:max_index], team_one[-1])
                            str_result += format_str.format(*pts_team_two[:max_index], team_two[-1])
                            bot.sendMessage(chat_id=update.message.chat_id, text=str_result)
        except Exception as exception:
            print(exception)
            print_stack()
            bot.sendMessage(chat_id=update.message.chat_id, text="Unable to get the page")
