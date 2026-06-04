"""Convert vocab data and replace VOCAB in jp_study_kivy.py"""
import re, random, os, sys

sys.path.insert(0, os.path.dirname(__file__))

# Import the raw data
exec(open(os.path.join(os.path.dirname(__file__), 'vocab_data.py'), encoding='utf-8').read())

def parse_word(w):
    """'僕（ぼく）' → ('僕','ぼく'); 'メンバー' → ('','メンバー')"""
    m = re.match(r'(.+?)（(.+?)）', w)
    if m: return m.group(1), m.group(2)
    return '', w

# Build new VOCAB
new_vocab = {}
total = 0
for day_num in sorted(RAW.keys()):
    day_name = f"第{day_num}天"
    entries = []
    for word, cn in RAW[day_num]:
        kanji, kana = parse_word(word)
        entries.append(f'{{"kanji":"{kanji}","kana":"{kana}","cn":"{cn}"}}')
    new_vocab[day_name] = entries
    total += len(entries)
    print(f'{day_name}: {len(entries)} words')

# Random review set
all_words = []
for entries in new_vocab.values():
    all_words.extend(entries)
random.shuffle(all_words)
new_vocab["随机复习"] = all_words

print(f'\nTotal: {total} words across {len(new_vocab)-1} days + random review')

# Build the Python code for the new VOCAB
lines = ['VOCAB = {']
day_keys = [k for k in new_vocab.keys() if k != '随机复习']
day_keys.sort(key=lambda k: int(k.replace('第','').replace('天','')))

for dk in day_keys:
    entries = new_vocab[dk]
    items = ',\n        '.join(entries)
    lines.append(f'    "{dk}": [{items}],')

# Random review
rand_items = ',\n        '.join(new_vocab['随机复习'])
lines.append(f'    "随机复习": [{rand_items}],')
lines.append('}')

vocab_code = '\n'.join(lines)

# Read current file
main_path = os.path.join(os.path.dirname(__file__), 'jp_study_kivy.py')
with open(main_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find VOCAB start and end (only the dict itself)
v_start = content.find('VOCAB = {')
depth = 0
v_end = v_start
for i in range(v_start, len(content)):
    if content[i] == '{': depth += 1
    elif content[i] == '}': depth -= 1
    if depth == 0:
        v_end = i + 1  # include the closing }
        break

new_content = content[:v_start] + vocab_code + content[v_end:]

# Remove old _all and SAVE_FILE/lines if they appear between
# (they should be in the removed section)

with open(main_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
size = os.path.getsize(main_path)
print(f'\nDone! File size: {size} bytes ({size/1024:.0f} KB)')
