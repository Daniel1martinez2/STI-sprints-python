from utils.get_consensus_similarity import get_consensus_similarity
from utils.get_value_from_DF import get_value_from_DF


def sprint_3(NODE_DF, _data, neighbors_length):
    data_list = _data.iterrows()
    neighbors = []
    for (index, row) in data_list:
        similarity = get_consensus_similarity(NODE_DF, row)
        # Check wether is the same node
        if get_value_from_DF(_data.iloc[[index]], "Nombre") is not get_value_from_DF(NODE_DF, "Nombre"):
            neighbors.append({
                "name": row["Nombre"],
                "similarity": similarity
            })
    return sorted(neighbors, key=lambda d: d['similarity'], reverse=True)[:neighbors_length]

    # for x in new_list:
    #     print("{0} is {1} close to {2}".format(
    #         x["name"], x["similarity"], NODE_DF["Nombre"].to_list()[0]))
    #     print("================================================")
