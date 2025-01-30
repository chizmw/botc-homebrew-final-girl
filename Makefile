.PHONY: all

all: generate-wiki commit-wiki commit-sidebar update-submodule-ref

generate-wiki:
	poetry run python ./make-wiki-content.py

commit-wiki:
	cd wiki && git add Character:*md Abilities.md && git commit -m "docs(Characters): update generated Character content"

commit-sidebar:
	cd wiki && github-wiki-sidebar --skip-credentials --silent && [ `git status --porcelain=1 _Sidebar.md | wc -l` -ne 0 ] && (git commit -m "docs(Sidebar): regererate sidebar" _Sidebar.md) || true

update-submodule-ref:
	git commit -vm "docs(wiki): update submodule reference" wiki
