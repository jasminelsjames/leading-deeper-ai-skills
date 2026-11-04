"""Check published arithmetic/lengths; does not establish grader correctness."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parent
results = json.loads((root / "results.json").read_text())
totals = {c: {"passed": 0, "total": 0, "casesMeetingAllChecks": 0, "cases": 0, "approximateWords": 0} for c in ("with_skill", "without_skill")}
for case in results["cases"]:
    for config, recorded in case["conditions"].items():
        grade = json.loads((root / recorded["grading"]).read_text())
        criteria = json.loads((root / Path(recorded["grading"]).parents[1] / "criteria.json").read_text())
        assert [x["text"] for x in grade["expectations"]] == criteria
        assert all(isinstance(x["passed"], bool) for x in grade["expectations"])
        passed = sum(x["passed"] for x in grade["expectations"])
        total = len(grade["expectations"])
        answer = (root / recorded["output"]).read_text()
        words = len(re.findall(r"[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*", answer))
        assert (passed, total, words) == (recorded["passed"], recorded["total"], recorded["approximateWords"])
        assert grade["summary"]["passed"] == passed and grade["summary"]["total"] == total
        tally = totals[config]
        tally["passed"] += passed
        tally["total"] += total
        tally["casesMeetingAllChecks"] += passed == total
        tally["cases"] += 1
        tally["approximateWords"] += words
assert totals == results["summary"]
print(json.dumps(totals, indent=2))
