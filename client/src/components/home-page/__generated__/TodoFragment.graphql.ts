/**
 * @generated SignedSource<<0c8c6e375b5801c41114508d7a0df199>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { Fragment, ReaderFragment } from 'relay-runtime';
import { FragmentRefs } from "relay-runtime";
export type TodoFragment$data = {
  readonly content: string;
  readonly createdAt: any;
  readonly id: any;
  readonly updatedAt: any | null | undefined;
  readonly " $fragmentType": "TodoFragment";
};
export type TodoFragment$key = {
  readonly " $data"?: TodoFragment$data;
  readonly " $fragmentSpreads": FragmentRefs<"TodoFragment">;
};

const node: ReaderFragment = {
  "argumentDefinitions": [],
  "kind": "Fragment",
  "metadata": null,
  "name": "TodoFragment",
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
  "type": "Todo",
  "abstractKey": null
};

(node as any).hash = "646a639f1ae945ad2c442802282d3357";

export default node;