def sort_me(courses):
    courses = [x.split('-') for x in courses]
    courses = sorted(courses, key=lambda x: (x[1],x[0]))
    return [('-').join(x) for x in courses]