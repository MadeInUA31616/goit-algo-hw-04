def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats.append({'id': cat_id, 'name': name, 'age': int(age)})
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    return cats

cats = get_cats_info("cats.txt")
print(cats)
