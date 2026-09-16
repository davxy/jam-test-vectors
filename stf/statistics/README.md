# Validators Statistics STF Test Vectors

## Schema

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./statistics.asn) defined for these test cases.

## Validators Statistics

These vectors exclusively contribute to updating validator-related statistics
($π_V$ and $π_L$).

In contrast, service and core statistics ($π_S$ and $π_C$) are updated by
vectors that more directly influence the state changes relevant to those
metrics (i.e. see [preimages](../preimages/README.md#statistics),
[reports](../reports/README.md#statistics) and
[accumulate](../accumulate/README.md#statistics)).

## ⚠️Extrinsic Semantic Validity

These vectors are intended just to advance the statistics of validators.
Most of the content of the extrinsic is irrelevant and primarily consists of placeholder data.

## Tiny Vectors

- [stats_with_empty_extrinsic-1](./tiny/stats_with_empty_extrinsic-1.json) 🟢
  - Empty extrinsic with no epoch change.
  - Only author blocks counter is incremented.
- [stats_with_epoch_change-1](./tiny/stats_with_epoch_change-1.json) 🟢
  - Misc extrinsic information with no epoch change.
  - See "Extrinsic Semantic Validity" section.
- [stats_with_some_extrinsic-1](./tiny/stats_with_some_extrinsic-1.json) 🟢
  - Misc extrinsic information with no epoch change.
  - See "Extrinsic Semantic Validity" section.
- [stats_epoch_change_with_set_resize-1](./tiny/stats_epoch_change_with_set_resize-1.json) 🟢
  - Epoch change with an assurance from the last validator of the prior set.
  - Assurances are credited to the outgoing accumulator, which becomes the last epoch snapshot.
  - Under the tiny spec the set size is unchanged.

## Full Vectors

The same test cases as tiny vectors but at a larger scale, with one difference.

- [stats_epoch_change_with_set_resize-1](./full/stats_epoch_change_with_set_resize-1.json) 🟢
  - The active validators set shrinks to the minimum size at the epoch change.
  - The fresh accumulator is sized by the new set, the snapshot keeps the prior size.
  - The assurer index is beyond the new set size and is credited in the snapshot.
