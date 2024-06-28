/**
 * @generated SignedSource<<6ff9d3513a985fb5a4cb850ea489460f>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { ConcreteRequest, Mutation } from 'relay-runtime';
export type TodoDeleteMutation$variables = {
  connections: ReadonlyArray<string>;
  todoId: string;
};
export type TodoDeleteMutation$data = {
  readonly deleteTodo: {
    readonly deletedTodoId: string | null | undefined;
  };
};
export type TodoDeleteMutation = {
  response: TodoDeleteMutation$data;
  variables: TodoDeleteMutation$variables;
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
  "name": "todoId"
},
v2 = [
  {
    "kind": "Variable",
    "name": "todoId",
    "variableName": "todoId"
  }
],
v3 = {
  "alias": null,
  "args": null,
  "kind": "ScalarField",
  "name": "deletedTodoId",
  "storageKey": null
};
return {
  "fragment": {
    "argumentDefinitions": [
      (v0/*: any*/),
      (v1/*: any*/)
    ],
    "kind": "Fragment",
    "metadata": null,
    "name": "TodoDeleteMutation",
    "selections": [
      {
        "alias": null,
        "args": (v2/*: any*/),
        "concreteType": "DeleteTodoPayload",
        "kind": "LinkedField",
        "name": "deleteTodo",
        "plural": false,
        "selections": [
          (v3/*: any*/)
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
    "name": "TodoDeleteMutation",
    "selections": [
      {
        "alias": null,
        "args": (v2/*: any*/),
        "concreteType": "DeleteTodoPayload",
        "kind": "LinkedField",
        "name": "deleteTodo",
        "plural": false,
        "selections": [
          (v3/*: any*/),
          {
            "alias": null,
            "args": null,
            "filters": null,
            "handle": "deleteEdge",
            "key": "",
            "kind": "ScalarHandle",
            "name": "deletedTodoId",
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
    "cacheID": "7aa4fb975e8bb44c3fa9079110ceed86",
    "id": null,
    "metadata": {},
    "name": "TodoDeleteMutation",
    "operationKind": "mutation",
    "text": "mutation TodoDeleteMutation(\n  $todoId: ID!\n) {\n  deleteTodo(todoId: $todoId) {\n    deletedTodoId\n  }\n}\n"
  }
};
})();

(node as any).hash = "47c134b2a6ca1cf237ce202f1d00568c";

export default node;
