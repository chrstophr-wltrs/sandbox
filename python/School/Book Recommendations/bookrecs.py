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

def takeSecond(elem):
    return elem[1]

def last_name(elem):
    name = elem[0].split(' ')
    return name[-1]

def calculate_affinity(first_reader, second_reader):
    affinity = 0
    first_ratings = readers[first_reader]
    second_ratings = readers[second_reader]
    for i in range(len(first_ratings)):
        current_index = i - 1
        affinity += first_ratings[current_index] * second_ratings[current_index]
    return affinity

def friends(reader_to_calculate):
    scores = []
    for name in readers:
        if reader_to_calculate != name:
            current_affinity = calculate_affinity(reader_to_calculate, name)
            name_score = [name, current_affinity]
            scores.append(name_score)
    scores.sort()
    sorted_friends = sorted(scores, key=takeSecond, reverse = True)
    return (sorted_friends[0][0], sorted_friends[1][0])

def recommend(book_hunter):
    best_friends = friends(book_hunter)
    recommendations = []
    friend1_recommendations = readers[best_friends[0]]
    friend2_recommendations = readers[best_friends[1]]
    friend_likes = []
    hunter_has_read = readers[book_hunter]
    for i in range(len(friend1_recommendations)):
        current_index = i - 1
        book_like_status = [friend1_recommendations[current_index], friend2_recommendations[current_index]]
        friend_likes.append(book_like_status)
    for i in range(len(hunter_has_read)):
        ind = i - 1
        current_book = book_data[ind]
        if hunter_has_read[ind] == 0:
            if (friend_likes[ind][0] > 2) or (friend_likes[ind][1] > 2):
                recommendations.append(current_book)
    recommendations.sort(key=last_name)
    return recommendations

def recommendations_list(reader_name):
    best_friends = friends(reader_name)
    good_books = recommend(reader_name)
    print(f"Recommendtions for {reader_name} from {best_friends[0]} and {best_friends[1]}:")
    for book in good_books:
        print(f"\t {book[0]}, {book[1]}")


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