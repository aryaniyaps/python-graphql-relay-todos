/**
 * @generated SignedSource<<b8b555d454338485bf9239f18353e38c>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { ConcreteRequest, Mutation } from 'relay-runtime';
export type TodoDeleteMutation$variables = {
  todoId: any;
};
export type TodoDeleteMutation$data = {
  readonly deleteTodo: any | null | undefined;
};
export type TodoDeleteMutation = {
  response: TodoDeleteMutation$data;
  variables: TodoDeleteMutation$variables;
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
    "alias": null,
    "args": [
      {
        "kind": "Variable",
        "name": "todoId",
        "variableName": "todoId"
      }
    ],
    "kind": "ScalarField",
    "name": "deleteTodo",
    "storageKey": null
  }
];
return {
  "fragment": {
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Fragment",
    "metadata": null,
    "name": "TodoDeleteMutation",
    "selections": (v1/*: any*/),
    "type": "Mutation",
    "abstractKey": null
  },
  "kind": "Request",
  "operation": {
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Operation",
    "name": "TodoDeleteMutation",
    "selections": (v1/*: any*/)
  },
  "params": {
    "cacheID": "553933d2bc0e7fcc757612f6fe8b32e9",
    "id": null,
    "metadata": {},
    "name": "TodoDeleteMutation",
    "operationKind": "mutation",
    "text": "mutation TodoDeleteMutation(\n  $todoId: GlobalID!\n) {\n  deleteTodo(todoId: $todoId)\n}\n"
  }
};
})();

(node as any).hash = "e6b354d4ed0ab9e588fa74d5a1250cbd";

export default node;
