import glob
import json
import re
import collections

regexp = re.compile(r'^[\d]+\-[\d]+\-[\d]+$')

reps = glob.glob("reports/*-weekly-report.html")
result = {}
# print(reps)
for rep in reps:
    rep = rep.split('/')[-1]
    parts = rep.split('.')[0].split('-')
    print(rep, '-'.join(parts[:3]))
    if len(parts) < 5:
        continue
    if not regexp.search('-'.join(parts[:3])):
        continue
    date = '-'.join(parts[:3])
    if len(parts)==5:
        state="US"
    elif len(parts)==6:
        state = parts[3]
    else:
        continue
    if state not in result:
        result[state] = []
    result[state].append(date)
for k in result:
    result[k] = sorted(result[k], reverse=True)

# Sort keys alphabetically, keeping US at the top. 
result = collections.OrderedDict(sorted(result.items(), key = lambda x: 'AAA' if x[0] == 'US' else x[0]))
json.dump(result, open("reports/reports.json", "w"))

reps = glob.glob("eval-reports/*-Weekly-Model-Evaluation.html")
result = {}
# print(reps)
for rep in reps:
    rep = rep.split('/')[-1]
    parts = rep.split('.')[0].split('-')
    print(rep, '-'.join(parts[:3]))
    if len(parts) < 5:
        continue
    if not regexp.search('-'.join(parts[:3])):
        continue
    date = '-'.join(parts[:3])
    if len(parts)==6:
        state="US"
    elif len(parts)==7:
        state = parts[3]
    else:
        continue
    if state not in result:
        result[state] = []
    result[state].append(date)
for k in result:
    result[k] = sorted(result[k], reverse=True)

# Sort keys alphabetically, keeping US at the top. 
result = collections.OrderedDict(sorted(result.items(), key = lambda x: 'AAA' if x[0] == 'US' else x[0]))
json.dump(result, open("eval-reports/reports.json", "w"))

