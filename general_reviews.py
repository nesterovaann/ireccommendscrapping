import irecommend as rec
import irecommend_list as reclist


def delete_doubles(list):
    newlist = []
    for i in list:
        if i not in newlist: newlist.append(i)
    return newlist


def main():
    reclist.download_file('https://irecommend.ru/content/kolyaska-2-v-1-adamex-massimo')
    f = reclist.read_file('list_of_pages.html')
    links = reclist.get_links('list_of_pages.html')
    new_list_of_links = reclist.create_links(links)
    minus = []
    plus = []
    i = 0
    for link in new_list_of_links:
        if i == 9:
            break
        print(link)
        print(i)
        rec.download_file(link)
        filename = 'review.html'
        min, plu = rec.parse_user_datafile_bs(filename)
        minus.extend(min)
        plus.extend(plu)
        print(minus)
        print(plus)
        i += 1
    minus = delete_doubles(minus)
    plus = delete_doubles(plus)
    print("Минусы:", minus)
    print("Плюсы:", plus)






if __name__ == "__main__":
    main()