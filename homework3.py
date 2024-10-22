#1
def Operations(a, b):
    set_a = set(a)
    set_b = set(b)
    
    intersection = set_a & set_b
    union = set_a | set_b
    difference_a_b = set_a - set_b
    difference_b_a = set_b - set_a
    
    return [intersection, union, difference_a_b, difference_b_a]

#2
def Dictionary(sentence):

    dict = {}
    for letter in sentence:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
        
    return dict

#3
def Comp(dict1, dict2):
    for key in dict1:
        if key not in dict2:
            return False
        if dict1[key] != dict2[key]:
            return False
    return True

#4
def build_xml_element(tag, content, **attributes):
    for key, value in attributes.items():
        tag += " " + key + "=\"" + value + "\""

    return "<" + tag + ">" + content + "</" + tag.split(" ")[0] + ">"

#5
def Validation(rules, dictionary):    
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False
        value = dictionary[key]

        if not value.startswith(prefix):
            return False
        if middle not in value or value.startswith(middle) or value.endswith(middle):
            return False
        if not value.endswith(suffix):
            return False

    return True

#6
def Count(list):
    
    a = set()
    b = set()

    for word in list:
        if word in a:
            b.add(word)
        else:
            a.add(word)

    return (len(a), len(b))

#7
def Operations2(*sets):
    
    result = {}
    list1 = list(sets)

    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            set_a = list1[i]
            set_b = list1[j]
            intersection, union, difference_a_b, difference_b_a = Operations(set_a, set_b)
            result[f"{set_a} | {set_b}"] = union
            result[f"{set_a} & {set_b}"] = intersection
            result[f"{set_a} - {set_b}"] = difference_a_b
            result[f"{set_b} - {set_a}"] = difference_b_a
        
    return result

#10
def Mapping(mapping):

    current = mapping["start"]
    visited = set()
    result = []

    while True:
        if current in visited:
            break

        result.append(current)
        visited.add(current)
        current = mapping[current]

    return result

#11
def Positional(*args, **keywords):
    keywords = set(keywords.values())
    
    count = sum(1 for arg in args if arg in keywords)
    
    return count

print(Operations([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print(Dictionary("Ana has apples."))
print(Comp({"a": 2, "b": 1}, {"a": 2, "b": 1}))
print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))
print(Validation({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
print(Count([1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7]))
print(Operations2({1,2}, {2, 3}))
print(Mapping({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
print(Positional(1, 2, 3, 4, x=1, y=2, z=3, w=5))