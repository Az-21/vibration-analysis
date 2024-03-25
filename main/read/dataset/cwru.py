import os
import main.read.csv


def read(path):
  normal_folders: list[str] = ["12k Normal"]
  faulty_folders: list[str] = ["12k Fan End Bearing Fault", "12k Drive End Bearing Fault"]

  # Lists to store CSVs as DFs
  normal_dfs = []
  faulty_dfs = []

  for folder in normal_folders:
    folder_path = os.path.join(path, folder)
    df = main.read.csv.as_list(folder_path)
    normal_dfs.append(df)

  for folder in faulty_folders:
    folder_path = os.path.join(path, folder)
    df = main.read.csv.as_list(folder_path)
    faulty_dfs.append(df)

  return (normal_dfs, faulty_dfs)
