def count_item_and_sort(items):
    data = {}
    for el in items:
        data[el] = items.count(el)
    sorted_data = dict(sorted(data.items(), key=lambda value: (value[1], value[0])))
    return ' '.join([f"{key}->{value}" for key, value in sorted_data.items()])


if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"
