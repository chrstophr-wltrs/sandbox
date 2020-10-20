book_data = []
with open("booklist.txt", "r") as data:
    for line in data:
        working_line = line.strip().split(',')
        tuple_line = tuple(working_line)
        book_data.append(tuple_line) 

readers = {}
list_of_readers = []
with open("ratings.txt", "r") as data:
    for line in data:
        reader_name = line.strip().lower()
        reader_ratings = data.readline().strip().split(' ')
        reader_ratings = [int(i) for i in reader_ratings]
        readers[reader_name] = reader_ratings
        list_of_readers.append(reader_name)

def calculate_affinity(first_reader, second_reader):
    affinity = 0
    first_ratings = readers[first_reader]
    second_ratings = readers[second_reader]
    for i in range(len(first_ratings)):
        affinity += first_ratings[i] * second_ratings[i]
    return affinity

def friends(reader_to_calculate):
    scores = []
    for name in readers:
        if reader_to_calculate != name:
            current_affinity = calculate_affinity(reader_to_calculate, name)
            name_score = [name, current_affinity]
            scores.append(name_score)
    scores.sort()
    sorted_friends = sorted(scores, key=lambda elem: elem[1], reverse = True)
    return (sorted_friends[0][0], sorted_friends[1][0])

def recommend(book_hunter):
    best_friends = friends(book_hunter)
    recommendations = []
    friend1_recommendations = readers[best_friends[0]]
    friend2_recommendations = readers[best_friends[1]]
    friend_likes = []
    hunter_has_read = readers[book_hunter]
    for i in range(len(friend1_recommendations)):
        book_like_status = [friend1_recommendations[i], friend2_recommendations[i]]
        friend_likes.append(book_like_status)
    for i in range(len(hunter_has_read)):
        ind = i - 1
        current_book = book_data[ind]
        if hunter_has_read[ind] == 0:
            if (friend_likes[ind][0] > 2) or (friend_likes[ind][1] > 2):
                recommendations.append(current_book)
    recommendations.sort(key=lambda name: name[0].split(' ')[-1].lower())
    return recommendations

def recommendations_list(reader_name):
    best_friends = friends(reader_name)
    good_books = recommend(reader_name)
    rec_list = (f"Recommendtions for {reader_name} from {best_friends[0]} and {best_friends[1]}:\n")
    for book in good_books:
        rec_list += (f"\t {book[0]}, {book[1]}\n")
    return rec_list

def report():
    report_string = ""
    for i in list_of_readers:
        report_string += (f"{recommendations_list(i)}\n")
    return report_string

def main():
    reader_to_test = input("Enter a reader's name: ")
    while reader_to_test != "":
        if reader_to_test in list_of_readers:
            recommendations_list(reader_to_test)
            pass
        else:
            print(f"No such reader {reader_to_test}")
        reader_to_test = input("Enter a reader's name: ")


if __name__ == "__main__":
    main()