# funkcja menu

results = [("Alfred", 10), ("Jan", 15), ("Darek", 20)]

def show_menu():
    print("\nMenu:\nall - wyświetl wszystkie wyniki\ndodaj - dodawanie wyniku\ngraj - zacznij kolejną grę")

def sort_results(scores_list):
    names, scores = [] , []
    for i in range(len(scores_list)):
        tmp_name, tmp_score = scores_list[i]
        names.append(tmp_name)
        scores.append(tmp_score)

    for i in range(1, len(scores)):
        key_scores = scores[i]
        key_names = names[i]
        j = i -1
        while j>= 0 and scores[j] > key_scores:
            scores[j + 1] = scores[j]
            names[j + 1] = names[j]
            j = j - 1
        scores[j + 1] = key_scores
        names[j + 1] = key_names

        while results:
            results.pop()
        while names and scores:
            results.append(names.pop(), scores.pop())
