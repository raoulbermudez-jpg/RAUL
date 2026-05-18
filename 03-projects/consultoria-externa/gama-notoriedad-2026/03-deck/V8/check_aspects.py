import sys
sys.stdout.reconfigure(encoding='utf-8')
from pptx import Presentation

DIR = r"C:\rAUL\03-projects\consultoria-externa\gama-notoriedad-2026\03-deck\V8"

files = [
    ('V8 (PNG charts)',    DIR + r'\2026-05-18_Notoriedad-Gama-2026_V8.pptx'),
    ('V8.2 (mal aspect)',  DIR + r'\2026-05-18_Notoriedad-Gama-2026_V8.2.pptx'),
    ('V8.3 (fix aspect)',  DIR + r'\2026-05-18_Notoriedad-Gama-2026_V8.3.pptx'),
]
for label, path in files:
    pres = Presentation(path)
    w = pres.slide_width / 914400
    h = pres.slide_height / 914400
    ratio = w/h
    aspect = '16:9' if abs(ratio-1.778) < 0.01 else ('4:3' if abs(ratio-1.333) < 0.01 else 'OTRO')
    print(f'{label}: {w:.2f} x {h:.2f} in, ratio {ratio:.3f} -> {aspect}')
