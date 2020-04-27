from glob import glob
import os.path
import dictdiffer
from src.helpers import *

clusters_dir = "clusters"
db = get_db()

def main():
    # TODO: refactor everything
    clusters_definitions = [f_name for f_name in glob("../clusters/*.json")]
    cluster_path_template = "../clusters/{}.json"

    # check if existing and defined clusters match
    existing_clusters = db.cluster.list_clusters()
    up_to_date_clusters = list()
    # print(json.dumps(existing_clusters))

    if 'clusters' in existing_clusters:
        for existing_cluster in existing_clusters['clusters']:
            cluster_name = existing_cluster['cluster_name']
            cluster_id = existing_cluster["cluster_id"]
            possible_cluster_definition = cluster_path_template.format(cluster_name)
            file_name = os.path.splitext(os.path.basename(possible_cluster_definition))[0]
            if os.path.exists(possible_cluster_definition):
                with open(possible_cluster_definition, "r") as json_file:
                    cluster_definition = json.load(json_file)
                    if cluster_name != cluster_definition["cluster_name"]:
                        print("Error! Found different Cluster Name for {}".format(file_name))
                    else:
                        comparable_keys = cluster_definition.keys()
                        comparable_existing_cluster = dictfilt(existing_cluster, list(comparable_keys))

                        if comparable_existing_cluster != cluster_definition:
                            print("\nCluster definition for \"{}\" does not match!".format(cluster_name))

                            for diff in list(dictdiffer.diff(comparable_existing_cluster, cluster_definition)):
                                print(diff)

                            print("Updating and restarting cluster {}".format(cluster_id))
                            db.cluster.edit_cluster(cluster_id=cluster_id,**cluster_definition)
                            print("Done!")
                        up_to_date_clusters.append(cluster_name)
            else:
                print("\nDefinition for Cluster \"{}\" not found!".format(cluster_name))
                #TODO: Generate this automatically using --generate-definition or something like this

        # read cluster definition to create clusters
        for updated_cluster in up_to_date_clusters:
            clusters_definitions.remove(cluster_path_template.format(updated_cluster))

        for cluster_definition in clusters_definitions:
            with open(cluster_definition, 'r') as json_file:
                cluster_name = json.load(json_file)["cluster_name"]
                file_name = os.path.splitext(os.path.basename(cluster_definition))[0]
                if cluster_name != file_name:
                    print("Warning! Found different Cluster Name for {}".format(file_name))
                    clusters_definitions.remove(cluster_path_template.format(file_name))

    for cluster_definition in clusters_definitions:
        with open(cluster_definition, "r") as json_file:
            cluster_file = json.load(json_file)
            db.cluster.create_cluster(**cluster_file)
            print("\nCreating cluster {}".format(cluster_file["cluster_name"]))


main()
