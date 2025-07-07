import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "%%%という名前のクラスを作成し、それは%%%である。",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "%%%クラスは、selfと***のパラメータを取る__init__を持つ。",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "%%%クラスは、selfと@@@のパラメータを取る***という名前の関数を持つ。",
    "*** = %%%()":
      "***をクラス%%%のインスタンスに設定する。",
    "***.***(@@@)":
      "***から***関数を取得し、パラメータself, @@@でそれを呼び出す。",
    "***.*** = '***'":
      "***から***属性を取得し、それを'***'に設定する。"
}

# フレーズを最初に練習したいかどうか
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# ウェブサイトから単語を読み込む
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # 架空のクラス名
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # 架空のその他の名前
        for word in other_names:
            result = result.replace("***", word, 1)

        # 架空のパラメータリスト
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# CTRL-Dを押すまで続ける
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"答え:  {answer}\n\n")
except EOFError:
    print("\nさようなら")
