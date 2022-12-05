from pandas import DataFrame


def parse_dataframe(data: DataFrame):
    di = data.set_index("JobID").T.to_dict('list')
    document_list = []
    for key, value in di.items():
        document = {
            'JobID': key,
            'SubmitTime': value[0],
            'WaitTime': value[1],
            'RunTime': value[2],
            'NProc': value[3],
            'UsedCPUTime': value[4],
            'UsedMemory': value[5],
            'ReqNProcs': value[6],
            'ReqTime': value[7],
            'ReqMemory': value[8],
            'Status': value[9],
            'UserID': value[10],
            'GroupID': value[11],
            'ExecutableID': value[12],
            'QueueID': value[13],
            'PartitionID': value[14],
            'OrigSiteID': value[15],
            'LastRunSiteID': value[16],
            'JobStructure': value[17],
            'JobStructureParams': value[18],
            'UsedNetwork': value[19],
            'UsedLocalDiskSpace': value[20],
            'UsedResources': value[21],
            'ReqPlatform': value[22],
            'ReqNetwork': value[23],
            'ReqLocalDiskSpace': value[24],
            'ReqResources': value[25],
            'VOID': value[26],
            'ProjectID': value[27]

        }

        document_list.append(document)
    return document_list

