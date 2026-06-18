# Bardinfra layer

- **Ansible owns the fleet** (`BI-FLEET`, prio 62) — Every node is under declarative Ansible control; the inventory lives in the repo; plays are idempotent and safe to re-run, converging any node to the same state.
- **Vault-encrypted creds in-repo** (`BI-VAULT`, prio 61) — Connectivity config and ansible-vault-ENCRYPTED credentials live in the testbed-project repo — encrypted blobs only, never plaintext passwords in git (AX-NOSECRET). Rotate on schedule; least privilege per node (AX-LEASTPRIV).
- **Graded connectivity rubric** (`BI-CONN`, prio 60) — Prove each node reachable+ready before use, graded not vibed: SSH up, vault decrypts, Ansible ping/play converges, health endpoint green, a representative request succeeds.
- **Nodes reproducible from the repo** (`BI-REPRO`, prio 59) — A node is a git clone + ansible-playbook away; nothing important lives only on a box. Reimage and rebuild deterministically (headless, script-everything — AX-HEADLESS).
- **OpenShift-first, portable plays** (`BI-PORTABLE`, prio 58) — The same plays target on-prem or GCloud with inventory/vars only — never play changes. Cloud-native by config, not by fork.
- **Show every node's IPv4 + IPv6** (`BI-ADDR`, prio 57) — The fleet view surfaces each node's IPv4 and IPv6 addresses, both local and bardnet (Tailnet). IPv6 is first-class, not an afterthought.
