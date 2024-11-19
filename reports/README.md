# Work Reports STF Test Vectors

We offer two types of test vectors:

- Tiny: These are designed for quick adjustments and prototyping, with reduced validators (6)
  and cores (2) count. They are provided in both JSON format for easy inspection
  and modification, and in SCALE format, which is the production binary codec.

- Full: These vectors use production validators (1023) and cores (341) count.
  Similar to the tiny vectors, they are available in JSON and SCALE format.

Both JSON and SCALE formats conform to the specified ASN.1 schema provided [here](./reports.asn).

## Error Output

On execution error, post-state must match pre-state.

Possible error codes returned as output are not part of the specification,
feel free to ignore actual numeric values.

A map for errors codes semantics used by for the test vectors is given in the ASN.1 schema.

## Tiny Vectors

- [report_curr_rotation](./tiny/report_curr_rotation-1.json) 🟢
  - Report uses current guarantors rotation.
- [report_prev_rotation](./tiny/report_prev_rotation-1.json) 🟢
  - Report uses previous guarantors rotation.
  - Previous rotation falls within previous epoch, thus previous epoch validators
    set is used to construct report core assignment to pick expected guarantors.
- [multiple_reports](./tiny/multiple_reports-1.json) 🟢
  - Multiple good work reports.
- [anchor_not_recent](./tiny/anchor_not_recent-1.json) 🔴
  - Context anchor is not recent enough.
- [bad_beefy_mmr](./tiny/bad_beefy_mmr-1.json) 🔴
  - Context Beefy MMR root doesn't match the one at anchor.
- [bad_code_hash](./tiny/bad_code_hash-1.json) 🔴
  - Work result code hash doesn't match the one expected for the service.
- [bad_core_index](./tiny/bad_core_index-1.json) 🔴
  - Core index is too big.
- [bad_service_id](./tiny/bad_service_id-1.json) 🔴
  - Work result service identifier doesn't have any associated account in state.
- [bad_state_root](./tiny/bad_state_root-1.json) 🔴
  - Context state root doesn't match the one at anchor.
- [bad_validator_index](./tiny/bad_validator_index-1.json) 🔴
  - Validator index is too big.
- [consume_authorization_once](./tiny/consume_authorization_once-1.json) 🔴
  - Multiple authorizers are available for the same work report.
  - Only one is consumed. 
- [core_engaged](./tiny/core_engaged-1.json) 🔴
  - A core is not available.
- [dependency_missing](./tiny/dependency_missing-1.json) 🔴
  - Prerequisite is missing.
- [duplicate_package_in_recent_history](./tiny/duplicate_package_in_recent_history-1.json) 🔴
  - Package was already available in recent history.
- [duplicated_package_in_report](./tiny/duplicated_package_in_report-1.json) 🔴
  - Report contains a duplicate package.
- [future_report_slot](./tiny/future_report_slot-1.json) 🔴
  - Report refers to a slot in the future with respect to container block slot.
- [bad_signature](./tiny/bad_signature-1.json) 🔴
  - Invalid report guarantee signature.
- [high_work_report_gas](./tiny/high_work_report_gas-1.json) 🟢
  - Work report per core gas is very high, still less than the limit.
- [too_high_work_report_gas](./tiny/too_high_work_report_gas-1.json) 🔴
  - Work report per core gas is too much high.
- [many_dependencies](./tiny/many_dependencies-1.json) 🟢
  - Work report has many dependencies, still less than the limit.
- [too_many_dependencies](./tiny/too_many_dependencies-1.json) 🔴
  - Work report has too many dependencies.
- [no_enough_guarantees](./tiny/no_enough_guarantees-1.json) 🔴
  - Report with no enough guarantors signatures.
- [not_authorized](./tiny/not_authorized-1.json) 🔴
  - Target core without any authorizer.
- [not_authorized](./tiny/not_authorized-2.json) 🔴
  - Target core with unexpected authorizer.
- [not_sorted_guarantor](./tiny/not_sorted_guarantor-1.json) 🔴
  - Guarantors indices are not sorted or unique.
- [out_of_order_guarantees](./tiny/out_of_order_guarantees-1.json) 🔴
  - Reports cores are not sorted or unique.
- [report_before_last_rotation](./tiny/report_before_last_rotation-1.json) 🔴
  - Report guarantee slot is too old with respect to block slot.
- [reports_with_dependencies](./tiny/reports_with_dependencies-1.json) 🟢
  - Simple report dependency satisfied by another work report in the same
    extrinsic. 
- [reports_with_dependencies](./tiny/reports_with_dependencies-2.json) 🟢
  - Work reports mutual dependency (indirect self-referential dependencies).
- [reports_with_dependencies](./tiny/reports_with_dependencies-3.json) 🟢
  - Work report direct self-referential dependency.
- [reports_with_dependencies](./tiny/reports_with_dependencies-4.json) 🟢
  - Work report dependency satisfied by recent blocks history.
- [reports_with_dependencies](./tiny/reports_with_dependencies-5.json) 🟢
  - Work report segments tree root lookup dependency satisfied by another
    work report in the same extrinsic.
- [reports_with_dependencies](./tiny/reports_with_dependencies-6.json) 🟢
  - Work report segments tree root lookup dependency satisfied by recent
    blocks history.
- [segment_root_lookup_invalid](./tiny/segment_root_lookup_invalid-1.json) 🔴
  - Segments tree root lookup item not found in recent blocks history.
- [segment_root_lookup_invalid](./tiny/segment_root_lookup_invalid-2.json) 🔴
  - Segments tree root lookup item found in recent blocks history but with
    an unexpected value.
- [wrong_assignment](./tiny/wrong_assignment-1.json) 🔴
  - Unexpected guarantor for work report core.

## Full Vectors

Currently, the same test cases as tiny vectors but at a larger scale.