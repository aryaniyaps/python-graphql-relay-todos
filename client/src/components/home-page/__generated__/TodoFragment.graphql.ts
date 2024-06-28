/**
 * @generated SignedSource<<9ce645bd37b15e08deb7728cdcb33a93>>
 * @lightSyntaxTransform
 * @nogrep
 */

/* tslint:disable */
/* eslint-disable */
// @ts-nocheck

import { Fragment, ReaderFragment } from 'relay-runtime';
import { FragmentRefs } from "relay-runtime";
export type TodoFragment$data = {
  readonly completed: boolean;
  readonly content: string;
  readonly createdAt: any;
  readonly id: string;
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
};

(node as any).hash = "e701824aa0abe96c0c4edcd0253fe9ab";

export default node;
