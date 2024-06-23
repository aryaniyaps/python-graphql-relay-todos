/**
 * @generated SignedSource<<0d62b7802e7d0191fdf9e9e876928564>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { ConcreteRequest, Mutation } from 'relay-runtime';
export type TodoDeleteMutation$variables = {
  noteId: any;
};
export type TodoDeleteMutation$data = {
  readonly deleteNote: any | null | undefined;
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
    "kind": "ScalarField",
    "name": "deleteNote",
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
    "cacheID": "74f725e48f2d831b2a62ad7d7b21012f",
    "id": null,
    "metadata": {},
    "name": "TodoDeleteMutation",
    "operationKind": "mutation",
    "text": "mutation TodoDeleteMutation(\n  $noteId: GlobalID!\n) {\n  deleteNote(noteId: $noteId)\n}\n"
  }
};
})();

(node as any).hash = "cc81b0a4a33cb83f7ed2bded60900cca";

export default node;
