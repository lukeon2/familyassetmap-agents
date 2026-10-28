from pathlib import Path
import json, zipfile
root = Path(__file__).resolve().parents[1]
plugin = root / "plugins/familyassetmap-codex"
manifest = json.loads((plugin / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
assert manifest["name"] == "familyassetmap"
assert len(manifest["interface"]["displayName"]) <= 30
assert len(manifest["interface"]["shortDescription"]) <= 30
for field in ["composerIcon", "logo"]:
    asset = (plugin / manifest["interface"][field]).resolve()
    assert asset.is_relative_to(plugin.resolve()) and asset.is_file()
mcp = json.loads((plugin / ".mcp.json").read_text(encoding="utf-8"))
assert mcp == {"mcpServers": {"familyassetmap": {"url": "https://familyassetmap.com/mcp"}}}
files = [".codex-plugin/plugin.json", ".mcp.json", "README.md", "LICENSE", "assets/icon.png", "skills/family-map/SKILL.md"]
output = root / "dist" / ("familyassetmap-codex-" + manifest["version"] + ".zip")
output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for file in files:
        path = plugin / file
        assert path.is_file() and not path.is_symlink()
        archive.write(path, file)
with zipfile.ZipFile(output) as archive:
    assert archive.namelist() == files
    assert archive.testzip() is None
print(str(output))
