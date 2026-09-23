import re, zlib
with open(r'C:\laragon\www\blog\handson_extract\handson activity.docx.pdf', 'rb') as f:
    data = f.read()
streams = re.findall(rb'stream\r?\n(.*?)\r?\nendstream', data, re.DOTALL)
text_parts = []
for s in streams:
    try:
        dec = zlib.decompress(s)
        text_parts.append(dec.decode('latin-1', errors='replace'))
    except:
        pass
combined = '\n'.join(text_parts)
texts = re.findall(r'\((?:[^()\\]|\\.)*\)', combined)
clean = []
for t in texts:
    t = t.strip('()')
    t = t.replace('\\(', '(').replace('\\)', ')').replace('\\\\', '\\')
    if t.strip():
        clean.append(t)
with open(r'C:\laragon\www\blog\pdf_output.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(clean))