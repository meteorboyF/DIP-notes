import pathlib
REPL = '\ufffd'
file = pathlib.Path(r'c:\Users\ASUS\Desktop\DIP\DIP-notes\index.html')
content = file.read_text(encoding='utf-8')

fixes = [
    # Nav tab s2 - Sampling
    (f'id="tab-s2">{REPL}? Sampling',              'id="tab-s2">📐 Sampling'),
    # RGB section - Bit Depth step box (📏)
    (f'>{REPL}? Bit Depth</p>',                    '>📏 Bit Depth</p>'),
    # Section 2 icon (📐)
    (f'rgba(96,108,56,0.1);">{REPL}</div>',        'rgba(96,108,56,0.1);">📐</div>'),
    # Section 5 icon (📝)
    (f'rgba(168,80,80,0.1);">{REPL}</div>',        'rgba(168,80,80,0.1);">📝</div>'),
    # Warn box ⚠️ False Contouring
    (f'⚠{REPL}? False Contouring',                '⚠️ False Contouring'),
    # Applications - Edge Detection (📏 = U+1F4CF)
    (f'>{REPL}? Edge Detection</p>',               '>📏 Edge Detection</p>'),
    # ANN neural net node subscripts (₁ = U+2081)
    (f'>x{REPL}</div>',                            '>x₁</div>'),
    (f'>h{REPL}</div>',                            '>h₁</div>'),
    (f'>j{REPL}</div>',                            '>j₁</div>'),
    (f'>o{REPL}</div>',                            '>o₁</div>'),
    # Forward propagation "a = [x₁, x₂, ...]"
    (f'a = [x{REPL},',                             'a = [x₁,'),
    # Loss calculation y₁ and o₁
    (f'y{REPL}=1.0',                               'y₁=1.0'),
    (f'o{REPL}=0.4526',                            'o₁=0.4526'),
    # Theme toggle ☀️
    (f"'☀{REPL}?'",                               "'☀️'"),
]

count = 0
for broken, correct in fixes:
    if broken in content:
        n = content.count(broken)
        content = content.replace(broken, correct)
        count += n
        print(f'Fixed {n}x: {repr(broken[:60])} -> {repr(correct[:40])}')
    else:
        print(f'NOT FOUND: {repr(broken[:60])}')

remaining = content.count(REPL)
print(f'\nRemaining replacement chars: {remaining}')
if remaining:
    idx = content.find(REPL)
    print(f'Context: {repr(content[max(0,idx-40):idx+80][:150])}')

file.write_text(content, encoding='utf-8')
print(f'\nDone. {count} fix(es) applied.')
