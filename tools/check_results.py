#!/usr/bin/env python3
"""检查收到的结果文件 / Check the result files you received.

    python3 tools/check_results.py  <文件夹或文件 / folder or files>

例如 / e.g.  python3 tools/check_results.py ~/Downloads/image_study_*.json
每份结果一行：编号、答了多少题、注意力检查、每题中位用时、总用时、屏幕，最后一列是结论。
One line per result: code, answers, attention checks, median time per trial, total minutes, screen, verdict.
合格的标准和分析程序一样：做完、注意力检查至少 75 % 正确、每题中位用时至少 0.6 秒。
"""
import datetime as dt
import glob
import json
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def expected_counts():
    """Trials per code from trials.js next to this folder (318 if it cannot be read)."""
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


def main(args):
    paths = []
    for a in args or ['.']:
        a = os.path.expanduser(a)
        paths += sorted(glob.glob(os.path.join(a, '*.json'))) if os.path.isdir(a) else sorted(glob.glob(a))
    if not paths:
        print('没有找到 .json 文件 / no .json files found')
        return 1
    exp = expected_counts()
    seen, rows, n_ok = {}, [], 0
    print(f'{"文件 file":44s} {"编号":5s} {"答题":>9s} {"注意力":>7s} {"中位秒":>6s} {"分钟":>5s}  {"屏幕 screen":17s} 结论 verdict')
    for p in paths:
        name = os.path.basename(p)
        try:
            st = json.load(open(p, encoding='utf-8'))
        except Exception as e:  # noqa: BLE001
            print(f'{name[:44]:44s} 读不出来 / unreadable: {e}')
            continue
        if not isinstance(st, dict) or 'responses' not in st:
            print(f'{name[:44]:44s} 不是本实验的结果文件 / not a result file of this study')
            continue
        code = st.get('set', '?')
        resp = st['responses']
        main_ = [r for r in resp if isinstance(r.get('c'), int)]
        chk = [r for r in resp if r.get('c') == 'check']
        acc = sum(bool(r.get('correct')) for r in chk) / len(chk) if chk else float('nan')
        rt = statistics.median([r['rt'] for r in main_]) / 1000 if main_ else 0.0
        mins = minutes(st.get('started', ''), st.get('finished') or (resp[-1]['at'] if resp else ''))
        n_exp = exp.get(code, 318)
        scr = st.get('display_check') or {}
        screen = f'{scr.get("dev_w", "?")}x{scr.get("dev_h", "?")} dpr{scr.get("dpr", "?")}'
        key = (code, st.get('started'))
        if key in seen:
            verdict = f'重复（和 {seen[key]} 是同一份）/ duplicate'
        elif not st.get('finished') or len(resp) < n_exp:
            verdict = '没做完 / incomplete'
        elif chk and acc < 0.75:
            verdict = '注意力检查不合格 / failed attention checks'
        elif rt < 0.6:
            verdict = '答得太快 / too fast'
        else:
            verdict = '合格 / OK'
            n_ok += 1
        seen.setdefault(key, name)
        print(f'{name[:44]:44s} {code:5s} {len(resp):4d}/{n_exp:<4d} {(100 * acc if chk else float("nan")):6.0f}% {rt:6.1f} {mins:5.0f}  {screen:17s} {verdict}')
        rows.append((code, verdict))
    codes = sorted({c for c, v in rows if v.startswith('合格')})
    print(f'\n合格 {n_ok} 份 / {n_ok} valid; 编号 / codes: {", ".join(codes) if codes else "-"}')
    if exp:
        missing = [c for c in sorted(exp) if c not in codes]
        print(f'还没有合格结果的编号 / codes without a valid result yet: {", ".join(missing) if missing else "无 / none"}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
