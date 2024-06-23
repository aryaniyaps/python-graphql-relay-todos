/**
 * @generated SignedSource<<f6d7723e630ba24fdc09ed4b2b513a4f>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { ConcreteRequest, Mutation } from 'relay-runtime';
export type TodoControllerCreateMutation$variables = {
  content: string;
};
export type TodoControllerCreateMutation$data = {
  readonly createNote: {
    readonly content: string;
    readonly createdAt: any;
    readonly id: any;
    readonly updatedAt: any | null | undefined;
  };
};
export type TodoControllerCreateMutation = {
  response: TodoControllerCreateMutation$data;
  variables: TodoControllerCreateMutation$variables;
};

const node: ConcreteRequest = (function(){
var v0 = [
  {
    "defaultValue": null,
    "kind": "LocalArgument",
    "name": "content"
  }
],
v1 = [
  {
    "alias": null,
    "args": [
      {
        "kind": "Variable",
        "name": "content",
        "variableName": "content"
      }
    ],
    "concreteType": "Note",
    "kind": "LinkedField",
    "name": "createNote",
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
];
return {
  "fragment": {
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Fragment",
    "metadata": null,
    "name": "TodoControllerCreateMutation",
    "selections": (v1/*: any*/),
    "type": "Mutation",
    "abstractKey": null
  },
  "kind": "Request",
  "operation": {
    "argumentDefinitions": (v0/*: any*/),
    "kind": "Operation",
    "name": "TodoControllerCreateMutation",
    "selections": (v1/*: any*/)
  },
  "params": {
    "cacheID": "14676ec994fe5e23dca49586089a03a3",
    "id": null,
    "metadata": {},
    "name": "TodoControllerCreateMutation",
    "operationKind": "mutation",
    "text": "mutation TodoControllerCreateMutation(\n  $content: String!\n) {\n  createNote(content: $content) {\n    id\n    content\n    createdAt\n    updatedAt\n  }\n}\n"
  }
};
})();

(node as any).hash = "d8361e3708e7dd052054e7f2b6701677";

export default node;
