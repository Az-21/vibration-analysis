def create_sublists(data, bucket_size):
  sublists = [data[i : i + bucket_size] for i in range(0, len(data), bucket_size)]
  return sublists
