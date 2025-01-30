# {{character.name}}

<!-- markdownlint-disable-file MD013 -->
<!-- markdownlint-disable-file MD033 -->

<img src="{{character.image.0}}" alt="{{character.name}}" title="{{character.name}}" height="100px" />

## {{character.team |title}}

{% if character['thematic-flavor'] -%}
_{{ character['thematic-flavor'] }}_
{%- endif %}

## Ability

> {{character.ability}}

{%- if character.strengths or character.weaknesses %}

## Considerations

{%- endif %}

{%- if character.strengths %}

### Strengths

{%- for strength in character.strengths %}

- {{strength}}

{%- endfor %}

{%- endif %}

{%- if character.weaknesses %}

### Weaknesses

{%- for weakness in character.weaknesses %}

- {{weakness}}

{%- endfor %}

{%- endif %}

{% if character['example-plays'] -%}

## How It Plays

{% for playList in character['example-plays'] %}

## Example {{loop.index}}

{% for item in playList -%}
{%- set nightLabel = "Night %d:" % loop.index -%}

- {{ item |replace(nightLabel, '**%s**' % nightLabel) }}

{% endfor %}

{% endfor %}

{%- endif %}
