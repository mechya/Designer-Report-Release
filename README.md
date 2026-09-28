# Designer Report

**A free, lightweight visual designer for JasperReports® 7 reports (JRXML) — for Windows.**

Design reports on a visual canvas, edit the JRXML source side by side, and preview the filled report page by page, with full support for Japanese fonts and layouts.

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-support-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/gurung.bhupesh)

---

## Download

Designer Report for Windows 10 / 11 is available in the **Microsoft Store**:

<a href="https://apps.microsoft.com/detail/9N6XX87LGVS6"><img src="https://get.microsoft.com/images/en-us%20dark.svg" alt="Get it from Microsoft" width="200"></a>

No Java installation is needed — the app includes everything it requires. Updates are installed automatically by the Store.

## Compatibility — JasperReports 7 only

> [!IMPORTANT]
> Designer Report works with the **JasperReports® 7** JRXML format only.
>
> - **Reports made for JasperReports 6 or older** (for example with Jaspersoft® Studio 6.x or iReport) use an older JRXML format and **can't be opened**. Convert them first, for example by opening and saving them in Jaspersoft® Studio 7.
> - **Compiled `.jasper` files** from Designer Report need **JasperReports Library 7.x** in the application that fills them. They don't run on JasperReports 6.

## Features

- **New report in seconds** — start from a blank page, from a template (invoice, quotation, delivery note, purchase order, receipt, lists — built in, from your own folder, or from the online [template library](templates/README.md)), or from a description that the AI helper drafts. Check it in a live preview and change it before anything is saved.
- **Templates with versions** — keep your own templates in a folder (a shared team folder works too) and save any report as a template; every version stays available.
- **Template test** — fills a report with sample data in four cases (empty, short, just fits, too long) and shows cut-off text, growing boxes, missing fonts and "null" at a glance, with a PDF of each.
- **AI helper (optional, offline)** — a free AI model downloaded once that runs on your PC: realistic test text, template drafts and changes in plain words. Nothing you type leaves your computer.
- **Visual designer** — drag elements from the palette, move, resize, align and layer them; snap-to-grid, rulers and guide lines.
- **Source editor** — JRXML with syntax highlighting, kept in sync with the design view.
- **Preview** — compiles, fills and renders the report page by page.
- **Build** — compiles a workspace into a self-contained `build/` folder (and `build.zip`): the compiled `.jasper` files and only the fonts and images they use, ready to drop into your own application or onto a server.
- **Elements** — static text, text fields, images, lines, rectangles, ellipses, frames, page breaks, barcodes / QR codes, charts, crosstabs, lists, subreports, and page number / date / time fields.
- **Subreports made easy** — the *Reports* tab shows each report with its subreports; create, attach, open and delete subreports from the right-click menu.
- **Fonts** — manage the fonts of a workspace, preview them, and see each font's details (name, version, license).
- **JSON data sources** — pick a JSON file, detect fields automatically and preview with real data.
- **Japanese and English** user interface, **dark and light** themes.

See the **[User Guide](docs/user-guide.md)** for everything the app can do.

## Documentation

- [Getting started](docs/getting-started.md)
- [User guide](docs/user-guide.md)
- [Subreports](docs/subreports.md)
- [Fonts](docs/fonts.md)
- [FAQ & troubleshooting](docs/faq.md)

## Support

Found a bug or have an idea? See **[Support](SUPPORT.md)** — or open an [issue](https://github.com/mechya/Designer-Report-Release/issues/new/choose).

If Designer Report is useful to you, you can support its development with a **[coffee ☕](https://buymeacoffee.com/gurung.bhupesh)**. It is always free to use.

## License

Designer Report is **free to use** and is provided under the [Designer Report License](LICENSE.md). It is not open source.

It includes open-source software, listed with their licenses in [Third-Party Notices](THIRD_PARTY_NOTICES.md). See also the [Privacy Policy](PRIVACY.md).

JasperReports® is a registered trademark of Cloud Software Group, Inc. Designer Report is an independent project and is not affiliated with or endorsed by Cloud Software Group, Inc. or the Jaspersoft® team.

---

## 日本語

**Designer Report** は、JasperReports® 7（JRXML）用の無料・軽量なビジュアル帳票デザイナーです（Windows）。

- 新規作成ウィザード：空白、テンプレート（請求書・見積書・納品書・注文書・領収書・一覧、自分のフォルダーやオンラインのライブラリも）、またはAIによる下書きから作成。保存前にプレビューで確認・変更できます
- バージョン管理付きのテンプレート（チームの共有フォルダーにも対応）、「テンプレートとして保存」
- テンプレートのテスト：サンプルデータで文字の切れ・枠の伸び・フォント不足を確認し、PDF を出力
- AIヘルパー（任意・オフライン）：PC上で動く無料のAIモデル。入力した内容はPCの外に送られません
- キャンバスでのレイアウト編集、JRXML ソース編集、プレビュー、.jasper へのビルド
- サブレポートの作成・追加・削除（レポートタブ）
- 日本語フォントの管理とプレビュー、フォント情報の表示
- 日本語 / 英語 UI、ダーク / ライトテーマ

> [!IMPORTANT]
> **JasperReports® 7 専用です。** JasperReports 6 以前（Jaspersoft® Studio 6.x や iReport など）で作成した JRXML は形式が異なるため開けません。先に Jaspersoft® Studio 7 で開いて保存するなどして変換してください。Designer Report でビルドした `.jasper` を使うアプリには JasperReports Library 7.x が必要です（JasperReports 6 では動きません）。

ダウンロード：Microsoft Store から入手できます（更新は自動で行われます）。

<a href="https://apps.microsoft.com/detail/9N6XX87LGVS6?hl=ja-jp"><img src="https://get.microsoft.com/images/ja-jp%20dark.svg" alt="Microsoft から入手" width="200"></a>
不具合の報告・要望は [Issues](https://github.com/mechya/Designer-Report-Release/issues/new/choose) へ。
開発を応援していただける方は [Buy Me a Coffee](https://buymeacoffee.com/gurung.bhupesh) からどうぞ。

---

© 2026 Gurung Bhupesh. All rights reserved.
