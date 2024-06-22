/**
 * @generated SignedSource<<57a858550105ad8cc27290f0b7d61ae6>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { ConcreteRequest, Mutation } from 'relay-runtime';
export type TodoDeleteMutation$variables = {
  noteId: string;
};
export type TodoDeleteMutation$data = {
  readonly deleteNote: {
    readonly id: string;
  };
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
    "name": "noteId"
  }
],
v1 = [
  {
    "alias": null,
    "args": [
      {
        "kind": "Variable",
        "name": "noteId",
        "variableName": "noteId"
      }
    ],
    "concreteType": "Note",
    "kind": "LinkedField",
    "name": "deleteNote",
    "plural": false,
    "selections": [
      {
        "alias": null,
        "args": null,
        "kind": "ScalarField",
        "name": "id",
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
    "cacheID": "2be5da13a42938046eab82d6f155d65d",
    "id": null,
    "metadata": {},
    "name": "TodoDeleteMutation",
    "operationKind": "mutation",
    "text": "mutation TodoDeleteMutation(\n  $noteId: String!\n) {\n  deleteNote(noteId: $noteId) {\n    id\n  }\n}\n"
  }
};
})();

(node as any).hash = "ea721afaaa5aa524b3410c3672de089a";

export default node;
