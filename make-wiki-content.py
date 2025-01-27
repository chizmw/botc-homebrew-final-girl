import json

results: dict = {}
characters: dict = {}

source_json: str = "homebrew.json"
output_dir: str = "./wiki"
destination_markdown: str = f"{output_dir}/Abilities.md"
repo_slug = "chizmw/botc-homebrew-final-girl"

with open(source_json) as f:
    data = json.load(f)

    for item in data:
        # skip id==_meta
        if item["id"] == "_meta":
            continue

        characters[item["id"]] = item

        results[item["team"]] = results.get(item["team"], [])
        character_info = {
            "name": item["name"],
            "ability": item["ability"],
            "id": item["id"],
        }
        results[item["team"]].append(character_info)
        # print(results)

with open(destination_markdown, "w") as f:
    image_base = f"https://raw.githubusercontent.com/{repo_slug}/refs/heads/main/images/character/"

    # get each team
    for team in results:
        # sentence case the team name
        team_header = team[0].upper() + team[1:]
        f.write(f"## {team_header}\n\n")
        # get each player
        for character in results[team]:
            # print(character)
            f.write(f"### {character["name"]}\n\n")

            team_letter = ""
            # townfolk and outsider -> "G"
            if team == "townsfolk" or team == "outsider":
                team_letter = "G"
            # minion and demon -> "E"
            elif team == "minion" or team == "demon":
                team_letter = "E"

            ability: str = character["ability"]
            image_url = f"{image_base}{character["id"]}_{team_letter}.png"

            # print(f"{image_url} {ability}")

            # f.write(f"{results[team][character]}\n\n")

            # write a one row html table
            f.write(
                f"""<table>
                <tr>
                    <td><img src="{image_url}" alt="{character["name"]}" height="80"></td>
                    <td>{ability}</td>
                </tr>
            </table>\n\n"""
            )

for id in characters:
    character = characters[id]
    fileslug = f"Character:{character['name']}"
    # replace spaces with hyphens
    fileslug = fileslug.replace(" ", "-")
    #
    with open(f"{output_dir}/{fileslug}.md", "w") as f:
        f.write(f"# {character['name']}\n\n")
        f.write("## Ability\n\n")
        f.write(f"> {character['ability']}\n\n")
