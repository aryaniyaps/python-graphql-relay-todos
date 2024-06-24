/**
 * @generated SignedSource<<a91027f78d65a07eadc02c30d02911cc>>
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
  readonly createTodo: {
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
    "concreteType": "Todo",
    "kind": "LinkedField",
    "name": "createTodo",
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
    "cacheID": "de8b414ad517265ebb752ff530d3fdf5",
    "id": null,
    "metadata": {},
    "name": "TodoControllerCreateMutation",
    "operationKind": "mutation",
    "text": "mutation TodoControllerCreateMutation(\n  $content: String!\n) {\n  createTodo(content: $content) {\n    id\n    content\n    createdAt\n    updatedAt\n  }\n}\n"
  }
};
})();

(node as any).hash = "64286bb13e5cdfdb683b88282f72b21f";

export default node;
