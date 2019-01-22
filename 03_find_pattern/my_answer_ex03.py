# coding : utf-8
import re

def main():
    pattern = re.compile('##.*')
    matched = []
    with open('README.md', 'r', encoding='utf-8') as f:
        for line in f:
            match = pattern.match(line.strip())
            if match:
                matched.append(match.group(0)) # マッチした全ての部分
    print(matched)

if __name__ == "__main__":
    main()
