## [0.8.0] - 10-09-2026

### Changed

* Validator sequences (`ValidatorsData`, `ValidatorsStatistics`, epoch mark
  `validators`) and verdict `votes` are bounded sequences instead of fixed-size
  sequences. `WorkPackageSpec` records the number of erasure shards
  (`erasure-shards`).
  (GP [#514](https://github.com/gavofyork/graypaper/pull/514),
  [#527](https://github.com/gavofyork/graypaper/pull/527))
* `RefineContext` carries `anchor-slot` and `lookup-anchor-state-root`.
  Recent blocks history items carry the block `slot`.
  (GP [#526](https://github.com/gavofyork/graypaper/pull/526))
* Availability assignments hold the full `ReportGuarantee` and the
  `registered-slot` instead of the bare work report and a timeout.
  (GP [#494](https://github.com/gavofyork/graypaper/pull/494))
* Service accumulation statistics carry `accumulate-transfer-count`.
  New accumulate vector `transfer_for_live_service`.
  (GP [#502](https://github.com/gavofyork/graypaper/pull/502))
* Disputes: removed the two-culprits minimum for `bad` verdicts. The
  `not-enough-culprits` error is gone and the error codes are renumbered
  (see `stf/disputes/disputes.asn`).
  (GP [#525](https://github.com/gavofyork/graypaper/pull/525))
* New PVM gas cost model, `sbrk` instruction removed, `grow_heap` host call
  added, host calls priced per the GP gas table. Accumulate vectors and block
  import traces are regenerated with the new costs (see `traces/README.md`).
  (GP [#508](https://github.com/gavofyork/graypaper/pull/508),
  [#517](https://github.com/gavofyork/graypaper/pull/517))
* Extrinsic hash: preimages contribute as `(requester, hash)` pairs rather
  than full `(requester, blob)` entries.
  (GP [#524](https://github.com/gavofyork/graypaper/pull/524))
* Block import traces: all suites regenerated for 0.8.0.

### Fixes

* Trie vectors: node type discriminators moved to the most significant bits
  of the head byte, key bits consumed most significant bit first.

### Deviations

* `grow_heap` out-of-gas handling follows GP
  [#533](https://github.com/gavofyork/graypaper/pull/533): when the remaining
  gas cannot cover the call cost the gas counter is drained to zero and the
  call exits out-of-gas.
* `grow_heap` address-space limit rounds the stack reservation up to the
  64 KiB zone size, as per GP
  [#538](https://github.com/gavofyork/graypaper/pull/538).

## [0.7.2] - 01-12-2025

### Changed

* Accumulation statistics include the services accumulated for free or due
  to transfers. Listed as a deviation in 0.7.1, now the specified behavior.
  (GP [#484](https://github.com/gavofyork/graypaper/pull/484))
* Simplify `fetch` host call case 8: fetch only the authorizer config blob.
  (GP [#486](https://github.com/gavofyork/graypaper/pull/486))
* PVM invocations: correct gas charge for `transfer` host call failures.
  (GP [#488](https://github.com/gavofyork/graypaper/pull/488))
* Fix max size of concatenated variable-size blobs, extrinsics and imported
  segments of a work package.
  (GP [#493](https://github.com/gavofyork/graypaper/pull/493))
* Accumulate vectors: the `log` host call is charged 10 gas
  ([JIP-1](https://github.com/polkadot-fellows/JIPs/blob/main/JIP-1.md)).
* Accumulate and reports STF vectors regenerated for protocol version 0.7.2.
* ASN.1: `Account` renamed to `ServiceAccount`. The preimage maps are now
  `preimage-blobs` (`PreimagesBlobMapEntry`) and `preimage-requests`
  (`PreimagesRequestsMapEntry`, keyed by hash and length, value bounded to
  three timeslots). Applies to the accumulate and preimages STF vectors.
* Reports: new error code `missing-work-results` (25) and new vector
  `report_with_no_results`. ASN.1 validation skips this vector because its
  empty results sequence violates the schema bounds.
* Block import traces regenerated.

## [0.7.1] - 08-10-2025

### Changed

* Remove `on_transfer` from service statistics
  (GP [#457](https://github.com/gavofyork/graypaper/pull/457))
* Serialization: Include version byte prefix for accounts
  (GP [#472](https://github.com/gavofyork/graypaper/pull/472))
* Registrar service privilege
  (GP [#473](https://github.com/gavofyork/graypaper/pull/473))
* Add preimage provision status to the `Account`s structure of
  accumulate `StfState` (see ASN.1 syntax).

### Deviations

* Accumulation statistics for services accumulation are updated
  according to version 0.7.2. In 0.7.2, service stats need to be
  updated when any service accumulation logic has been executed.
  (https://graypaper.fluffylabs.dev/#/ab2cdbd/18e60318e603?v=0.7.2)

## [0.7.0] - 26-08-2025

### Changed

* Serialization: Move all variable-length items to end of encoding
  (GP [#418](https://github.com/gavofyork/graypaper/pull/418))
* Rearrange the items in `CoreActivityRecord` and `ServiceActivityRecord`,
  refer to the ASN.1 schema and GP (no explicit GP PR).

## [0.6.7] - 07-08-2025

### Changed

* Rearrange the inner PVM page admin
  (GP [#402](https://github.com/gavofyork/graypaper/pull/402))
* PVM pages can change access without clearing
  (GP [#404](https://github.com/gavofyork/graypaper/pull/404))
* Renumber host-calls [#715](https://github.com/paritytech/polkajam/pull/715)
  (GP [#408](https://github.com/gavofyork/graypaper/pull/408))
* `info` host call uses fixed length types
  (GP [#410](https://github.com/gavofyork/graypaper/pull/410))
* Accounts storage deposit offset and additional metadata
  (GP [#397](https://github.com/gavofyork/graypaper/pull/397)
   and [#400](https://github.com/gavofyork/graypaper/pull/400))
* Core assignment privileges is a sequence, one item per core
  (GP [#393](https://github.com/gavofyork/graypaper/pull/393))
* Most recent accumulation outputs are stored in state; Recent blocks history now stores
  the MMR roots only, the full MMR structure relative to the last accumulation is kept
  separately (GP [#405](https://github.com/gavofyork/graypaper/pull/405))
* New bundle size limit (GP [#407](https://github.com/gavofyork/graypaper/pull/407))

## [0.6.6] - 25-06-2025

### Changed

- Codebase reorganization
- Binary to JSON conversion scripts and utilities
* Extended the `fetch` host call with new variants.
* Updated numeric identifiers used in `fetch`.
* Updated numeric identifiers for PVM errors.
* PVM wrangled operands changed.
* Removed the traces `000...000.bin/json` step, as it was not a valid trace step
  and was intended to be handled specially for genesis. Since it shared the same
  format as regular trace steps, it could be ambiguous or misleading.
* Introduced an explicit `genesis.bin` file containing the genesis state and header.
* The *authorizer trace* field has been moved to the end of the accumulation
  operand encoding (C.29)

### Deviations

* `fetch` host call for protocol parameters ($\omega_{10}=0$) has been implemented
  according to this (currently) unreleased change: https://github.com/gavofyork/graypaper/pull/414
  For the `fetch` hostcall id we're still using 18 as per GP 0.6.6. The picked
  change only concerns the value returned for w_10=0

### Extra

* Codebase reorganization
* Binary to JSON conversion scripts and utilities
* CI: ASN.1 verification

## [0.6.5] - 02-06-2025

- First Release
