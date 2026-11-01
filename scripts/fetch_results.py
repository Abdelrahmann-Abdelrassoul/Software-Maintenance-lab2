"""Pull SonarQube results for project 'flasky' into results/ (stdlib only)."""
import base64, json, os, sys, time, urllib.error, urllib.parse, urllib.request

URL = os.environ.get("SONAR_URL", "http://localhost:9000")
AUTH = base64.b64encode(f"{os.environ['SONAR_TOKEN']}:".encode()).decode()
KEY = "flasky"
OUT = "results"
os.makedirs(OUT, exist_ok=True)


def api(path, **params):
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{URL}{path}?{q}", headers={"Authorization": f"Basic {AUTH}"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


# wait for background analysis task to finish
for _ in range(60):
    tasks = api("/api/ce/component", component=KEY)
    if not tasks.get("queue") and tasks.get("current", {}).get("status") == "SUCCESS":
        break
    time.sleep(5)
else:
    sys.exit("analysis did not finish")

metrics = ("ncloc,files,functions,classes,bugs,vulnerabilities,code_smells,security_hotspots,"
           "sqale_index,sqale_debt_ratio,sqale_rating,reliability_rating,security_rating,"
           "security_review_rating,duplicated_lines_density,duplicated_blocks,complexity,"
           "cognitive_complexity,coverage,alert_status")
measures = {m["metric"]: m.get("value") for m in
            api("/api/measures/component", component=KEY, metricKeys=metrics)["component"]["measures"]}

issues, page = [], 1
while True:
    r = api("/api/issues/search", componentKeys=KEY, ps=500, p=page, additionalFields="rules")
    issues += r["issues"]
    if page * 500 >= r["total"]:
        break
    page += 1

hotspots = []
for params in ({"project": KEY}, {"projectKey": KEY}):
    try:
        hotspots = api("/api/hotspots/search", ps=100, **params).get("hotspots", [])
        break
    except urllib.error.HTTPError as e:
        print("hotspots", params, e.code, e.read()[:300])

json.dump({"measures": measures, "issues": issues, "hotspots": hotspots},
          open(f"{OUT}/sonar_results.json", "w"), indent=2)

# readable summary
L = ["# SonarQube results - Flasky", "", "## Measures", ""]
L += [f"- {k}: {v}" for k, v in sorted(measures.items())]
L += ["", f"## Issues ({len(issues)})", "",
      "| Type | Severity | Impact (quality:severity) | File:Line | Rule | Message |", "|---|---|---|---|---|---|"]
for i in sorted(issues, key=lambda i: (i.get("type", ""), i.get("severity", ""), i["component"])):
    f = i["component"].split(":", 1)[-1]
    imp = ", ".join(f"{x['softwareQuality']}:{x['severity']}" for x in i.get("impacts", []))
    L.append(f"| {i.get('type')} | {i.get('severity')} | {imp} | {f}:{i.get('line', '')} | "
             f"{i['rule']} | {i['message'].replace('|', '/')} |")
L += ["", f"## Security hotspots ({len(hotspots)})", ""]
for h in hotspots:
    L.append(f"- {h['component'].split(':', 1)[-1]}:{h.get('line', '')} [{h.get('vulnerabilityProbability')}] {h['message']}")
open(f"{OUT}/summary.md", "w").write("\n".join(L) + "\n")
print("\n".join(L))
