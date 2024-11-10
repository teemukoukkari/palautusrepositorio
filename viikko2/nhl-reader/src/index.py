from playerreader import PlayerReader
from playerstats import PlayerStats
from rich import print
from rich.prompt import Prompt
from rich.table import Table

def main():
    print("NHL statistics by nationality")
    
    seasons = [
        '2018-19',
        '2019-20',
        '2020-21',
        '2021-22',
        '2022-23',
        '2023-24',
        '2024-25'
    ]
    season = Prompt.ask("Select season", choices=seasons, default='2024-25')
    
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = stats.get_nationalities()

    while True:
        nationality = Prompt.ask(
            "\nSelect nationality",
            choices=nationalities,
            default='FIN'
        )
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(show_header=True)
        table.add_column('name')
        table.add_column('team')
        table.add_column('goals')
        table.add_column('assits')
        table.add_column('points')
        
        for player in players:
            table.add_row(
                f"[cyan]{player.name}[/cyan]",
                f"[purple]{player.team}[/purple]",
                f"[green]{player.goals}[/green]",
                f"[green]{player.assists}[/green]",
                f"[green]{player.points}[/green]"
            )
        
        print(f"          Top scorers of {nationality} season {season}")
        print(table)

if __name__ == "__main__":
    main()