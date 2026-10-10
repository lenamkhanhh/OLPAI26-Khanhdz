# -*- coding: utf-8 -*-
import urllib.request
import json

test_list = [
    # Candidates cho §2.2 (Activation Functions: ReLU, Sigmoid, Softmax)
    ("§2.2_A", "m0p7flgk414", "3Blue1Brown chapter"),
    ("§2.2_B", "68BZ5fQtRL8", "StatQuest"),
    ("§2.2_C", "s-V7gKpHbV8", "Activation Functions overview"),
    ("§2.2_D", "k4a3P9DuZ9c", "StatQuest Softmax"),
    ("§2.2_E", "kp33ZprO0Ck", "StatQuest"),
    ("§2.2_F", "YzhGY_9gflM", "Deep Learning activation"),
    # Candidates cho §4.3 (Cosine Similarity)
    ("§4.3_A", "e9U0QafnwWQ", "StatQuest"),
    ("§4.3_B", "m_CooPE3R44", "Cosine similarity in Python"),
    ("§4.3_C", "x_t7d1p8yVw", "Cosine similarity NLP"),
    ("§4.3_D", "ilskw9F4wX8", "StatQuest"),
]

for tag, ytid, desc in test_list:
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={ytid}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=3) as r:
            d = json.loads(r.read().decode('utf-8'))
            print(f"PASS {tag}: {ytid} -> {d.get('title')}")
    except Exception as e:
        pass
print("Done test.")
