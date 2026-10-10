# -*- coding: utf-8 -*-
import pypdf
import os
import glob
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

q_dir = r'C:\Users\HP\Downloads\OLPAI\Quizzes'
for fpath in glob.glob(os.path.join(q_dir, "*.pdf")):
    fname = os.path.basename(fpath)
    try:
        reader = pypdf.PdfReader(fpath)
        print(f"{fname:35s}: {len(reader.pages):3d} pages")
    except Exception as e:
        print(f"{fname:35s}: Error {e}")
