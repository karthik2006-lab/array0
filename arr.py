import os
import sys

def parse_scores_from_string(s):
    s = s.replace(',', ' ')
    parts = [p.strip() for p in s.split()]
    scores = []
    for p in parts:
        try:
            scores.append(float(p))
        except ValueError:
            print(f"warning: skipping non-numeric token: {p}")
            continue
    return scores

def read_scores():
    if len(sys.argv) > 1:
        return parse_scores_from_string(" ".join(sys.argv[1:]))

    env = os.getenv("scores")
    if env:
        return parse_scores_from_string(env)

    if os.path.isfile("scores.txt"):
        with open("scores.txt", "r") as f:
            return parse_scores_from_string(f.read())

    raw = input("Enter scores separated by spaces or commas: ")
    return parse_scores_from_string(raw)

def main():
    scores = read_scores()
    if not scores:
        print("no valid scores provided")
        sys.exit(1)

    total = sum(scores)
    avg = total / len(scores)

    print("==main/master branch output")
    print(f"count of scores: {len(scores)}")
    print(f"sum: {total}")
    print(f"average: {avg}")
    if len(scores)>0:
        print("==local branch output==")
        print(f"Maximum: {max(scores)}")
        print(f"minimum: {min(scores)}")
if __name__ == "__main__":
    main()
