# Tips, Tricks, And Reminders

## Validate Against JSON Schema

As per [https://code.visualstudio.com/docs/languages/json#\_json-schemas-and-settings](https://code.visualstudio.com/docs/languages/json#_json-schemas-and-settings):

```json
{
  "json.schemas": [
    {
      "fileMatch": ["**/homebrew.json", "**/homebrew-template.json"],
      "url": "https://raw.githubusercontent.com/ThePandemoniumInstitute/botc-release/main/script-schema.json"
    }
  ]
}
```

## Base URLS

Assuming this is still a `chizmw` hosted Github project then URLs should look
something like:

```text
https://raw.githubusercontent.com/chizmw/botc-homebrew-slay-bells-revisited/refs/heads/main/images/_logo.png
https://raw.githubusercontent.com/chizmw/botc-homebrew-slay-bells-revisited/refs/heads/main/images/_background.png
```

```text
https://raw.githubusercontent.com/chizmw/botc-homebrew-CHANGEME/refs/heads/main/images/townsfolk-01_G.png"
https://raw.githubusercontent.com/chizmw/botc-homebrew-CHANGEME/refs/heads/main/images/townsfolk-01_E.png"
```

## Guide To Numbering

### First Night

- 13.5: Minion Info
- 17.5: Demon Info

### Other Nights

General guide:

- 1 - 13: special early actions
- 13.5: Minion Info
- 17.5: Demon Info
- 20 - 29: demons
- 30 - 39: minions
- 40 - 59: passive good players
- 60 - 79: active good players
