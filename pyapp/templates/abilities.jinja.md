# Abilities

<!-- markdownlint-disable-file MD013 -->
<!-- markdownlint-disable-file MD033 -->

This is a summary of the characters and their abilities

{%- for team in teams -%}

## {{ team |title }}

{%- set members = teams[team] -%}
{%- for member in members %}

### {{member.name}}

{%- set character_page = "Character%3A" + member.name |replace(" ", "-") %}
[(More Info)]({{character_page}})

#### {{ character_page }}

<table border="0" width="100%">
    <tr>
        <td><img src="{{member.primary_image}}" alt="{{member.name}}" height="80"></td>
        <td>{{member.ability}}</td>
    </tr>
</table>
{%- endfor -%}

{%- endfor -%}
