import thingi10k

thingi10k.init()


full_data = thingi10k.dataset()
categories = sorted(set(full_data['category']))

with open("category_query_output.txt", "w") as file:
    for cat in categories:
        subset = thingi10k.dataset(category=cat)
        file.write("-------------------------------------\n")
        file.write(f"Category: {cat}\n")
        file.write(f"Amount of models for this category: {len(subset)}\n")
        file.write(f"The unique subcategories within this category are: {subset.unique("subcategory")}\n")
        # looking for unique models 
        unique_names = list(dict.fromkeys(subset['name']))[:20]
        file.write(f"Some examples of model names are: {unique_names}\n")
        file.write("-------------------------------------")

print("Done logging.")