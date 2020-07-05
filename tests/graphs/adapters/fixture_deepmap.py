from copy import deepcopy
import networkx as nx

from tests.base_fixture import graph, graph_with_virtual_lanes

# Translation of Dummy HD graph into DeepMap data
deepmap_lane_data = [
    {
        "id": 1,
        "fromLaneIdsList": [14],
        "toLaneIdsList": [2],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": 0, "lat": 0}, {"lng": 0, "lat": -1}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 2,
        "fromLaneIdsList": [1],
        "toLaneIdsList": [3, 4],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": 0, "lat": -1}, {"lng": 0, "lat": -2}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 3,
        "fromLaneIdsList": [2, 12],
        "toLaneIdsList": [5, 19],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": 0, "lat": -2}, {"lng": 0, "lat": -3}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 4,
        "fromLaneIdsList": [2, 12],
        "toLaneIdsList": [],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": 0, "lat": -2}, {"lng": 2, "lat": -2}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 5,
        "fromLaneIdsList": [3],
        "toLaneIdsList": [6, 7],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": 0, "lat": -3}, {"lng": 0, "lat": -4}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 6,
        "fromLaneIdsList": [5],
        "toLaneIdsList": [],
        "leftLanesList": [],
        "rightLanesList": [20],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "BROKEN",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": 0, "lat": -4}, {"lng": 0, "lat": -5}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 7,
        "fromLaneIdsList": [5],
        "toLaneIdsList": [8, 9],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": 0, "lat": -4}, {"lng": -1, "lat": -5}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 8,
        "fromLaneIdsList": [7],
        "toLaneIdsList": [],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": -1, "lat": -5}, {"lng": -2, "lat": -5}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 9,
        "fromLaneIdsList": [7],
        "toLaneIdsList": [10],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": -1, "lat": -5}, {"lng": -1, "lat": -4}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 10,
        "fromLaneIdsList": [9],
        "toLaneIdsList": [11, 12, 15],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": -1, "lat": -4}, {"lng": -1, "lat": -3}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 11,
        "fromLaneIdsList": [10],
        "toLaneIdsList": [13],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": -1, "lat": -3}, {"lng": -1, "lat": -1}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 12,
        "fromLaneIdsList": [10],
        "toLaneIdsList": [3, 4],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": -1, "lat": -3}, {"lng": 0, "lat": -2}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 13,
        "fromLaneIdsList": [11, 18],
        "toLaneIdsList": [14],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": -1, "lat": -1}, {"lng": -1, "lat": 0}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 14,
        "fromLaneIdsList": [13],
        "toLaneIdsList": [1],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": -1, "lat": 0}, {"lng": 0, "lat": 0}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 15,
        "fromLaneIdsList": [10],
        "toLaneIdsList": [16],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": -1, "lat": -3}, {"lng": -2, "lat": -2.5}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 16,
        "fromLaneIdsList": [15],
        "toLaneIdsList": [],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {
            "geometry": [{"lng": -2, "lat": -2.5}, {"lng": -3, "lat": -2.5}]
        },
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 17,
        "fromLaneIdsList": [],
        "toLaneIdsList": [18],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {
            "geometry": [{"lng": -3, "lat": -1.5}, {"lng": -2, "lat": -1.5}]
        },
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 18,
        "fromLaneIdsList": [17],
        "toLaneIdsList": [13],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": -2, "lat": -1.5}, {"lng": -1, "lat": -1}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 19,
        "fromLaneIdsList": [3],
        "toLaneIdsList": [20],
        "leftLanesList": [],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "DOUBLE SOLID",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": 0, "lat": -3}, {"lng": 1.5, "lat": -4}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
    {
        "id": 20,
        "fromLaneIdsList": [19],
        "toLaneIdsList": [],
        "leftLanesList": [6],
        "rightLanesList": [],
        "leftBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "BROKEN",
            "lineColor": "YELLOW",
        },
        "rightBoundaryLine": {
            "geometry": [],
            "isImplicit": False,
            "lineType": "SOLID",
            "lineColor": "WHITE",
        },
        "centerLine": {"geometry": [{"lng": 1.5, "lat": -4}, {"lng": 1.5, "lat": -5}]},
        "restrictions": {
            "allowedVehicleTypesList": ["CAR"],
            "trafficDirection": "STRAIGHT",
            "speedLimitKph": 40,
        },
    },
]

# Please note that there is no explicit concept of node in DeepMap and as such node IDs from original graph
# in base_fixture are not represented, so the actual node IDs created by the adapter will not correspond to the ones on
# the base fixture but rather on the ones generated below
expected_graph = deepcopy(graph)
expected_graph = nx.relabel_nodes(
    expected_graph,
    {
        1: 1,
        2: 2,
        3: 3,
        16: 4,
        4: 5,
        5: 6,
        6: 7,
        15: 8,
        7: 9,
        8: 10,
        9: 11,
        10: 12,
        11: 13,
        13: 14,
        14: 15,
        12: 16,
        17: 17,
        18: 18,
    },
)

expected_graph_with_virtual_lanes = deepcopy(graph_with_virtual_lanes)
expected_graph_with_virtual_lanes = nx.relabel_nodes(
    expected_graph_with_virtual_lanes,
    {
        1: 1,
        2: 2,
        3: 3,
        16: 4,
        4: 5,
        5: 6,
        6: 7,
        15: 8,
        7: 9,
        8: 10,
        9: 11,
        10: 12,
        11: 13,
        13: 14,
        14: 15,
        12: 16,
        17: 17,
        18: 18,
    },
)