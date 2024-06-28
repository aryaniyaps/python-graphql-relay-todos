/**
 * @generated SignedSource<<ae4c5fb2b03b27e334b844b9b1123442>>
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
    readonly todo: {
      readonly " $fragmentSpreads": FragmentRefs<"TodoFragment">;
    };
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
];
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
        "concreteType": "ToggleTodoCompletedPayload",
        "kind": "LinkedField",
        "name": "toggleTodoCompleted",
        "plural": false,
        "selections": [
          {
            "alias": null,
            "args": null,
            "concreteType": "Todo",
            "kind": "LinkedField",
            "name": "todo",
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
        "concreteType": "ToggleTodoCompletedPayload",
        "kind": "LinkedField",
        "name": "toggleTodoCompleted",
        "plural": false,
        "selections": [
          {
            "alias": null,
            "args": null,
            "concreteType": "Todo",
            "kind": "LinkedField",
            "name": "todo",
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
      }
    ]
  },
  "params": {
    "cacheID": "e3cf7f8998462f435a80013de63cbf0d",
    "id": null,
    "metadata": {},
    "name": "TodoToggleCompleteMutation",
    "operationKind": "mutation",
    "text": "mutation TodoToggleCompleteMutation(\n  $todoId: ID!\n) {\n  toggleTodoCompleted(todoId: $todoId) {\n    todo {\n      ...TodoFragment\n      id\n    }\n  }\n}\n\nfragment TodoFragment on Todo {\n  id\n  content\n  completed\n  createdAt\n  updatedAt\n}\n"
  }
};
})();

(node as any).hash = "8764b6d695a1cc21b40aaa799cb5cf02";

export default node;
