import json

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(loader=PackageLoader("pyapp"), autoescape=select_autoescape())

results: dict = {}
characters: dict = {}

source_json: str = "homebrew.json"
extra_json: str = "extra.json"
output_dir: str = "./wiki"
destination_markdown: str = f"{output_dir}/Abilities.md"
repo_slug = "chizmw/botc-homebrew-final-girl"

with open(extra_json, "r") as f:
    extra_data = json.load(f)

with open(source_json, "r") as f:
    data = json.load(f)

    for item in data:
        # skip id==_meta
        if item["id"] == "_meta":
            continue

        characters[item["id"]] = item

        # if we have extra data for this character, use it
        if item["id"] in extra_data:
            item.update(extra_data[item["id"]])

        results[item["team"]] = results.get(item["team"], [])
        character_info = {
            "name": item["name"],
            "ability": item["ability"],
            "id": item["id"],
            "primary_image": item["image"][0],
        }
        results[item["team"]].append(character_info)
        # print(results)

template = env.get_template("abilities.jinja.md")
rendered = template.render(teams=results)
with open(destination_markdown, "w") as f:
    f.write(rendered)
    f.write("\n\n")

for id in characters:
    character = characters[id]
    fileslug = f"Character:{character['name']}"
    # replace spaces with hyphens
    fileslug = fileslug.replace(" ", "-")

    template = env.get_template("character.jinja.md")
    rendered = template.render(character=character)

    with open(f"{output_dir}/{fileslug}.md", "w") as f:
        f.write(rendered)
        f.write("\n\n")
