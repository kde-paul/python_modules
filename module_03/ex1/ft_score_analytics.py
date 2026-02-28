import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    try:
        if not sys.argv[1:]:
            raise ValueError("No scores provided. Usage: \
python3 ft_score_analytics.py <score1> <score2> ...")
        else:
            list = []
            arg_i = 1
            arg_len = len(sys.argv)
            while arg_i < arg_len:
                list.append(int(sys.argv[arg_i]))
                arg_i += 1
            print("Scores processed:", list)
            print("Total players:", len(list))
            print("Total score:", sum(list))
            print("Average score:", sum(list) / len(list))
            print("High score:", max(list))
            print("Low score:", min(list))
            print("Score range:", max(list) - min(list))
    except Exception as error:
        print(error)
