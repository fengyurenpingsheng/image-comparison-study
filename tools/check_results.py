#!/usr/bin/env python3
"""检查收到的结果文件 / Check the result files you received.

    python3 tools/check_results.py  <文件夹或文件 / folder or files>  [--csv 编号表.csv]

例如 / e.g.  python3 tools/check_results.py "../subj_own_results"
每份结果一行：内部编号（按开始时间排）、名字、答了多少题、注意力检查、每题中位用时、总用时、屏幕，最后一列是结论。
One line per result: internal number (by start time), name, answers, attention checks, median time per trial,
total minutes, screen, verdict.
合格的标准和分析程序一样：做完、注意力检查至少 75 % 正确、每题中位用时至少 0.6 秒。
加 --csv 会另存一张"编号-名字-文件-结论"对照表；里面有名字，只留在你自己的电脑上。
"""
import argparse
import csv
import datetime as dt
import glob
import json
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def expected_counts():
    """Trials per order from trials.js next to this folder ({} if it cannot be read)."""
    try:
        t = open(os.path.join(HERE, '..', 'trials.js'), encoding='utf-8').read()
        s = json.loads(t[t.index('{'):t.rindex('}') + 1])
        return {k: len(v) for k, v in s['participants'].items()}
    except Exception:  # noqa: BLE001
        return {}


def minutes(a, b):
    try:
        f = lambda x: dt.datetime.fromisoformat(x.replace('Z', '+00:00'))  # noqa: E731
        return (f(b) - f(a)).total_seconds() / 60
    except Exception:  # noqa: BLE001
        return float('nan')


def norm(v):
    return ' '.join(str(v or '').split()).lower()


def main(argv):
    ap = argparse.ArgumentParser(description='检查结果文件 / check result files')
    ap.add_argument('paths', nargs='*', default=['.'], help='文件夹或 .json 文件 / folder or .json files')
    ap.add_argument('--csv', help='另存对照表 / also write a number-name-file table (keep it private)')
    a = ap.parse_args(argv)
    paths = []
    for p in a.paths:
        p = os.path.expanduser(p)
        paths += sorted(glob.glob(os.path.join(p, '*.json'))) if os.path.isdir(p) else sorted(glob.glob(p))
    if not paths:
        print('没有找到 .json 文件 / no .json files found')
        return 1
    exp = expected_counts()
    n_default = max(exp.values()) if exp else 119
    recs = []
    for p in paths:
        name = os.path.basename(p)
        try:
            st = json.load(open(p, encoding='utf-8'))
        except Exception as e:  # noqa: BLE001
            print(f'{name}: 读不出来 / unreadable: {e}')
            continue
        if not isinstance(st, dict) or 'responses' not in st:
            print(f'{name}: 不是本实验的结果文件 / not a result file of this study')
            continue
        recs.append((st.get('started') or '', name, st))
    recs.sort(key=lambda r: (r[0], r[1]))
    sessions_of = {}
    for started, _n, st in recs:
        k = norm(st.get('pid'))
        if k:
            sessions_of.setdefault(k, set()).add(started)

    print(f'{"#":>3s}  {"名字 name":20s} {"答题":>9s} {"注意力":>6s} {"中位秒":>6s} {"分钟":>5s}  {"屏幕 screen":16s} {"结论 verdict":24s} 文件 file')
    seen, rows, n_ok, number = {}, [], 0, 0
    for started, fname, st in recs:
        resp = st['responses']
        main_ = [r for r in resp if isinstance(r.get('c'), int)]
        chk = [r for r in resp if r.get('c') == 'check']
        acc = sum(bool(r.get('correct')) for r in chk) / len(chk) if chk else float('nan')
        rt = statistics.median([r['rt'] for r in main_]) / 1000 if main_ else 0.0
        mins = minutes(started, st.get('finished') or (resp[-1]['at'] if resp else ''))
        n_exp = exp.get(st.get('set'), n_default)
        scr = st.get('display_check') or {}
        screen = f'{scr.get("dev_w", "?")}x{scr.get("dev_h", "?")} dpr{scr.get("dpr", "?")}'
        who = str(st.get('pid') or st.get('set') or '-')
        if len(sessions_of.get(norm(st.get('pid')), ())) > 1:
            who += ' (同名)'
        key = (st.get('set'), started)
        if key in seen:
            num = seen[key]
            verdict = f'重复（同 #{num:02d}）/ duplicate'
        else:
            number += 1
            num = seen[key] = number
            if not st.get('finished') or len(resp) < n_exp:
                verdict = '没做完 / incomplete'
            elif chk and acc < 0.75:
                verdict = '注意力检查不合格 / failed checks'
            elif rt < 0.6:
                verdict = '答得太快 / too fast'
            else:
                verdict = '合格 / OK'
                n_ok += 1
        print(f'{num:3d}  {who[:20]:20s} {len(resp):4d}/{n_exp:<4d} {(100 * acc if chk else float("nan")):5.0f}% {rt:6.1f} {mins:5.0f}  '
              f'{screen:16s} {verdict:24s} {fname}')
        rows.append({'number': f'{num:02d}', 'name': st.get('pid') or '', 'file': fname, 'started': started,
                     'answers': len(resp), 'attention': '' if not chk else f'{acc:.2f}', 'median_s': f'{rt:.1f}',
                     'verdict': verdict})
    print(f'\n合格 {n_ok} 份 / {n_ok} valid results (目标 15–20 / target 15-20)')
    if a.csv:
        with open(os.path.expanduser(a.csv), 'w', newline='', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ['number'])
            w.writeheader()
            w.writerows(rows)
        print(f'对照表 / table: {a.csv}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
