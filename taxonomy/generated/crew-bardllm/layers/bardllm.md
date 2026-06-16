# Bardllm layer

- **On-device, offline-first** (`BL-ONDEVICE`, prio 62) — Models run locally on the device; core function works with no network. Privacy by default — prompts and model I/O never leave the device, no prompt telemetry.
- **Ships the sliced ruleset** (`BL-RULESRUNNER`, prio 61) — bard-llm runs local models against a per-model rule slice (sizing law): the rule slice is shipped into the on-device model's context/system prompt. The taxonomy's composer output IS bard-llm's payload.
- **Apple platforms, native** (`BL-APPLE`, prio 60) — Ships iOS, iPadOS, macOS as a Universal (arm64) build; follows the Human Interface Guidelines; no private APIs.
- **On-device resource budgets** (`BL-RESOURCE`, prio 59) — Respect memory/battery/thermal ceilings; use quantized models sized to the device; degrade gracefully under memory pressure rather than crash.
- **App Store compliance** (`BL-STORE`, prio 58) — Unique monotonic CFBundleVersion per upload (stores reject reused build numbers); conforms to review guidelines; no remote code execution beyond on-device model inference.
