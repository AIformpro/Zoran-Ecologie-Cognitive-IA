# Zoran — GitHub Auto-Publish Workflows

Two ways to publish files that ChatGPT (or any tool) generated **without giving tokens** to external services.

## Option A — Manual URL Import (recommended)
1. Upload your ZIP to a **public URL** (e.g., GitHub Release asset, public S3, Dropbox direct link).
2. In your repo → **Actions** → **Import ZIP into repo** → **Run workflow**.
3. Provide:
   - `zip_url`: the public link.
   - `target_subdir` (optional): where to land files.
   - Choose `create_branch=true` to review via PR, or set to false to push to default branch.

## Option B — Push ZIP to `_inbox/`
1. Commit any ZIP to the repo’s `_inbox/` directory.
2. The workflow auto-extracts and syncs contents to the repo root (excluding `.github/workflows/`).

## Safety Notes
- Workflows use repo `GITHUB_TOKEN` with `contents: write` only.
- `.github/workflows/` is **excluded** from imports to avoid pipeline hijacking.
- Default behavior: flatten one top-level folder inside the ZIP.

## Files
- `.github/workflows/import-zip.yml` — manual import from URL.
- `.github/workflows/inbox-autodeploy.yml` — auto-deploy on ZIP pushed to `_inbox/`.
- `scripts/flatten.sh` — utility (not required).

## Typical Flow with ChatGPT
- ChatGPT gives you a ZIP (download locally).
- **Either**: upload ZIP to a public place and use **Option A**.
- **Or**: commit ZIP to `_inbox/` and push — **Option B** imports automatically.

— MIT License
