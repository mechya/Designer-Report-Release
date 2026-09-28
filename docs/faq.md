# FAQ & troubleshooting

### Is Designer Report free?

Yes, completely. If it is useful to you, you can support development with a [coffee ☕](https://buymeacoffee.com/gurung.bhupesh).

### Is it made by Jaspersoft?

No. Designer Report is an independent project that uses the open-source JasperReports® Library. It is not affiliated with Cloud Software Group, Inc.

### Which JRXML versions are supported?

JasperReports **7.x** JRXML only. Reports made with Jaspersoft Studio 7 open directly. Reports made for JasperReports 6 or older (Jaspersoft Studio 6.x, iReport) use an older format that JasperReports 7 can't read — opening one fails with *Unable to load report*. Convert them first, for example by opening and saving them in Jaspersoft Studio 7.

The compiled `.jasper` files that **Build** writes need **JasperReports Library 7.x** in the application that fills them; they don't run on JasperReports 6.

### Can I use the reports in my own application?

Yes — they are yours. Use your workspace `.jrxml` files, or the compiled `.jasper` files from `build/jasper/` (or `build.zip`), together with the fonts in `build/fonts/`; put the `build/` folder itself on the classpath so JasperReports finds them, and set `SUBREPORT_DIR` to the folder of the report you are filling. When your application uses subreports, pass `SUBREPORT_DIR` (see [Subreports](subreports.md#paths-and-subreport_dir)).

### Preview says a font is not available

The report uses a font that is not in the workspace `fonts/` folder. Add it with **Tools → Manage Fonts → Add Font…**, or change the font in the Properties panel.

### A subreport is shown as *(not found)*

The report refers to a file that does not exist (renamed, moved or deleted). Right-click it in the Reports tab → **Delete** to remove the box, or fix the path in the subreport's expression. For old absolute paths use **Fix Subreport Paths…** on the workspace root.

### Preview says the band is taller than the page

Bands must fit on the page. Make elements smaller, move them, or reduce the band height.

### The crosstab does not fill

Crosstab groups cannot group empty (null) values. Make sure the bucket expression always has a value, e.g. `$F{category} != null ? $F{category} : "-"`.

### How do I update?

The Microsoft Store updates the app automatically. Your workspaces and settings are kept.

### Where are my settings stored?

In your user profile (Java preferences). Reports and their per-report settings (`.json-config`, `.notes.json`) are stored in your workspace.

### Something else?

See [Support](../SUPPORT.md).
