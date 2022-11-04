import pandas as pd
import numpy as np
from utils.get_consensus_similarity import get_consensus_similarity


data = pd.read_csv("./data/pizzas.csv")

def sprint_3(NODE_DF, _data):
  data_list = _data.iterrows()
  for (index, row) in data_list:
    print("================================")
    similarity = get_consensus_similarity(NODE_DF, row)
    print(similarity)

try:
  row_frame_A = data[data["Nombre"] == "Natalia Betancourt"]
  row_frame_B = data[data["Nombre"] == "Isabella Gallego"]

  similarity = get_consensus_similarity(row_frame_A, row_frame_B)


  # print(similarity)
  sprint_3(row_frame_A, data)

except:
  print('oops')