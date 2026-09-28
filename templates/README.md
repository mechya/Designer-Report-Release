# Templates / テンプレート

Templates in this folder appear in Designer Report under **File > New > Template** when
**Show online templates** is switched on. Each template can have several versions; users pick
one, and older versions stay available.

このフォルダーのテンプレートは、Designer Report の「ファイル > 新規 > テンプレート」で
「オンラインのテンプレートも表示」をオンにすると表示されます。テンプレートごとに複数の
バージョンを持てます。以前のバージョンも選べます。

## Layout / 構成

```
templates/
  index.json                      built automatically - do not edit / 自動生成（編集しない）
  invoice-standard/
    meta.json                     title, category, tags, description
    1.0.0/template.jrxml
    1.0.0/thumbnail.png           optional (the app draws one if missing)
    1.0.0/version.json            optional: date and what changed
    1.1.0/...
```

The same layout works in a workspace's own `templates/` folder (My Templates), so a template
can be copied from one to the other as it is. In the app, **File > Save as Template** writes
exactly this layout, thumbnail included.

同じ構成はワークスペースの `templates/` フォルダー（マイテンプレート）でも使えます。
アプリの「ファイル > テンプレートとして保存」で、サムネイル付きでこの構成が作られます。

### meta.json

```json
{
  "title": { "ja": "請求書（標準）", "en": "Invoice (standard)" },
  "category": "billing",
  "tags": ["請求書", "invoice", "bill"],
  "description": { "ja": "ロゴ、宛先、明細、合計のある請求書。", "en": "Invoice with logo, customer, items and total." },
  "minAppVersion": "1.3.0"
}
```

`category`: `billing` (請求・見積), `delivery` (納品・発注), `list` (一覧), `hr` (人事・履歴書), `other` (その他).
`minAppVersion` is optional: older apps show the template as needing an update.

### version.json

```json
{ "updated": "2026-09-28", "changes": { "ja": "税率の列を追加", "en": "Added a tax rate column" } }
```

## Adding a template / テンプレートの追加

1. In Designer Report, open the report and use **File > Save as Template**.
2. Copy the folder it made (`<workspace>/templates/<name>/`) here, renaming it to lower-case
   letters, digits and `-` (for example `delivery-note-simple`).
3. Open a pull request. The check runs `python templates/build_index.py --check`.
4. After merging, the index is rebuilt automatically and the template appears in the app.

To publish a **new version**, add a new version folder (for example `1.2.0/`) next to the old
ones. Never change a version that is already published: users may have made reports from it.

**新しいバージョン**は、既存のフォルダーの横に新しいバージョンのフォルダー（例 `1.2.0/`）を
追加します。公開済みのバージョンは変更しないでください。

## Rules / ルール

- Use fonts every workspace has: **BIZ UDGothic / BIZ UDMincho** (bundled with the app), or no
  font name at all. Windows fonts such as MS Gothic are not available everywhere.
- Pictures use workspace paths such as `images/logo.png`, never absolute paths. A missing logo
  should not stop the report (`onErrorType="Blank"`).
- Report expressions are Java code that runs on the user's computer. Templates must only format
  fields and variables; the check rejects file, network, process and reflection access, and every
  pull request is reviewed by a person before it is merged.
- No subreports for now: a template is a single `template.jrxml`.
