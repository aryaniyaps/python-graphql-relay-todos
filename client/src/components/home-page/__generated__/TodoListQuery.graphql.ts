/**
 * @generated SignedSource<<8aa727cfc8bb6786c48cb66a702e7e32>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { ConcreteRequest, Query } from 'relay-runtime';
export type TodoListQuery$variables = {
  first: number;
};
export type TodoListQuery$data = {
  readonly notes: {
    readonly edges: ReadonlyArray<{
      readonly node: {
        readonly content: string;
        readonly createdAt: any;
        readonly id: any;
        readonly updatedAt: any | null | undefined;
      };
    }>;
    readonly pageInfo: {
      readonly hasNextPage: boolean;
    };
  };
};
export type TodoListQuery = {
  response: TodoListQuery$data;
  variables: TodoListQuery$variables;
};

const node: ConcreteRequest = (function(){
var v0 = [
  {
    "defaultValue": null,
    "kind": "LocalArgument",
    "name": "first"
  }
],
v1 = [
  {
    "alias": null,
    "args": [
      {
        "kind": "Variable",
        "name": "first",
        "variableName": "first"
      }
    ],
    "concreteType": "NoteConnection",
    "kind": "LinkedField",
    "name": "notes",
    "plural": false,
    "selections": [
      {
        "alias": null,
        "args": null,
        "concreteType": "NoteEdge",
        "kind": "LinkedField",
        "name": "edges",
        "plural": true,
        "selections": [
          {
            "alias": null,
            "args": null,
            "concreteType": "Note",
            "kind": "LinkedField",
            "name": "node",
            "plural": false,
            "selections": [
              {
                "alias": null,
                "args": null,
                "kind": "ScalarField",
                "name": "id",
                "storageKey": null
              },
              {
                "alias": null,
                "args": null,
                "kind": "ScalarField",
                "name": "content",
                "storageKey": null
              },
              {
                "alias": null,
                "args": null,
                "kind": "ScalarField",
                "name": "createdAt",
                "storageKey": null
              },
              {
                "alias": null,
                "args": null,
                "kind": "ScalarField",
                "name": "updatedAt",
                "storageKey": null
              }
            ],
            "storageKey": null
          }
        ],
        "storageKey": null
      },
      {
        "alias": null,
        "args": null,
        "concreteType": "PageInfo",
        "kind": "LinkedField",
        "name": "pageInfo",
        "plural": false,
        "selections": [
          {
            "alias": null,
            "args": null,
            "kind": "ScalarField",
            "name": "hasNextPage",
            "storageKey": null
          }
        ],
        "storageKey": null
      }
    ],
    "storageKey": null
  }
];
return {
  "fragment": {
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Fragment",
    "metadata": null,
    "name": "TodoListQuery",
    "selections": (v1/*: any*/),
    "type": "Query",
    "abstractKey": null
  },
  "kind": "Request",
  "operation": {
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Operation",
    "name": "TodoListQuery",
    "selections": (v1/*: any*/)
  },
  "params": {
    "cacheID": "d7ba992f05e38cf7d4d2d3b1d9314d3c",
    "id": null,
    "metadata": {},
    "name": "TodoListQuery",
    "operationKind": "query",
    "text": "query TodoListQuery(\n  $first: Int!\n) {\n  notes(first: $first) {\n    edges {\n      node {\n        id\n        content\n        createdAt\n        updatedAt\n      }\n    }\n    pageInfo {\n      hasNextPage\n    }\n  }\n}\n"
  }
};
})();

(node as any).hash = "6f53f4b729ad7a54434f416179b6af9f";

export default node;
