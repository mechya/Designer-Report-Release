# Subreports

A subreport is a report placed inside another report — for example page sections of a form, each designed in its own file.

## Seeing which report uses what

Open the **Reports** tab of the Project Explorer:

```
▼ page1.jrxml
    ├ PersonalInfo.jrxml
    └ Education.jrxml
▼ page2.jrxml
    ├ Qualifications.jrxml
    └ Motivation.jrxml
```

- *(not found)* — the report refers to a subreport file that does not exist.
- *(circular)* — a report that (directly or indirectly) includes itself.
- Hover a subreport to see all reports that use it.

## Creating and attaching

Right-click a report in the Reports tab (or a `.jrxml` in the Files tab):

- **New Subreport…** — enter a name and a height. The new file is created next to the report, as wide as the report's column, with no margins and the report's styles and fonts. It is placed below the last element of the report and selected.
- **Attach Existing Subreport…** — choose a report from the list (reports not used anywhere come first). Its page height is used as the box height.

The change is made in the report's tab: **Ctrl+Z** undoes it, and you save the report as usual.

If the band has no free space left, the subreport is still added below the last element and you are warned that the band is taller than the page — move or resize elements, otherwise the report does not compile.

## Showing and deleting

Right-click a subreport in the Reports tab:

- **Show in *report*** — opens the report and selects the subreport box.
- **Delete** — deletes the subreport file **and removes its boxes from every report that uses it**. Reports that are open without other unsaved changes are saved automatically. **Ctrl+Z** right afterwards restores the file and all boxes; the deleted file also goes to the Recycle Bin / Trash.

For a subreport whose file is missing, **Delete** removes the dead box from the report.

Double-click a subreport box on the design canvas to open its file.

## Paths and `SUBREPORT_DIR`

Subreports are found relative to the main report. The recommended expression is:

```
net.sf.jasperreports.engine.JasperCompileManager.compileReport($P{SUBREPORT_DIR} + "Part.jrxml")
```

with a report parameter `SUBREPORT_DIR` (default `""`). New Subreport / Attach write exactly this, and also pass `SUBREPORT_DIR` on to the subreport, so subreports inside subreports — and in subfolders — work too.

- **In Designer Report**, Preview sets `SUBREPORT_DIR` to the main report's folder automatically. Workspaces can be moved or shared between Windows and macOS.
- **In your own application**, pass the folder when filling the report:

  ```java
  params.put("SUBREPORT_DIR", "/path/to/reports/");
  ```

  Without it, a relative path is resolved against the program's working directory, not the report's folder.

### Old reports with absolute paths

Right-click the workspace root → **Fix Subreport Paths…**. The app lists every absolute path it will change (for example `"C:/Users/…/reports/"` → `""`), saves a `.bak` copy of each file and skips files with unsaved changes.
