def main() -> None:
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)


def search_by_name(filename: str, word: str) -> list[str]:
    recipes = get_recipes_dict(filename)
    found = []
    for recipe in recipes:
        if word.lower() in recipe.lower():
            found.append(recipe)
    return found


def search_by_time(filename: str, prep_time: int) -> list[str]:
    recipes = get_recipes_dict(filename)
    found = []
    for recipe in recipes:
        if recipes[recipe]["time"] <= prep_time:
            found.append(f"{recipe}, preparation time {recipes[recipe]['time']} min")
    return found


def search_by_ingredient(filename: str, ingredient: str) -> list[str]:
    recipes = get_recipes_dict(filename)
    found = []
    for recipe in recipes:
        for current_ingredient in recipes[recipe]["ingredients"]:
            if current_ingredient == ingredient:
                found.append(
                    f"{recipe}, preparation time {recipes[recipe]['time']} min"
                )
    return found


def get_recipes_dict(filename: str) -> dict:
    recipes_list_raw = []
    with open(filename) as recipes_file:
        for line in recipes_file:
            recipes_list_raw.append(line)

    recipes_list = []
    current_recipe = []
    for i, item in enumerate(recipes_list_raw):
        if item == "\n":
            recipes_list.append(current_recipe.copy())
            current_recipe.clear()
        elif i == len(recipes_list_raw) - 1:
            current_recipe.append(item.strip())
            recipes_list.append(current_recipe.copy())
        else:
            current_recipe.append(item.strip())

    del recipes_list_raw
    del current_recipe

    recipes_dict = {}
    for recipe in recipes_list:
        recipes_dict[recipe[0]] = {"time": int(recipe[1]), "ingredients": recipe[2:]}

    return recipes_dict


# main()
