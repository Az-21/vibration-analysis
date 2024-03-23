import os
import pandas as pd


def mini_batch_normal(chunk_size):
  # Define the directory containing CSV files
  directory = r"C:\Users\sinuk\OneDrive\Documents\Python_VS\CSV\12k Normal"

  # Initialize an empty list to store sub-lists for all CSV files
  all_sublists = []

  # Iterate over each file in the directory
  for filename in os.listdir(directory):
    if filename.endswith(".csv"):
      filepath = os.path.join(directory, filename)

      # Read the CSV file into a DataFrame
      df = pd.read_csv(filepath)
      df1 = df.iloc[:120000, :]

      # Initialize an empty list to store sub-lists for the current CSV file
      file_sublists = []

      # Iterate over the DataFrame in chunks and append each chunk as a sub-list
      for i in range(0, len(df1), chunk_size):
        chunk = df1.iloc[i : i + chunk_size].values.tolist()
        file_sublists.append(chunk)

      # Append the sub-lists for the current CSV file to the list of all sub-lists
      all_sublists.append(file_sublists)

  # Example: Print the number of files processed and the number of sub-lists for each file
  print(f"Number of files processed: {len(all_sublists)}")
  for i, file_sublists in enumerate(all_sublists):
    print(f"File {i+1}: Number of sub-lists: {len(file_sublists)}")
  print(all_sublists)


# Define the list of parent directories
parent_directories = [
  r"C:\Users\sinuk\OneDrive\Documents\Python_VS\CSV\12k Fan End Bearing Fault",
  r"C:\Users\sinuk\OneDrive\Documents\Python_VS\CSV\12k Drive End Bearing Fault",
]


def mini_batch(chunk_size):
  # Initialize an empty list to store sub-lists for all CSV files in all folders
  all_sublists = []

  # Iterate over each parent directory
  for parent_directory in parent_directories:
    # Initialize an empty list to store sub-lists for all CSV files in all folders in the current parent directory
    parent_sublists = []

    # Iterate over each folder in the current parent directory
    for foldername in os.listdir(parent_directory):
      folderpath = os.path.join(parent_directory, foldername)

      # Check if the current item in the parent directory is a folder
      if os.path.isdir(folderpath):
        # Initialize an empty list to store sub-lists for all CSV files in the current folder
        folder_sublists = []

        # Iterate over each file in the current folder
        for filename in os.listdir(folderpath):
          if filename.endswith(".csv"):
            filepath = os.path.join(folderpath, filename)

            # Read the CSV file into a DataFrame
            df = pd.read_csv(filepath)
            df1 = df.iloc[:120000, 1:]

            # Initialize an empty list to store sub-lists for the current CSV file
            file_sublists = []

            # Iterate over the DataFrame in chunks and append each chunk as a sub-list
            for i in range(0, len(df1), chunk_size):
              chunk = df1.iloc[i : i + chunk_size].values.tolist()
              file_sublists.append(chunk)

            # Append the sub-lists for the current CSV file to the list of all sub-lists in the folder
            folder_sublists.append(file_sublists)

        # Append the sub-lists for all CSV files in the current folder to the list of all sub-lists in the parent directory
        parent_sublists.append(folder_sublists)

    # Append the sub-lists for all CSV files in all folders in the current parent directory to the list of all sub-lists
    all_sublists.append(parent_sublists)

  # Example: Print the number of parent directories processed and the number of sub-lists for each parent directory
  print(f"Number of parent directories processed: {len(all_sublists)}")
  for i, parent_sublists in enumerate(all_sublists):
    print(f"Parent Directory {i+1}: Number of sub-lists: {len(parent_sublists)}")
  print(all_sublists)


batch_1 = mini_batch_normal(3000)
batch_2 = mini_batch(3000)
