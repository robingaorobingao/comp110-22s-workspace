# """Demonstrations of dictionary capabilities."""
# # declaring the type of a dictionary
# schools: dict[str, int]
# # initialize to an empty dictionary
# schools = dict()
# # set a key-value pairing in the dictionary
# schools["unc"] = 19400
# schools["duke"] = 6717
# schools["ncsu"] = 26150
# # print a dictionary literal representation
# print(schools)
# # access a value by its key — "lookup"
# print(f"unc has {schools['unc']} students")
# # remove a key-value pair from a dictionary by its key
# schools.pop("duke")
# # # test for the existence of a key
# # is_duke_present: bool = "duke" in schools
# # print(f"duke is present: {is_duke_present}")
# if "duke" in schools:
#     print("found the key 'duke' in schools")
# else:
#     print("no key 'duke' in schools")
# schools["unc"] = 20000
# schools["ncsu"] += 200
# print(schools)
# # empty dictionary literal
# schools = {}
# print(schools)
# # initialize key-value pairs
schools = {"unc": 19400, "duke": 6717, "ncsu": 261500}
# print(schools)
# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")