# Improve a skill

Choose one problem and keep the change focused. In your PR, show the request, fictional or sanitized inputs, the relevant output and why the change helps.

1. Edit the relevant `skills/<id>/SKILL.md`.
2. Update its `catalog.json` entry or example if the inputs or output change.
3. Run `python3 scripts/validate_repository.py`.
4. Explain any behavior you tested and any checks you could not run.

Keep evidence, uncertainty and human decisions explicit. A skill must not silently expand tool access or authorize sending, publishing or recurring runs. Preserve useful learning when proposing automation.

Examples must contain no private workplace material. Claims of better quality or saved time need supporting evidence; label estimates and fictional calculations.

Repository checks validate structure and links. They do not establish that an AI output is correct. Include a representative before-and-after example when changing behavior.

By submitting a contribution, you agree to license it under this repository’s [MIT license](LICENSE).

An optional GitHub Actions template is in [.github/examples/validate-skills.yml](.github/examples/validate-skills.yml). Maintainers can enable it by copying it into `.github/workflows/` with an account that has workflow access.
