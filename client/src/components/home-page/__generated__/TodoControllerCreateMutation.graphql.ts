/**
 * @generated SignedSource<<f3ebd057dca58340b239822859321d97>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { ConcreteRequest, Mutation } from 'relay-runtime';
import { FragmentRefs } from "relay-runtime";
export type TodoControllerCreateMutation$variables = {
  connections: ReadonlyArray<string>;
  content: string;
};
export type TodoControllerCreateMutation$data = {
  readonly createTodo: {
    readonly todoEdge: {
      readonly node: {
        readonly " $fragmentSpreads": FragmentRefs<"TodoFragment">;
      };
    };
  };
};
export type TodoControllerCreateMutation = {
  response: TodoControllerCreateMutation$data;
  variables: TodoControllerCreateMutation$variables;
};

const node: ConcreteRequest = (function(){
var v0 = {
  "defaultValue": null,
  "kind": "LocalArgument",
  "name": "connections"
},
v1 = {
  "defaultValue": null,
  "kind": "LocalArgument",
  "name": "content"
},
v2 = [
  {
    "kind": "Variable",
    "name": "content",
    "variableName": "content"
  }
];
return {
  "fragment": {
    "argumentDefinitions": [
      (v0/*: any*/),
      (v1/*: any*/)
    ],
    "kind": "Fragment",
    "metadata": null,
    "name": "TodoControllerCreateMutation",
    "selections": [
      {
        "alias": null,
        "args": (v2/*: any*/),
        "concreteType": "CreateTodoPayload",
        "kind": "LinkedField",
        "name": "createTodo",
        "plural": false,
        "selections": [
          {
            "alias": null,
            "args": null,
            "concreteType": "TodoEdge",
            "kind": "LinkedField",
            "name": "todoEdge",
            "plural": false,
            "selections": [
              {
                "alias": null,
                "args": null,
                "concreteType": "Todo",
                "kind": "LinkedField",
                "name": "node",
                "plural": false,
                "selections": [
                  {
                    "args": null,
                    "kind": "FragmentSpread",
                    "name": "TodoFragment"
                  }
                ],
                "storageKey": null
              }
            ],
            "storageKey": null
          }
        ],
        "storageKey": null
      }
    ],
    "type": "Mutation",
    "abstractKey": null
  },
  "kind": "Request",
  "operation": {
    "argumentDefinitions": [
      (v1/*: any*/),
      (v0/*: any*/)
    ],
    "kind": "Operation",
    "name": "TodoControllerCreateMutation",
    "selections": [
      {
        "alias": null,
        "args": (v2/*: any*/),
        "concreteType": "CreateTodoPayload",
        "kind": "LinkedField",
        "name": "createTodo",
        "plural": false,
        "selections": [
          {
            "alias": null,
            "args": null,
            "concreteType": "TodoEdge",
            "kind": "LinkedField",
            "name": "todoEdge",
            "plural": false,
            "selections": [
              {
                "alias": null,
                "args": null,
                "concreteType": "Todo",
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
                    "name": "completed",
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
            "filters": null,
            "handle": "prependEdge",
            "key": "",
            "kind": "LinkedHandle",
            "name": "todoEdge",
            "handleArgs": [
              {
                "kind": "Variable",
                "name": "connections",
                "variableName": "connections"
              }
            ]
          }
        ],
        "storageKey": null
      }
    ]
  },
  "params": {
    "cacheID": "391da1a17dde71fde2d05fc83ea1264f",
    "id": null,
    "metadata": {},
    "name": "TodoControllerCreateMutation",
    "operationKind": "mutation",
    "text": "mutation TodoControllerCreateMutation(\n  $content: String!\n) {\n  createTodo(content: $content) {\n    todoEdge {\n      node {\n        ...TodoFragment\n        id\n      }\n    }\n  }\n}\n\nfragment TodoFragment on Todo {\n  id\n  content\n  completed\n  createdAt\n  updatedAt\n}\n"
  }
};
})();

(node as any).hash = "cd62480730e0e573d88dbbe68f982d0d";

export default node;
