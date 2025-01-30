# Abilities

<!-- markdownlint-disable-file MD013 -->
<!-- markdownlint-disable-file MD033 -->

This is a summary of the characters and their abilities

{% for team in teams -%}

## {{ team |title }}

{%- set members = teams[team] -%}
{%- for member in members %}

### {{member.name}}

> {{ member.ability }}

{% set character_page = "Character%3A" + member.name |replace(" ", "-") %}
[(More Info)]({{character_page}})

{% endfor -%}

{%- endfor -%}
