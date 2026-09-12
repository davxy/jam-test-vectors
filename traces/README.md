# Block Import Traces

Import full blocks starting from genesis, implementing the complete logic
required of a block importer that complies with the specifications outlined
in Graypaper Milestone 1 (M1).

## Chainspec

The traces vectors are provided for **tiny** configuration only.

## Schema

The schema is designed to be sufficiently generic to allow easy processing by
any implementation aiming to undergo conformance testing.

Both the binary and json formats adhere to the overarching JAM protocol ASN.1
[schema](../jam-types-asn/jam-types.asn), as well as the specific vectors
[schema](./schema.asn) defined for these test cases.

## Gas Costs

Instruction gas costs follow the GP 0.8.0 gas cost model
(GP [#508](https://github.com/gavofyork/graypaper/pull/508)), as implemented by the
PolkaVM `Full` cost model with the `L2Hit` cache model.

Host-call gas costs follow the GP 0.8.0 host-call gas table
(GP [#517](https://github.com/gavofyork/graypaper/pull/517)), including the
`grow_heap` host call introduced by GP #508.

The `log` host call ([JIP-1](https://github.com/polkadot-fellows/JIPs/blob/main/JIP-1.md))
is not defined by the GP and is charged as an unknown host call: **1000** gas.

## Vectors

- [Fallback](./fallback): fallback block authoring, no work reports.
- [Safrole](./safrole): safrole block authoring, no work reports.
- [Storage](./storage): no-safrole, service storage related work reports, max 6 work items per report.
- [Storage Light](./storage_light): no-safrole, service related work reports, max 1 work item per report.
- [Preimages](./preimages): no-safrole, preimages related work reports, max 6 work items per report.
- [Preimages Light](./preimages_light): no-safrole, preimages related work reports, max 1 work item per report.
- [Fuzzy](./fuzzy): no-safrole, fuzzy service, random fuzzy service profile, max 6 work item per report.
- [Fuzzy Light](./fuzzy_light): no-safrole, fuzzy service, empty fuzzy service profile, max 1 work item per report.

## Preimage Expunge Delay

The GP defines a constant `D`, representing the number of timeslots after which
an unreferenced preimage may be expunged.

In the `full` configuration, the GP mandates `D = 19,200`, which corresponds to
exactly 32 full epochs (`E = 600`). Applying the same logic to the `tiny`
configuration, where `E = 12`, would yield `D = 12 × 32 = 384` slots.

However, this value is too large for a constrained set of test vectors with very
few blocks. For testing purposes, we have therefore chosen to use **`D = 32`**
instead.

**The final value of `D` for the `tiny` testnet remains undecided**,
and should be documented in the community-maintained
[chain spec documentation](https://docs.jamcha.in/basics/chain-spec/tiny) once determined.
