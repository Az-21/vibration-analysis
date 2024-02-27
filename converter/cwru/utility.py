import os


def flatten(xss):
    return [x for xs in xss for x in xs]


def find_mat_files(directory):
    mat_files = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".mat"):
                mat_files.append(os.path.join(root, filename))
    return mat_files
