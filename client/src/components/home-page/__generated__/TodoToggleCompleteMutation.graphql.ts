/**
 * @generated SignedSource<<079d1c0a637ccb401e7387ee22d22d57>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { ConcreteRequest, Mutation } from 'relay-runtime';
import { FragmentRefs } from "relay-runtime";
export type TodoToggleCompleteMutation$variables = {
  todoId: string;
};
export type TodoToggleCompleteMutation$data = {
  readonly toggleTodoCompleted: {
    readonly " $fragmentSpreads": FragmentRefs<"TodoFragment">;
  };
};
export type TodoToggleCompleteMutation = {
  response: TodoToggleCompleteMutation$data;
  variables: TodoToggleCompleteMutation$variables;
};

const node: ConcreteRequest = (function(){
var v0 = [
  {
    "defaultValue": null,
    "kind": "LocalArgument",
    "name": "todoId"
  }
],
v1 = [
  {
    "kind": "Variable",
    "name": "todoId",
    "variableName": "todoId"
  }
],
v2 = {
  "alias": null,
  "args": null,
  "kind": "ScalarField",
  "name": "id",
  "storageKey": null
};
return {
  "fragment": {
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Fragment",
    "metadata": null,
    "name": "TodoToggleCompleteMutation",
    "selections": [
      {
        "alias": null,
        "args": (v1/*: any*/),
        "concreteType": null,
        "kind": "LinkedField",
        "name": "toggleTodoCompleted",
        "plural": false,
        "selections": [
          {
            "kind": "InlineFragment",
            "selections": [
              {
                "args": null,
                "kind": "FragmentSpread",
                "name": "TodoFragment"
              }
            ],
            "type": "Todo",
            "abstractKey": null
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
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Operation",
    "name": "TodoToggleCompleteMutation",
    "selections": [
      {
        "alias": null,
        "args": (v1/*: any*/),
        "concreteType": null,
        "kind": "LinkedField",
        "name": "toggleTodoCompleted",
        "plural": false,
        "selections": [
          {
            "alias": null,
            "args": null,
            "kind": "ScalarField",
            "name": "__typename",
            "storageKey": null
          },
          {
            "kind": "InlineFragment",
            "selections": [
              (v2/*: any*/),
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
            "type": "Todo",
            "abstractKey": null
          },
          {
            "kind": "InlineFragment",
            "selections": [
              (v2/*: any*/)
            ],
            "type": "Node",
            "abstractKey": "__isNode"
          }
        ],
        "storageKey": null
      }
    ]
  },
  "params": {
    "cacheID": "e892be72b1b91fd463e8910b031d82f1",
    "id": null,
    "metadata": {},
    "name": "TodoToggleCompleteMutation",
    "operationKind": "mutation",
    "text": "mutation TodoToggleCompleteMutation(\n  $todoId: ID!\n) {\n  toggleTodoCompleted(todoId: $todoId) {\n    __typename\n    ... on Todo {\n      ...TodoFragment\n    }\n    ... on Node {\n      __isNode: __typename\n      id\n    }\n  }\n}\n\nfragment TodoFragment on Todo {\n  id\n  content\n  completed\n  createdAt\n  updatedAt\n}\n"
  }
};
})();

(node as any).hash = "2b3c7afd5491b9988135e656391edcc3";

export default node;
