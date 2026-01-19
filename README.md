# Epoch Light Theme

**Epoch Light** is a minimalist, high-clarity browser theme suite designed for engineers who value focus.

It reduces visual latency and cognitive load by removing decorative noise and utilizing a low-saturation, high-contrast palette (`#E0E2E5`).

## Installation

### Option 1: One-Click Install (Recommended)
Add it directly from the official Firefox Add-ons Store:

[![Get Epoch Light](https://blog.mozilla.org/addons/files/2020/04/get-the-addon-fx-apr-2020.svg)](https://addons.mozilla.org/en-US/firefox/addon/epoch-light/)

### Option 2: Manual Build
If you prefer to build from source or use a specific release version:
1. Download the latest `.zip` from [Releases](../../releases).
2. Go to `about:addons` in Firefox.
3. Click the Gear icon ⚙️ -> "Install Add-on From File...".
4. Select the `.zip` file.

## The Engineering
Unlike standard themes, Epoch is treated as a software artifact:
- **Reproducible:** Managed via `uv` and Python.
- **Procedural:** Assets are generated via code (Lanczos resampling), not manual editing.
- **Automated:** CI/CD pipelines handle packaging.

## The Epoch Suite
- [x] **Epoch Light** (Firefox Theme)
- [ ] **Epoch Focus** (New Tab Extension - *In Review*)
- [ ] VS Code (Coming Soon)
- [ ] Terminal (Coming Soon)

---
*Built by [Sumit Nautiyal](https://thecsjourney.com)*